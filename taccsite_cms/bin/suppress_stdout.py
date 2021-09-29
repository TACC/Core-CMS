#!/usr/bin/env python

# Allow a script to temporarily hide `print` output
# SEE: https://gist.github.com/djsmith42/3956189#file-gistfile1-py
# SEE: https://thesmithfam.org/blog/2012/10/25/temporarily-suppress-console-output-in-python/

from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
