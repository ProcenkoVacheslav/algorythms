import functools
import timeit

from typing import Callable, Optional

from custom_annotations import algorythm_types, algorythm_names
from loggers import algorythm_logger


def get_version_string(version: Optional[int]):
    version_string = ''
    if version:
        version_string = f'-{version}'

    return version_string


def time_decorator(algorythm_type: algorythm_types, algorythm_name: algorythm_names, version: Optional[int] = None):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            algorythm_time = timeit.timeit(lambda: func(*args, **kwargs), number=1)

            result = func(*args, **kwargs)

            version_string = get_version_string(version)

            algorythm_logger.debug(
                f'Execution {algorythm_type}-{algorythm_name}{version_string} with arguments'
                f'{args, kwargs} took {algorythm_time}s'
            )

            return result
        return wrapper
    return decorator
