# -*- coding: utf-8 -*-
#
# A framework of sentiment analysis applied on the tweets related to the 2014 FIFA World Cup.
# Copyright (C) 2014 Rubens Pessoa 
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SA_WorldCup.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
