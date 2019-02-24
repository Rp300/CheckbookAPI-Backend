import webbrowser
import requests
redirect_uri=""
client_id ="5633b82026504602837d70cf0a84323a"
data = {
    'client_id':client_id,
    'response_type': "code",
    'scope': "check",
    'redirect_uri':redirect_uri
}
url = "https://checkbook.io/oauth/authorize?client_id=5633b82026504602837d70cf0a84323a&response_type=code&scope=check&redirect_uri=http://0.0.0.0:8000/"
webbrowser.open(url)
