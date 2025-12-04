# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from pydantic import BaseModel

# Metadata offering methods corresponds to how the metadata is provided, e.g.,
# embedded JSON-LD in HTML (json_in_html), Microdata (microdata),
# HTML meta tags (meta_tags), RDFa (rdfa), typed links (typed_links),
# signposting links (signposting), and Content Negotiation (content_negotiation).


class MetadataOfferingMethod(BaseModel):
    label: str
    acronym: str
