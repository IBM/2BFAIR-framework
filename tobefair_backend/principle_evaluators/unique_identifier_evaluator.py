from typing import ClassVar, List

from tobefair_backend.principle_evaluators.fairness_test import fairness_test
from tobefair_framework.core.evaluator.fairness_principle_evaluator import (
    evaluator_of_principle,
)
from tobefair_framework.core.evaluator.principle_evaluator import PrincipleEvaluator
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleIDs
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestIDs
from tobefair_framework.model.identifier.identifier_info import IdentifierInfo
from tobefair_framework.model.identifier.identifier_type import IdentifierType
from tobefair_framework.model.results.test_result import TestResult


@evaluator_of_principle(FAIRPrincipleIDs.F1.value)
class UniqueIdentifierEvaluator(PrincipleEvaluator):

    VALID_PIDS: ClassVar[dict] = {
        "ark": {
            "label": "Archival Resource Key (ARK)",
            "source": "datacite.org",
        },
        "arxiv": {"label": "arXiv Submission ID", "source": "datacite.org"},
        "bioproject": {"label": "BioProject ID", "source": "identifiers.org"},
        "biosample": {"label": "BioSample ID", "source": "identifiers.org"},
        "doi": {
            "label": "Digital Object Identifier (DOI)",
            "source": "datacite.org",
        },
        "ensembl": {"label": "Ensembl ID", "source": "identifiers.org"},
        "genome": {
            "label": "GenBank or RefSeq genome",
            "source": "identifiers.org",
        },
        # identifier by idutils and,
        # if is the case, define an approach to not consider gnd in the identification.
        # Example to test: "1701892803_487152_3f90d213_db45_4cb2_a262_b33e49b722bc"
        #    'gnd':{'label':'Gemeinsame Normdatei (GND) ID','source':'f-uji.net'},
        "handle": {"label": "Handle System ID", "source": "datacite.org"},
        "lsid": {"label": "Life Science Identifier", "source": "datacite.org"},
        "pmid": {"label": "PubMed ID", "source": "datacite.org"},
        "pmcid": {"label": "PubMed Central ID", "source": "identifiers.org"},
        "purl": {
            "label": "Persistent Uniform Resource Locator (PURL)",
            "source": "datacite.org",
        },
        "refseq": {"label": "RefSeq ID", "source": "identifiers.org"},
        "sra": {
            "label": "Sequence Read Archive (SRA) ID",
            "source": "identifiers.org",
        },
        "uniprot": {"label": "UniProt ID", "source": "identifiers.org"},
        "urn": {
            "label": "Uniform Resource Name (URN)",
            "source": "datacite.org",
        },
        "identifiers.org": {
            "label": "Identifiers.org Identifier",
            "source": "identifiers.org",
        },
        "w3id": {
            "label": "Permanent Identifier for the Web (W3ID)",
            "source": "identifiers.org",
        },
    }

    def evaluate(self, evaluation_subject: DigitalObjectInfo) -> List[TestResult]:
        identifier_info: IdentifierInfo = evaluation_subject.identifier_info
        identifier_type: IdentifierType = identifier_info.get_identifier_type()
        return [
            self._evaluate_identifier_type_f1_01md_1(identifier_type=identifier_type),
            self._evaluate_identifier_is_guid_f1_01md_2(
                identifier_type=identifier_type,
                preferred_schema=identifier_info.preferred_schema,
            ),
            self._evaluate_identifier_syntax_against_persistence_schema_f1_02md_1(
                preferred_schema=identifier_info.preferred_schema
            ),
        ]

    @classmethod
    def follows_persistent_identifier_schema(cls, preferred_schema: str) -> bool:
        return True if (preferred_schema in cls.VALID_PIDS.keys()) else False

    @fairness_test(FAIRnessTestIDs.F1_01MD_1_Hash_or_UUID.value)
    def _evaluate_identifier_type_f1_01md_1(
        self, identifier_type: IdentifierType
    ) -> TestResult:
        test_id = FAIRnessTestIDs.F1_01MD_1_Hash_or_UUID.value
        test_configuration = self._tests_configuration[test_id]
        if (
            identifier_type == IdentifierType.UUID
            or identifier_type == IdentifierType.HASH
        ):
            prefix = "an" if identifier_type == IdentifierType.UUID else "a"
            result_details = (
                f"Identifier follows {prefix} {identifier_type} type syntax."
            )
            test_result = test_configuration.make_passed_test_result(
                result_details=result_details,
            )
        else:
            test_result = test_configuration.make_failed_test_result()
        return test_result

    @fairness_test(FAIRnessTestIDs.F1_01MD_2_GUID.value)
    def _evaluate_identifier_is_guid_f1_01md_2(
        self, identifier_type: IdentifierType, preferred_schema: str | None
    ) -> TestResult:
        test_id = FAIRnessTestIDs.F1_01MD_2_GUID.value
        test_configuration = self._tests_configuration[test_id]
        evaluated_requirements = test_configuration.agnostic_requirements
        if identifier_type == IdentifierType.GUID:
            assert (
                preferred_schema
            ), "Preferred schema cannot be None if the identifier is a GUID"
            description = (
                "Identifier follows a defined unique identifier syntax "
                f"({preferred_schema})."
            )
            test_result = test_configuration.make_passed_test_result(
                result_description=description,
                evaluated_requirements=evaluated_requirements,
            )
        else:
            test_result = test_configuration.make_failed_test_result()
        return test_result

    @fairness_test(FAIRnessTestIDs.F1_02MD_1_GUPRI.value)
    def _evaluate_identifier_syntax_against_persistence_schema_f1_02md_1(
        self, preferred_schema: str | None
    ):
        test_id = FAIRnessTestIDs.F1_02MD_1_GUPRI.value
        test_configuration = self._tests_configuration[test_id]
        evaluated_requirements = test_configuration.agnostic_requirements
        if preferred_schema and self.follows_persistent_identifier_schema(
            preferred_schema=preferred_schema
        ):
            test_result = test_configuration.make_passed_test_result(
                evaluated_requirements=evaluated_requirements
            )
        else:
            test_result = test_configuration.make_failed_test_result(
                evaluated_requirements=evaluated_requirements
            )
        return test_result
