# coding:utf8
#
from app.app import create_app
import sys

print('==sys.version==',sys.version)
print('==sys.executable==',sys.executable)

application_mysite = create_app()

@application_mysite.template_filter('timeformat')
def timeformat(timestamp):
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
