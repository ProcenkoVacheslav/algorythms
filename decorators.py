import functools
import timeit

from typing import Callable

from custom_annotations import algorythm_types, algorythm_names
from loggers import algorythm_logger


def time_decorator(algorythm_type: algorythm_types, algorythm_name: algorythm_names):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            algorythm_time = timeit.timeit(lambda: func(*args, **kwargs), number=1)

            result = func(*args, **kwargs)

            algorythm_logger.debug(f'Execution {algorythm_type}-{algorythm_name} took {algorythm_time}s ')

            return result
        return wrapper
    return decorator
