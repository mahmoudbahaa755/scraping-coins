from flask import Flask, request
from flask_restful import Api, Resource
from flask_lt import run_with_lt




import requests
from bs4 import BeautifulSoup
data=[]
import random

def modify_data(data):
    for item in data:
        small_amount = random.uniform(-0.1, 0.1)
        item['value'] = str(float(item['value']) + small_amount)
    return data

def scrape_currency_data(url="https://dollaregypt.com"):
    response = requests.get(url)
    print('data before',data)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find('select', id='currency')
        options = title.find_all('option')
        data = []
        for option in options:
            currency_code = option['data-id']
            value = option['value']
            data.append({'data-id': currency_code, 'value': value})
        return data
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return None

app = Flask(__name__)
api = Api(app)


class GetEgyptBlackMarket(Resource):
        def get(self):
            data=scrape_currency_data()
            print(data)
            return {'data':data}


api.add_resource(GetEgyptBlackMarket, "/get_coins_price", methods=["GET"])

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5400)
