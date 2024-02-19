from flask import Flask, request
from flask_restful import Api, Resource
from flask_lt import run_with_lt




import requests
from bs4 import BeautifulSoup
def get_dict_data(data):
    scraped_data=[]
    for i in data:
         key_id=i['data-id']
         value=i['value']
         scraped_data.append({key_id:value})

    return scraped_data
     
def scrape_currency_data(url="https://dollaregypt.com",options="currency"):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the relevant data on the webpage
        title = soup.find('select', id=options)
        # gold = soup.find('select', id='gold-karat')
       
        options = title.find_all('option')
        # gold_data=get_dict_data(gold)
        data=get_dict_data(options)
         
        return data
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return None

app = Flask(__name__)
api = Api(app)
# run_with_lt(app)


class ClassificationAPI(Resource):
        def get(self):
            data=scrape_currency_data()
            gold_data=scrape_currency_data('https://www.dollaregypt.com/gold-price/',"gold-karat")
            print(data)
            return {'data':data,'gold_data':gold_data,'status':200,'message':'success',}


api.add_resource(ClassificationAPI, "/get_coins_price", methods=["GET"])

if __name__ == "__main__":
    # url = ngrok.connect(80,authtoken='usr_2Zm4w3LCulMqOUKcz120t3N9peK', region='us').public_url
    # print(" ***** Tunnel URL:", url)
    app.run(debug=False, host="0.0.0.0", port=5400)
