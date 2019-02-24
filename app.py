# import requests
# url = "https://demo.checkbook.io/v3/check"
# headers = {
#   'Accept': 'application/json',
#   'Authorization': 'd6aa2703655f4ba2af2a56202961ca86:dXbCgzYBMibj8ZwuQMd2NXr6rtvjZ8'
# }
#
# response = requests.request("GET", url, headers=headers)
# print(response.text)

from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def hello_world():
    print(request.args.get("code"))
    params = {"client_id":"5633b82026504602837d70cf0a84323a",
        "grant_type": "authorization_code",
        "scope": "check",
        "code":request.args.get("code"),
        "redirect_uri": "https://checkbook-facebookbot.herokuapp.com/redirect",
        "client_secret": "9dee4ce1dce741d797450b2e0e1ab837"}
    response = requests.post("https://checkbook.io/oauth/token", params)
    print(response)
    return 'Hello, World!'
