import requests

client_id = '43e63a41d246d6b8028b'
client_secret = 'f95bcdbdc757ca39b0802f0545e9bf58'

def get_token():
    url = 'https://api.artsy.net/api/tokens/xapp_token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(url, data=data)
    return response.json()['token']

def get_genes(token):
    url = 'https://api.artsy.net/api/genes/'
    headers = {
        'X-Xapp-Token': token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error' + str(response.status_code)

def get_impressionistic_paintings(token):
    url = 'https://api.artsy.net/api/search?q=impressionism+more:pagemap:metatags-og_type:artwork'
    headers = {
        'X-Xapp-Token': token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error' + str(response.status_code)

token = get_token()
genes = get_impressionistic_paintings(token)
print(genes)
