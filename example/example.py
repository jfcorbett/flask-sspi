#!/usr/bin/env python

import sys
sys.path.append("../")

from flask import Flask
from flask import render_template
from flask_sspi import init_sspi
from flask_sspi import requires_authentication

DEBUG=True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
@requires_authentication
def index(user):
    print("index")
    return render_template('index.html', user=user)


if __name__ == '__main__':
    init_sspi(app)
    app.run(host='0.0.0.0')
