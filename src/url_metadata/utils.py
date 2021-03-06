import warnings
from urllib.parse import unquote
from pathlib import Path
from typing import Union, Iterator, Dict, Any

import backoff  # type: ignore[import]


def normalize_path(p: Union[str, Path]) -> Path:
    if isinstance(p, Path):
        return p
    elif isinstance(p, str):
        return Path(p).expanduser().absolute()
    else:
        raise TypeError("Expected 'str' or 'pathlib.Path', received {}".format(type(p)))


def fibo_backoff() -> Iterator[int]:
    """
    Fibonacci backoff, with the first 6 elements consumed.
    In other words, this starts at 13, 21, ....
    """
    fib = backoff.fibo()
    for _ in range(6):
        next(fib)
    yield from fib


def backoff_warn(details: Dict[str, Any]) -> None:
    warning_msg: str = "Backing off {wait:0.1f} seconds afters {tries} tries with {args} {kwargs}".format(
        **details
    )
    warnings.warn(warning_msg)


def clean_url(url: str) -> str:
    """
    unquotes and removes whitespace from URLs
    https://docs.python.org/3/library/urllib.parse.html#urllib.parse.unquote
    """
    return unquote(url).strip()
