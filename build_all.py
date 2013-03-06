#!/usr/bin/python
from tools.build import build_component

COMPONENTS = [
    'boost',
    'gmp',
    'mpfr',
    'cgal',
]

for component in COMPONENTS:
    build_component(component)