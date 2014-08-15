import os
from flask.ext.script import Manager
from portcheck import app

manager = Manager(app)

@manager.command
def run():
  app.run(host='0.0.0.0', debug=app.config["DEBUG"], port=int(os.environ.get('PORT', 5000)))

if __name__ == '__main__':
    manager.run()