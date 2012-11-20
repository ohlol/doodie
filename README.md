Doodie
======

An pagerduty dashboard.

Setup
=====

    $ pip install -r requirements.txt
    $ cat > local_settings.py <<EOF
    PAGERDUTY_APIKEY="<apikey here>"
    PAGERDUTY_SUBDOMAIN="<subdomain here>"
    EOF
    
    $ env FLASK_DEBUG=true ./manage.py runserver &
    $ open http://localhost:7777/incidents
