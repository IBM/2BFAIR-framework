# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import cast

from tobefair_framework.core.evaluator.fairness_principle_evaluator import (
    EvaluatorRegistry,
)
from tobefair_framework.core.evaluator.principle_evaluator import PrincipleEvaluator
from tobefair_framework.model.configuration.fairness_configuration import (
    FAIRnessConfiguration,
)
from tobefair_framework.model.digital_object_info import DigitalObjectInfo
from tobefair_framework.model.identifier.fair_dimension_id import FAIRDimensionIDs
from tobefair_framework.model.results.fairness_result import FAIRResults, OverallResult
from tobefair_framework.model.results.test_specific_recommendation import (
    TestSpecificRecommendation,
)


def load_evaluators(name):
    import importlib
    import os

    slashed_name = name.replace(".", os.sep)
    subdirs = os.listdir(slashed_name)
    for subdir in subdirs:
        if ".py" == subdir[-3:]:
            subdir = subdir[:-3]
            importlib.__import__(f"{name}.{subdir}")


class Evaluator:

    @classmethod
    def evaluate(
        cls,
        digital_object: DigitalObjectInfo,
        fairness_configuration: FAIRnessConfiguration,
    ) -> FAIRResults:
        evaluators = EvaluatorRegistry.get_evaluators()
        test_results = []
        [
            test_results := test_results
            + evaluator.evaluate(evaluation_subject=digital_object)
            for evaluator in [
                cast(
                    PrincipleEvaluator,
                    evaluator(fairness_configuration=fairness_configuration),
                )
                for evaluator in evaluators
            ]
        ]
        dimension_results = FAIRResults.from_test_results(
            test_results=test_results, fairness_configuration=fairness_configuration
        )
        dimension_results.sort_all()
        return dimension_results

    @classmethod
    def get_overall_results(
        cls,
        digital_object: DigitalObjectInfo,
        dimension_results: FAIRResults,
        community: str,
        task: str,
    ) -> OverallResult:
        priority_recommendations = (
            TestSpecificRecommendation.get_priority_test_specific_recommendations(
                test_specific_recommendations=(
                    dimension_results.get_necessary_test_specific_recommendations()
                ),
                number_of_recommendations=8,
            )
        )
        landing_page_url = (
            landing_page.url if (landing_page := digital_object.landing_page) else None
        )
        overall_result = OverallResult(
            evaluation_id=digital_object.identifier_info.identifier,
            evaluated_digital_object_id=digital_object.identifier_info.identifier,
            evaluated_metadata_record_id=digital_object.identifier_info.identifier,
            evaluated_digital_object_landing_page_url=landing_page_url,
            community=community,
            task=task,
            evaluation_score=dimension_results.get_overall_score(
                predefined_order=[
                    FAIRDimensionIDs.F.value,
                    FAIRDimensionIDs.A.value,
                    FAIRDimensionIDs.I.value,
                    FAIRDimensionIDs.R.value,
                ]
            ),
            priority_recommendations=priority_recommendations,
        )
        return overall_result

    @classmethod
    def get_metadata_info(cls, digital_object_info: DigitalObjectInfo):
        evaluated_metadata = (
            digital_object_info.metadata_record.raw_value
            if digital_object_info.metadata_record is not None
            else {}
        )
        return evaluated_metadata
