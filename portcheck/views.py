from flask import Flask, jsonify, request, render_template
from portcheck import app, cache
from flask.ext.cors import cross_origin
import socket


@app.route('/')
def healthCheck():
    return render_template('index.html')

@app.route('/<host>/<port>')
@cross_origin()
def is_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3);
    result = sock.connect_ex((host,int(port)))
    msg = host + ":" + port

    msg += " is open" if result == 0 else " is closed"

    return jsonify(data=msg)

@app.errorhandler(404)
@cross_origin()
def not_found_exception(arg):
    app.logger.error(arg)
    return jsonify(error="Not found"), 404


@app.errorhandler(500)
@cross_origin()
def internal_server_error(arg):
    app.logger.error(arg)
    return jsonify(error="We had an internal server error."), 500
