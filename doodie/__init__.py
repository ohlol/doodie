import os

from flask import Flask

app = Flask(__name__)
app.config.from_pyfile(os.environ.get("DOODIE_SETTINGS",
                                      os.path.join(os.path.dirname(__file__),
                                                   "..", "settings.py")))
app.debug = os.environ.get("FLASK_DEBUG", app.config.get("DEBUG"))
pagerduty_apikey = app.config.get("PAGERDUTY_APIKEY",
                                  os.environ.get("PAGERDUTY_APIKEY"))
pagerduty_subdomain = app.config.get("PAGERDUTY_SUBDOMAIN",
                                     os.environ.get("PAGERDUTY_SUBDOMAIN"))

from doodie.views.frontend import frontend
app.register_module(frontend)
