# import requests
# url = "https://demo.checkbook.io/v3/check"
# headers = {
#   'Accept': 'application/json',
#   'Authorization': 'd6aa2703655f4ba2af2a56202961ca86:dXbCgzYBMibj8ZwuQMd2NXr6rtvjZ8'
# }
#
# response = requests.request("GET", url, headers=headers)
# print(response.text)

from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def hello_world():
    print(request.args.get("code"))
    params = {"client_id":"5633b82026504602837d70cf0a84323a",
        "grant_type": "authorization_code",
        "scope": "check",
        "code":request.args.get("code"),
        "redirect_uri": "https://checkbook-messenger-bot.herokuapp.com/redirect",
        "client_secret": "nWiQFp9iCGciZ8X1d62PTgNrosyXe3"}
    response = requests.post("https://sandbox.checkbook.io/oauth/token", params)
    print(response.json());
    return jsonify(response["access_token"])
