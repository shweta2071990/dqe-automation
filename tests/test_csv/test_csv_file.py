import pytest
import re

def test_file_not_empty(read_csv):
    assert len(read_csv) > 0, "CSV file is empty!"

@pytest.mark.validate_csv
def test_schema(read_csv, validate_schema):
    actual = list(read_csv[0].keys())
    expected = ["id", "name", "age", "email", "is_active"]
    validate_schema(actual, expected)

@pytest.mark.validate_csv
@pytest.mark.skip(reason="Skipping as per requirement")
def test_age(read_csv):
    for row in read_csv:
        age = int(row["age"])
        assert 0 <= age <= 100, f"Invalid age {age}"

@pytest.mark.validate_csv
def test_email(read_csv):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    for row in read_csv:
        assert re.match(pattern, row["email"]), \
            f"Invalid email {row['email']}"

@pytest.mark.validate_csv
@pytest.mark.xfail(reason="Known issue: duplicates present")
def test_duplicates(read_csv):
    rows = [tuple(sorted(row.items())) for row in read_csv]
    assert len(rows) == len(set(rows)), "Duplicates found"

@pytest.mark.parametrize(
    "id_val, expected",
    [("1", "False"), ("2", "True")]
)
def test_is_active_param(read_csv, id_val, expected):
    for row in read_csv:
        if row["id"] == id_val:
            assert row["is_active"] == expected

def test_is_active_id_2(read_csv):
    for row in read_csv:
        if row["id"] == "2":
            assert row["is_active"] == "True"