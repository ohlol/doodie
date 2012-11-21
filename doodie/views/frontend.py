from flask import Module, jsonify, render_template

from doodie import pagerduty_apikey, pagerduty_subdomain
from doodie.lib.pagerduty import Pagerduty

frontend = Module(__name__)

@frontend.route("/incidents")
def quick():
    return render_template("incidents.html")

@frontend.route("/incidents/count/", defaults={"status": "all"})
@frontend.route("/incidents/count/<string:status>")
def incidents_count(status):
    p = Pagerduty(pagerduty_apikey, pagerduty_subdomain)
    count = p.incident_count(status=status)

    if count:
          return jsonify(message=count)
    else:
          abort(500)
