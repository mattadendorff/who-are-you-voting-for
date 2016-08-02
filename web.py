import json
import a2c
from flask import Flask
from flask import Response
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello"

@app.route("/")
def get_candidates():
    address = request.args.get("address")
    variables = {}
    if address:
        ward = a2c.address_to_ward(address)
        variables.update(ward)
        candidates = a2c.get_candidates(ward["ward"])
        variables["candidates"] = candidates

    return render_template('index.html', **variables)

if __name__ == "__main__":
    app.run(debug=True)
        
