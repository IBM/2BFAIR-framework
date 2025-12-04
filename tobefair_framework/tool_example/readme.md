# Steps to implement a FAIRness evaluation tool

- Create a package for the FAIRness evaluation tool, e.g., the package [tool_example](../tool_example/).
- Create a module for the digital object collector implementation
  - E.g.: Implementation of `DigitalObjectCollectorFromFile` in the module [digital_object_collector_from_file.py](digital_object_collector_from_file.py), inheriting from `DigitalObjectCollector`, and implementing the method `_read_digital_object_info()`.
- Create a module for the class responsible to parser the digital object content to a metadata representation
  - E.g.: Implementation of the class `MetadataCollectorSchemaorgJsonldSimple` in the module [metadata_collector_schema_org_json_ld_simple.py](./metadata_collector_schema_org_json_ld_simple.py), inheriting from `MetadataCollector`, and implementing the method `get_metadata_record()`.
  - In our simple example, the digital object is stored in file already in json-ld representation.
- Create a script for the code to invoke the evaluators (e.g., [main_example.py](./main_example.py)) that runs the FAIRness evaluation.
- Create an example of digital object to be handled by your tool, e.g., the json-ld file [digital_object_example.json](./digital_object_example.json).
- Create a package for the evaluators, e.g., [principle_evaluators](./principle_evaluators/), and implement classes for each FAIRness metric and test. 
  - In our example we implemented the `UniqueIdentifierEvaluator` present in the module [unique_identifier_evaluator.py](./principle_evaluators/unique_identifier_evaluator.py) with two tests to:
    - Check if the identifier is a hash or a UUID.
    - Check if the identifier is a GUID.
  - We decorate the class with `@evaluator_of_principle(FAIRPrincipleIDs.F1.value)` since it is responsible to evaluate FAIRness considering the principle `F1`. The decorator register this class as an evaluator to be used in the FAIRness assessment.