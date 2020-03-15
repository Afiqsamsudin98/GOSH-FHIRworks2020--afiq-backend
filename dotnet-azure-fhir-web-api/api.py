import flask
from flask import request, jsonify
from flask_cors import CORS
import matplotlib.pyplot as plt
from fhir_parser import FHIR
from fhir import getLanguageData,getMaritalStatus,getAge

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>hiya</h1>"
    
@app.route('/language-data', methods=['GET'])
def getlanguage():
    languages = getLanguageData()
    return jsonify(languages)

@app.route('/marital-status-data', methods=['GET'])
def getmaritalstatus():
    marital = getMaritalStatus()
    return jsonify(marital)

@app.route('/age-data', methods=['GET'])
def getage():
    ages = getAge()
    returndata = {}
    for age in ages:
        returndata.update({str(age*10 ) + " - " + str(age*10 +9): ages.get(age)})
    # print(returndata)
    return jsonify(returndata)

x = getAge()
app.run(port=7000)