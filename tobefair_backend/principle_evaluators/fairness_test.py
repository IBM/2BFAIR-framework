from typing import ClassVar, List

from tobefair_backend.constants import FAIRNESS_CONFIGURATION_FILE_PATH
from tobefair_framework.core.configuration.fairness_configuration_file_dao import (
    FAIRnessConfigurationFileDAO,
)
from tobefair_framework.framework_constants import ALLOW_DUPLICATE_TESTS
from tobefair_framework.model.identifier.fairness_test_id import FAIRnessTestID


def basic_function(self, *args, **kwargs):
    pass


def should_execute_test(test_id: FAIRnessTestID) -> bool:
    fairness_configuration = FAIRnessConfigurationFileDAO(
        file_path=FAIRNESS_CONFIGURATION_FILE_PATH
    )
    test_configuration = fairness_configuration.read_configuration()
    test_ids_to_evaluate = test_configuration.get_fairness_test_ids_to_evaluate()
    return test_id in test_ids_to_evaluate


def fairness_test(test_id: FAIRnessTestID):
    def decorator(function):
        FAIRnessTestRegistry.define_test(test_id)
        if should_execute_test(test_id):

            def wrapper(self, *args, **kwargs):
                return function(self, *args, **kwargs)

            return wrapper
        return basic_function

    return decorator


class FAIRnessTestRegistry:
    _defined_tests: ClassVar[List[FAIRnessTestID]] = []

    @classmethod
    def define_test(cls, test_id: FAIRnessTestID):
        if cls.test_has_been_defined(test_id) and not ALLOW_DUPLICATE_TESTS:
            raise DuplicateFAIRnessTestError(duplicate_test_id=test_id)
        cls._defined_tests += [test_id]

    @classmethod
    def test_has_been_defined(cls, test_id: FAIRnessTestID) -> bool:
        return test_id in cls._defined_tests


class DuplicateFAIRnessTestError(Exception):
    def __init__(self, duplicate_test_id: FAIRnessTestID) -> None:
        error_message = (
            f"FAIRness test with ID {duplicate_test_id.value} declared twice"
        )
        super().__init__(error_message)
