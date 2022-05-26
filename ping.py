import requests

def check_server_status(url):
    request_response = requests.head(url)
    a = request_response.status_code
    if a == 200:
        return True
    else:
        return False
