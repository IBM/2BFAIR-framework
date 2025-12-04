# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from tobefair_framework.model.identifier.fair_principle_id import FAIRPrincipleID


def evaluator_of_principle(principle: FAIRPrincipleID):
    def decorator(cls):
        EvaluatorRegistry.set_evaluator(cls)
        cls._fair_principle_to_evaluate = principle
        return cls

    return decorator


class EvaluatorRegistry:
    _evaluators: ClassVar[list[type]] = []

    @classmethod
    def set_evaluator(cls, evaluator: type):
        cls._evaluators.append(evaluator)

    @classmethod
    def get_evaluators(cls) -> list[type]:
        return cls._evaluators
