import webbrowser
import requests
redirect_uri="https://checkbook-facebookbot.herokuapp.com/redirect"
client_id ="5633b82026504602837d70cf0a84323a"
data = {
    'client_id':client_id,
    'response_type': "code",
    'scope': "check",
    'redirect_uri':redirect_uri
}
url = "https://sandbox.checkbook.io/oauth/authorize"
r = requests.post(url=url, data = data)
print(r.text)
print(r.url)
