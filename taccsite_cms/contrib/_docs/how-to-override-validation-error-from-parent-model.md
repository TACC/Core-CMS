# How To Override `ValidationError()` from Parent Model

Intercept Error(s):

```python
from django.core.exceptions import ValidationError

from djangocms_Xxx.models import AbstractXxx

from taccsite_cms.contrib.helpers import (
    get_indices_that_start_with
)

class OurModelThatUsesXxx(AbstractXxx):
    # Validate
    def clean(self):
        # Bypass irrelevant parent validation
        try:
            super().clean()
        except ValidationError as err:
            # Intercept single-field errors
            if hasattr(err, 'error_list'):
                for i in range(len(err.error_list)):
                  # SEE: "Find Error(s)"
                  # ...
                    # Skip error
                    del err.error_list[i]
                    # Replace error
                    # SEE: https://docs.djangoproject.com/en/2.2/ref/forms/validation/#raising-validationerror

            # Intercept multi-field errors
            if hasattr(err, 'error_dict'):
                for field, errors in err.message_dict.items():
                    # SEE: "Find Error(s)"
                    # ...
                        # Skip error
                        del err.error_dict[field]
                        # Replace error
                        # SEE: https://docs.djangoproject.com/en/2.2/ref/forms/validation/#raising-validationerror

            # NOTE: The conditional `pass` is only to skip multi-field errors;
            #       single-field error skipping is unaffected by this logic;
            #       so it seems safe to always include this logic block
            if len(err.messages) == 0:
                pass
            else:
                raise err
```

Handle Error(s):

```python
# SEE: "Find Error(s)"
# ...

                    # Catch known static error
                    if 'Known static error string' in error:
                        # ...

                    # Catch known dynamic error
                    indices_to_catch = get_indices_that_start_with(
                        'Known dynamic error string that starts with same text',
                        errors
                    )
                    for i in indices_to_catch:
                        # ...
```
