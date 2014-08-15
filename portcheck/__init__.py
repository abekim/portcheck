from flask import Flask
from flask.ext.cache import Cache
from portcheck.config import configure

app = Flask(__name__)
configure(app)

if not app.debug:
    import logging
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.DEBUG)

cache = Cache(app)

from portcheck import views