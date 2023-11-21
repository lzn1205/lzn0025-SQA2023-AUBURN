import os
import scanner
from hypothesis import given, strategies as st

# Methods to be fuzzed
methods_to_fuzz = [
    scanner.isValidUserName,
    scanner.isValidPasswordName,
    scanner.isValidKey,
    scanner.checkIfValidSecret,
    scanner.checkIfValidKeyValue
]

# Define strategies for generating test data
username_strategy = st.text()
password_strategy = st.text()
key_strategy = st.text()
config_value_strategy = st.text()

# Property-based testing for each method
@given(username=username_strategy)
def test_isValidUserName(username):
    return scanner.isValidUserName(username)

@given(password=password_strategy)
def test_isValidPasswordName(password):
    return scanner.isValidPasswordName(password)

@given(key=key_strategy)
def test_isValidKey(key):
    return scanner.isValidKey(key)

@given(config_value=config_value_strategy)
def test_checkIfValidSecret(config_value):
    return scanner.checkIfValidSecret(config_value)

@given(config_value=config_value_strategy)
def test_checkIfValidKeyValue(config_value):
    return scanner.checkIfValidKeyValue(config_value)


def main():
    with open('fuzz_output.txt', 'w') as file:
        for test_function in [
            test_isValidUserName,
            test_isValidPasswordName,
            test_isValidKey,
            test_checkIfValidSecret,
            test_checkIfValidKeyValue
        ]:
            try:
                result = test_function()
                file.write(f"Testing {test_function.__name__} - Result: {result}\n")
            except Exception as e:
                file.write(f"Testing {test_function.__name__} - Exception: {str(e)}\n")

if __name__ == "__main__":
    main()
