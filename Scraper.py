import requests
import json

import googlemaps
"""
variables
"""
END_POINT = 'https://1fzqk3npw4.execute-api.us-east-1.amazonaws.com/nearby_store_stage/sv'  # endpoint  de la api de tiendacerca.com funciona con metodo post
# api de google maps para places
API_KEY = 'AIzaSyCswu8im_YgIcNBGFmRr-gRVBLqBHwXVxk'
NEW_API_KEY = 'AIzaSyA372lgSayQt_UW6EIb4IAjEABGg2elWrg'
#URL_GOOGLE_MAPS_GEOCODING ="https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={0}&inputtype=textquery&fields=formatted_address,name,geometry&key={1}"
END_POINT2 = 'https://tienda-cerca-api.herokuapp.com/api/find-lugar?lugar='


class Scraper(object):
    # busca un lugar y retorna un objeto json con la informacion de ese lugar
    def find_place(self, lugar):
        resultado_busqueda = requests.get(
            "https://tienda-cerca-api.herokuapp.com/api/find-lugar?lugar={0}".format(
                lugar))
        print(resultado_busqueda)
        return json.loads(resultado_busqueda.content)
        pass

    def get_data_stores(self, coordenadas):
        # convierte las coordenadas en un json
        js = json.dumps(coordenadas)
        response = requests.post(END_POINT, js)
        data_stores = json.loads(response.content)
        return data_stores
        pass

    pass


