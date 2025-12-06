# 2BFAIR Framework

2BFAIR-framework is a framework for automated FAIRness assessment of digital resources according to the FAIR principles. These principles correspond to 15 recommendations for improving the Findability, Accessibility, Interoperability, and Reusability of data objects but also algorithms, vocabularies, tools, workflows, and other data-related services insofar as they are made available as digital objects. FAIRness corresponds to a grade indicating how close a digital object is to abiding by the FAIR principles considered relevant for a community or task.

2BFAIR was designed as a framework to support full customization of the FAIRness evaluation. Customization is a crucial requirement partially addressed by existing automated tools. As a framework, 2BFAIR implements frozen spots, which encapsulate common complex logic required by any evaluation. For customization, it provides hot spots that users can adjust to fit specific needs. Besides, 2BFAIR teaches FAIR during its use and gives recommendations about how to improve the FAIR of digital objects according to the user's community priorities.

Packages descriptions:

- `tobefair_framework` main code of 2BFAIR.
- `tobefair_framework/model`: implementation of the data types used through the code, e.g., for configuration, fairness evaluation, identifier, metadata, request, results.
- `tobefair_framework/core`: implementation of the classes for, e.g., getting the configuration (`configuration`) collecting the resource (`collector`), executing the evaluation (`evaluator`).
- `tobefair_framework/core/controller`: classes to execute the use case required to perform evaluations, i.e., it calls the other components to execute the whole evaluation workflow.
- `tobefair_framework/tool_example`: an example of an application to call 2BFAIR-framework components. The users of the framework can start running this application to understand the 2BFAIR-framework code. The main code is in the file `main_example.py`. The file `tobefair_framework/tool_example/readme.md` explains how the tool example was implemented.

## To cite this work

AZEVEDO, L. G., CAROLI, E., CORRÊA, B. S., DA SILVA, V. T. “[2BFAIR: Framework for Automated FAIRness assessment](https://ceur-ws.org/Vol-3977/NSLP-09.pdf)”. In: 2nd International Workshop on Natural Scientific Language Processing and Research Knowledge Graphs (NSLP 2025), co-located with ESWC 2025, June 01–02, Portorož, Slovenia, 2025.

## Configuring the Environment

Using a virtual environment for all commands.

### Create a virtual environment

- We are using Python 3.11. If you are using pyenv, you can install Python 3.11 running: `pyenv install 3.11`.
- Create a virtual environment: `pyenv virtualenv 3.11.12 tobefair_framework`
- Start the environment running `pyenv shell tobefair_framework`
- Run `pyenv local tobefair_framework` to generate a `.python-version` with the Python version of the environment.

- Other useful commands:
  - `pyenv versions`
  - `pyenv virtualenvs`

- To start VS Code with the environment set, ensure that the following commands are in your `~/.zshrc` file.

```cli
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

## Installation

### How to install the framework as a library

```sh
# assuming you have an SSH key set up on GitHub
pip install "git+ssh://git@github.com/IBM/2BFAIR-framework.git@main"
```

### Suggested setup for development

```sh
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install -r dev_requirements.txt
pip install -e .
pre-commit install
```

## 2BFAIR_backend implementation

To run 2BFAIR_backend implementation.

- Install the required libraries: `pip install -r tobefair_backend_requirements.txt`
- Using Visual Studio Code, configure the following debug option:

```json
"configurations": [
        {
            "name": "Python Debugger: FastAPI",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "tobefair_backend.service.main:app",
                "--reload"
            ],
            "jinja": true,
        },
```
