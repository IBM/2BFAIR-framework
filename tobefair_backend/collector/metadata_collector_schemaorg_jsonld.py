# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

import json
import re
from typing import Any, ClassVar, Dict, List

import extruct
import jmespath

from tobefair_backend.constants import SCHEMA_ORG_DATASET_TYPES
from tobefair_backend.model.resources.data_size import DataSize, DataType, DataUnit
from tobefair_backend.model.resources.license_information import LicenseInformation
from tobefair_backend.model.resources.typed_link import TypedLink
from tobefair_backend.utils.dict_utils import (
    remove_empty_fields,
    remove_empty_list_values,
)
from tobefair_framework.core.collector.metadata_collector import MetadataCollector
from tobefair_framework.model.metadata.metadata_keys import (
    MetadataSourceKeys,
    MetadataStandardName,
)
from tobefair_framework.model.metadata.metadata_record import MetadataRecord


class MetadataCollectorSchemaOrgJsonLD(MetadataCollector):

    # TODO: Implement method to read schema.org contexts if it is needed in our case.
    SCHEMA_ORG_CONTEXT: ClassVar = (
        SCHEMA_ORG_DATASET_TYPES  # Preprocessor.get_schema_org_context()
    )
    # TODO: Implement method to read creativeworks contexts if it is needed in our case.
    SCHEMA_ORG_CREATIVEWORKS: ClassVar = (
        SCHEMA_ORG_DATASET_TYPES  # Preprocessor.get_schema_org_creativeworks()
    )
    SCHEMA_ORG_MAPPING: ClassVar = (
        '{name: name[*]."@value" || name || headline[*]."@value" || '
        'headline, "@type": "@type", '
        'datePublished: datePublished."@value" || datePublished || dateCreated, '
        'modified_date: dateModified."@value" ||dateModified, '
        "creator: creator[?\"@type\" =='Person'].name || "
        "creator[?\"@type\" =='Organization'].name || author[*].name || "
        "creator[*].name || creator.name || author.name, "
        "creator_first: creator[*].givenName || author[*].givenName || "
        "creator.givenName || author.givenName,"
        "creator_last: creator[*].familyName || author[*].familyName || "
        "creator.familyName || author.familyName,"
        "contributor: contributor[*].name || contributor[*].familyName, "
        "right_holder: copyrightHolder[*].name || copyrightHolder[*].familyName, "
        "publisher: publisher.name || provider.name || publisher || provider, "
        'license: license."@id" || license[?"@type" ==\'CreativeWork\'].id || '
        "license[?\"@type\" =='CreativeWork'].url || "
        "license[?\"@type\" =='CreativeWork'].name || license, "
        "description: description, keywords: keywords, "
        "identifier: [((identifier.value || identifier[*].value || "
        'identifier || "@id") || (url || url."@id")) , '
        '(sameAs."@id" || sameAs[0]."@id" || sameAs.url || '
        "sameAs[0].url || sameAs)][], "
        "access_level: conditionsOfAccess, "
        "access_free:  (isAccessibleForFree || free), "
        "measured_variable: variableMeasured[*].name || variableMeasured , "
        "object_size: size,"
        'related_resources: [{related_resource: (isPartOf."@id" || isPartOf[0]."@id" '
        "|| isPartOf.url || isPartOf[0].url || isPartOf), "
        "relation_type: 'isPartOf'}, "
        '{related_resource: (sameAs."@id" || sameAs[0]."@id" || sameAs.url || '
        "sameAs[0].url || sameAs), relation_type: 'sameAs'},"
        '{related_resource: (includedInDataCatalog."@id" || '
        'includedInDataCatalog[0]."@id" || includedInDataCatalog.url || '
        "includedInDataCatalog[0].url || includedInDataCatalog.name || "
        "includedInDataCatalog[0].name || "
        "includedInDataCatalog), relation_type: 'isPartOf'}, "
        '{related_resource: (subjectOf."@id" || subjectOf[0]."@id" || subjectOf.url ||'
        "subjectOf[0].url || subjectOf.name || subjectOf[0].name || subjectOf), "
        "relation_type: 'isReferencedBy'},"
        '{related_resource: (isBasedOn."@id" || isBasedOn[0]."@id" || isBasedOn.url '
        "|| isBasedOn[0].url || isBasedOn) , relation_type: 'isBasedOn'} , "
        '{related_resource: "@reverse".isBasedOn[0]."@id" || '
        '"@reverse".isBasedOn."@id" || "@reverse".isBasedOn[0].url || isBasedOn ,'
        "relation_type: 'isBasisFor'} ], "
        "object_content_identifier: (distribution[*].{url: contentUrl, type: "
        "(encodingFormat || fileFormat), size: (contentSize || fileSize), "
        "profile: schemaVersion} || [distribution.{url: contentUrl, type: "
        "(encodingFormat || fileFormat), size: (contentSize || fileSize),"
        " profile: schemaVersion}])"
        "language: inLanguage.name || inLanguage.alternateName || inLanguage}"
    )

    @classmethod
    def get_metadata_record(
        cls, raw_digital_object: str | dict
    ) -> MetadataRecord | None:
        raw_digital_object_str = (
            raw_digital_object
            if isinstance(raw_digital_object, str)
            else json.dumps(raw_digital_object)
        )
        return cls.extract_json_ld_metadata_from_landing_page_body(
            landing_page_body=raw_digital_object_str
        )

    @classmethod
    def get_content_links(cls, schemaorg_raw_value: dict) -> List[TypedLink]:
        """
        corresponds to F-UJI's object_content_identifier. Currently,
        supports only Schema.org Dataset type
        """
        jmespath_query = (
            "(distribution[*].{url: (contentUrl || url), "
            "type: (encodingFormat || fileFormat), size: (contentSize || fileSize),"
            " profile: schemaVersion} || [distribution.{url: (contentUrl || url), "
            "type: (encodingFormat || fileFormat), size: (contentSize || fileSize)"
            ", profile: schemaVersion}])"
        )
        try:
            results = jmespath.search(jmespath_query, schemaorg_raw_value)
            secondary_size_jmespath_query = "size.{value: value, unit: unitText}"
            secondary_size_information = jmespath.search(
                secondary_size_jmespath_query, schemaorg_raw_value
            )
            return [
                TypedLink(
                    href=result.get("url"),
                    type=(
                        DataType(value=type_value)
                        if (type_value := result.get("type"))
                        else None
                    ),
                    profile=result.get("profile"),
                    content_size=(
                        DataSize.from_string(size)
                        if (size := result.get("size"))
                        else (
                            DataSize(value=value, unit=DataUnit(name=unit))
                            if (
                                (value := secondary_size_information.get("value"))
                                and (unit := secondary_size_information.get("unit"))
                            )
                            else None
                        )
                    ),
                    measured_variable=cls.measured_variable(schemaorg_raw_value),
                )
                for result in results
                if result is not None
            ]
        except Exception:
            return []

    @classmethod
    def measured_variable(cls, schemaorg_raw_value: dict) -> List[str] | None:
        jmespath_query = "variableMeasured[*].name || variableMeasure"
        try:
            matches = jmespath.search(jmespath_query, schemaorg_raw_value)
            is_single_value = not isinstance(matches, list)
            matches = [matches] if is_single_value and matches is not None else matches
            return matches
        except Exception:
            return None

    @classmethod
    def get_license_information(
        cls, schemaorg_raw_value: dict, license_metadata_key: str | None
    ) -> LicenseInformation | None:
        if license_information_raw_value := schemaorg_raw_value.get(
            license_metadata_key
        ):
            if license_information_raw_value != "":
                return LicenseInformation(raw_value=license_information_raw_value)
        return None

    @classmethod
    def _retrieve_metadata_from_html(
        cls, html_body: str, metadata_syntaxes=["json-ld"]
    ) -> Dict | None:
        extracted: dict | None = None
        try:
            html_body = re.sub("(<!--.*?-->)", "", html_body)
        finally:
            try:
                html_body_bytes = html_body.encode("utf-8")
                extracted = extruct.extract(
                    html_body_bytes, encoding="UTF-8", syntaxes=["schema.org"]
                )
            except Exception:
                try:
                    extracted = extruct.extract(
                        html_body_bytes, syntaxes=metadata_syntaxes
                    )
                except Exception as e:
                    raise e

        if isinstance(extracted, dict):
            extracted = remove_empty_list_values(extracted)
        return extracted

    @classmethod
    def extract_json_ld_metadata_from_landing_page_body(
        cls, landing_page_body: str
    ) -> MetadataRecord | None:
        if not (
            (all_metadata := cls._retrieve_metadata_from_html(landing_page_body))
            and (json_ld_metadata := all_metadata.get("json-ld"))
        ):
            return None
        if isinstance(json_ld_metadata, list):
            if len(json_ld_metadata) > 0:
                json_ld_metadata = json_ld_metadata[0]
            else:
                return None
        found_metadata_standard = None
        if cls._metadata_is_schema_org(json_ld_metadata):
            found_metadata_standard = MetadataStandardName.SCHEMA_ORG
        return MetadataRecord(
            is_machine_retrieved=True,
            raw_value=remove_empty_fields(json_ld_metadata),
            metadata_standard_name=found_metadata_standard,
            metadata_source_key=MetadataSourceKeys.SCHEMA_ORG_EMBEDDED,
        )

    @classmethod
    def _metadata_is_schema_org(cls, raw_metadata: dict) -> bool:
        return (
            "@context" in raw_metadata.keys()
            and str(raw_metadata.get("@context")).find("://schema.org") > -1
        )

    @classmethod
    def get_schema_org_metadata(cls, json_ld: dict) -> MetadataRecord | None:
        extracted_metadata: dict[Any, Any] | None = {}
        # TODO: Discover where namespace variable is used by F-UJI
        namespaces = list()

        # self.logger.info('FsF-F2-01M :
        # Trying to extract schema.org JSON-LD metadata from -: {}'.format(
        #     self.source_name.name))
        # TODO check syntax - not ending with /, type and @type
        # TODO (important) extend mapping to detect other pids
        # (link to related entities)?
        try:
            # if ext_meta['@context'] in check_context_type['@context']
            # and ext_meta['@type'] in check_context_type["@type"]:
            if cls._metadata_is_schema_org(json_ld):
                schema_org_namespace = cls._get_schema_org_namespace(json_ld)
                json_ld = json.loads(
                    json.dumps(json_ld).replace('"' + schema_org_namespace + ":", '"')
                )
                cls._handle_main_entity(json_dict=json_ld)
                extracted_metadata = jmespath.search(cls.SCHEMA_ORG_MAPPING, json_ld)
                if extracted_metadata:
                    namespaces.append("http://schema.org/")
                    cls._handle_creator(extracted_metadata=extracted_metadata)
                    cls._get_license(extracted_metadata=extracted_metadata)
                    cls._filter_out_none_related_resources(
                        extracted_metadata=extracted_metadata
                    )
                    return MetadataRecord(
                        is_machine_retrieved=True,
                        raw_value=remove_empty_fields(extracted_metadata),
                        metadata_standard_name=MetadataStandardName.SCHEMA_ORG,
                        metadata_source_key=MetadataSourceKeys.SCHEMA_ORG_EMBEDDED,
                    )
            else:
                # self.logger.info('FsF-F2-01M :
                # Found JSON-LD but record is not of type schema.org
                # based on context -: ' + str(json_dict.get('@context')))
                msg = "Found JSON-LD but record is not of type schema.org"
                print(
                    "FsF-F2-01M : "
                    + msg
                    + " based on context -: "
                    + str(json_ld.get("@context"))
                )
                return None

        except Exception as err:
            # print(err.with_traceback())
            # self.logger.info('FsF-F2-01M :
            # Failed to parse JSON-LD schema.org -: {}'.format(err))
            print(("FsF-F2-01M : Failed to parse JSON-LD schema.org -: {}".format(err)))
            # self.logger.info('FsF-F2-01M :
            # Could not identify JSON-LD schema.org metadata from ingested JSON dict')
            msg = (
                "Could not identify JSON-LD schema.org metadata from ingested JSON dict"
            )
            print("FsF-F2-01M : " + msg)
        return None

    @classmethod
    def _get_schema_org_namespace(cls, json_ld: dict) -> str:
        if (digital_object_context := json_ld.get("@context")) and isinstance(
            digital_object_context, dict
        ):
            # TODO: check this loop because it just leaves in schema_org_namespace
            # the last context_uri that ends with schema.org.
            for context_name, context_uri in digital_object_context.items():
                if context_uri.endswith("schema.org/"):
                    return context_name
        return "schema"

    @classmethod
    def _handle_main_entity(cls, json_dict: dict):
        # special case #1
        if not (digital_object_main_entity := json_dict.get("mainEntity")):
            return
        # self.logger.info('FsF-F2-01M : \'MainEntity\' detected in JSON-LD,
        # trying to identify its properties')
        msg = "'MainEntity' detected in JSON-LD, trying to identify its properties"
        print("FsF-F2-01M : " + msg)
        # TODO: check this code because it is transforming properties of
        # a mainEntity to properties of the dict.
        # TODO: Understand why it is looping through main entity
        # and checking if it is a dict all the time.
        # This checking code stay in the previous
        # if because the transformation is done just if the mainEntity
        # is a dict.
        for main_entity_prop in digital_object_main_entity:
            json_dict[main_entity_prop] = digital_object_main_entity.get(
                main_entity_prop
            )

        # special case #2
        # TODO: this code was also commented in th F-UJI implementation.
        # Implement a function to handle it if it is needed.
        # if json_dict.get('@graph'):
        #    self.logger.info('FsF-F2-01M :
        # Seems to be a JSON-LD graph, trying to compact')
        # ext_meta = self.compact_jsonld(ext_meta)

    @classmethod
    def _handle_creator(cls, extracted_metadata):
        if extracted_metadata.get("creator") is None:
            first = extracted_metadata.get("creator_first")
            last = extracted_metadata.get("creator_last")
            if last:
                if isinstance(first, list) and isinstance(last, list):
                    if len(first) == len(last):
                        # TODO: Understand why zip is here
                        names = [str(i) + " " + str(j) for i, j in zip(first, last)]
                        extracted_metadata["creator"] = names
                else:
                    extracted_metadata["creator"] = [str(first) + " " + str(last)]

    @classmethod
    def _handle_object_size(cls, json_ld_metadata):
        if json_ld_metadata.get("object_size"):
            # print(jsnld_metadata.get('object_size'))
            if isinstance(json_ld_metadata["object_size"], dict):
                # TODO: Check if we can consider that the value is correctly
                # in the document when object size is a dict.
                # For example,
                # the file could have typos or other errors
                # and the field does not exists.
                json_ld_metadata["object_size"] = str(
                    json_ld_metadata["object_size"].get("value")
                )

            # jsnld_metadata['object_size'] =
            # str(jsnld_metadata['object_size'].get('value')) + ' '+
            # jsnld_metadata['object_size'].get('unitText')

    @classmethod
    def _get_license(cls, extracted_metadata):
        invalid_license = False
        if extracted_metadata.get("license"):
            # self.logger.info('FsF-R1.1-01M :
            # License metadata found (schema.org) -: {}'.format(
            #     json_ld_metadata.get('license')))
            if not isinstance(extracted_metadata.get("license"), list):
                extracted_metadata["license"] = [extracted_metadata["license"]]
            lk = 0
            for license in extracted_metadata.get("license"):
                # TODO: Check it processes only licenses that are presented as dict.
                if isinstance(license, dict):
                    ls_type = license.get("@type")
                    # license can be of type URL or CreativeWork
                    if ls_type == "CreativeWork":
                        ls = license.get("url")
                        if not ls:
                            ls = license.get("name")
                        if ls:
                            extracted_metadata["license"][lk] = ls
                        else:
                            invalid_license = True
                    else:
                        invalid_license = True
                    if invalid_license:
                        # self.logger.warning(
                        #     'FsF-R1.1-01M : Looks like schema.org representation of
                        # license is incorrect.'
                        # )
                        extracted_metadata["license"][lk] = None
                lk += 1

    @classmethod
    def _filter_out_none_related_resources(cls, extracted_metadata):
        # filter out None values of related_resources
        if extracted_metadata.get("related_resources"):
            related = [
                d
                for d in extracted_metadata["related_resources"]
                if d["related_resource"] is not None
            ]
            if related:
                extracted_metadata["related_resources"] = related
                # self.logger.info('FsF-I3-01M : {0}
                # related resource(s) extracted from -: {1}'.format(
                #     len(json_ld_metadata['related_resources']),
                # self.source_name.name))
            else:
                del extracted_metadata["related_resources"]
                # self.logger.info('FsF-I3-01M :
                # No related resource(s) found in Schema.org metadata')
