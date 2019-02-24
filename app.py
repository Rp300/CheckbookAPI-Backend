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
app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def hello_world():
    print(request.args.get("code"))
    return 'Hello, World!'
