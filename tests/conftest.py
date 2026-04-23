import pytest
import csv

@pytest.fixture(scope="session")
def path_to_file():
    return "src/data/data.csv"

@pytest.fixture(scope="session")
def read_csv(path_to_file):
    data = []
    with open(path_to_file, newline='') as file:
        reader = csv.DictReader(file)
        data.extend(reader)
    return data

@pytest.fixture(scope="session")
def validate_schema():
    def _validate(actual_schema, expected_schema):
        assert actual_schema == expected_schema, \
            f"Schema mismatch! Expected {expected_schema}, got {actual_schema}"
    return _validate

def pytest_collection_modifyitems(config, items):
    for item in items:
        custom_marks = [m for m in item.iter_markers() if m.name != "parametrize"]
        if not custom_marks:
            item.add_marker(pytest.mark.unmarked)