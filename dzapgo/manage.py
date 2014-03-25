#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dzapgo.settings.dev")

    # Add apps/ to the path
    PROJ_ROOT = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.join(PROJ_ROOT, 'apps'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
