# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     run_gunicore
   Description :
   Author :       conner
   date：          2018-4-19
-------------------------------------------------
   Change Activity:
                   2018-4-19:
-------------------------------------------------
"""
__author__ = 'conner'

#-*- coding: utf-8 -*-
import re
import sys
from gunicorn.app.wsgiapp import run
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script/.pyw|/.exe)?$', '', sys.argv[0])
    sys.exit(run())