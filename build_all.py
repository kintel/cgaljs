#!/usr/bin/python
from tools.build import build_component

INCLUDES_DIR = 'includes'
LIBS_DIR = 'libs'

COMPONENTS = [
    #'boost',
    #'gmp',
    #'mpfr',
    'cgal',
]

for component in COMPONENTS:
    build_component(component, INCLUDES_DIR, LIBS_DIR)


