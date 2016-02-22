from flex.constants import (
    ARRAY,
    OBJECT
)
from flex.validation.common import (
    generate_object_validator,
)
from flex.validation.schema import (
    construct_schema_validators,
)


all_of_schema = {
    'type': ARRAY,
    'minItems': 1,
    'items': {
        'type': OBJECT,
    },
}
all_of_validators = construct_schema_validators(all_of_schema, {})

all_of_validator = generate_object_validator(
    field_validators=all_of_validators,
)
