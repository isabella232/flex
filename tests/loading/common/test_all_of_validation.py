import pytest

from flex.error_messages import MESSAGES
from flex.exceptions import ValidationError
from flex.loading.definitions.schema import schema_validator

from tests.utils import (
    assert_path_not_in_errors,
    assert_message_in_errors,
)


def test_all_of_is_not_required():
    try:
        schema_validator({})
    except ValidationError as err:
        errors = err.detail
    else:
        errors = {}

    assert_path_not_in_errors('allOf', errors)


@pytest.mark.parametrize(
    'value',
    ({'a': 'abc'}, 1, 1.1, True, None, [1, 2]),
)
def test_all_of_with_invalid_types(value):
    schema = {'allOf': value}

    with pytest.raises(ValidationError) as err:
        schema_validator(schema)

    assert_message_in_errors(
        MESSAGES['type']['invalid'],
        err.value.detail,
        'all_of.type',
    )


def test_all_of_with_empty_array_is_invalid():
    with pytest.raises(ValidationError) as err:
        schema_validator({'allOf': []})

    assert_message_in_errors(
        MESSAGES['min_items']['invalid'],
        err.value.detail,
        'allOf.minItems',
    )


def test_valid_all_of():
    schema = {'allOf': [{}]}

    try:
        schema_validator(schema)
    except ValidationError as err:
        errors = err.detail
    else:
        errors = {}

    assert_path_not_in_errors(
        'allOf',
        errors,
    )


def test_all_of_with_reference():
    pass
