"""
To Install:
conda install -c conda-forge black

To Run as an application:
black black_test.py or directory

or as a package

python -m black black_test.py

can automate this when commiting to the repo, by using a hook in your repo:
    add commands to file named .pre-commit-config.yaml
    then pre-commit install 

or can add to github actions when running a push request (PR)
    add file named .github/workflows/black.yml with commands

"""

import black
def my_function():
    print("testing black\n")

def my_function_2(fun_input, fun_output, param_1, param_2,
                  parameters=5, logging=False):
    print(f"input: {input}")

my_list = [1,
           2,
           3,
           4,
           5]

my_dictionary = {
    "name": "my_name", "address": "123 Main St",
    "phone": 1234567, "age": 30
}