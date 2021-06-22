#!/usr/bin/env python
import os
import sys

from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists


if __name__ == "__main__":
    settings_module = env.str("SETTINGS_MODULE", "settings.local")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
