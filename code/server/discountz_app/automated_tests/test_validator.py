import pytest
from django.core.exceptions import ValidationError
from validator import validate_edu_email, validate_only_letters

# Tests for validate_edu_email
def test_validate_edu_email_success():
    assert validate_edu_email("test@uni.edu") is None

def test_validate_edu_email_fail():
    with pytest.raises(ValidationError) as excinfo:
        validate_edu_email("test@gmail.com")
    assert str(excinfo.value) == "['Email address must end in .edu']"

# Tests for validate_only_letters
def test_validate_only_letters_success():
    assert validate_only_letters("lettersOnly") is None

def test_validate_only_letters_fail():
    with pytest.raises(ValidationError) as excinfo:
        validate_only_letters("letters and 123")
    assert str(excinfo.value) == "['String must contain only letters']"
