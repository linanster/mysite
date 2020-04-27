# coding:utf8
#
from flask_script import Manager
from app.app import create_app

app = create_app()

manager = Manager(app)

@manager.command
def hello():
    print('Hello, Manager Command!')

if __name__ == '__main__':
    manager.run()
