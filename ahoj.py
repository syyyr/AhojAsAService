#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return render_template("home.html")

@app.route("/version", methods=["GET"])
def version():
    if request.headers["Accept"] == "application/json":
        return jsonify({"version": {"major": 0, "minor": 0, "patch": 1}})
    elif request.headers["Accept"] == "text/plain":
        return "0.0.1"
    else:
        return render_template("version.html", ver="0.0.1")

@app.route("/ahoj")
@app.route("/ahoj/<komu>")
@app.route("/ahoj/<komu>/<od>", methods=["GET"])
def AHOJ(komu=None, od=None):
    str = "AHOJ"

    if komu is not None:
        str += ", {0}".format(komu.upper())

    if request.headers["Accept"] == "application/json":
        if komu is not None and od is not None:
            return jsonify({"message": str, "from": od.upper()})
        else:
            return jsonify({"message": str})

    elif request.headers["Accept"] == "text/plain":
        if komu is not None and od is not None:
            str += ", {0} –{1}".format(komu.upper(), od.upper())
        return str

    else: # default to html
        return render_template("page.html", od=od, komu=komu)

if __name__ == "__main__":
    app.run(debug=True)

