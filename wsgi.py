# coding:utf8
#
from app.app import create_app
import sys

print('==sys.version==',sys.version)
print('==sys.executable==',sys.executable)

application_mysite = create_app()
