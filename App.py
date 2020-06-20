from Scraper import Scraper
from writerExcel import EscribeExcel
import json


# inicia todo el programa
def inicio_programa(numero_departamento):
    scraper = Scraper()
    escribir = EscribeExcel()
    departamentos = get_departamentos()
    municipios_array = departamentos['departamentos'][numero_departamento]
    for municipio in municipios_array['municipios']:
        nombre_departamento = municipios_array['nombre']
        find_lugar = "{0}, {1}".format(municipio, nombre_departamento)
        dt = scraper.find_place(find_lugar)
        # prepara los datos para ser enviados al servidor
        print(dt)
        try:
            da = {
                "center": {
                    "lat": dt['candidates'][0]['geometry']['location']['lat'],
                    "lag": dt['candidates'][0]['geometry']['location']['lng']
                },
                "zoom": 15,
                "country_code": "sv",
                "east": dt['candidates'][0]['geometry']['viewport']['northeast']['lng'],
                "north": dt['candidates'][0]['geometry']['viewport']['northeast']['lat'],
                "south": dt['candidates'][0]['geometry']['viewport']['southwest']['lat'],
                "west": dt['candidates'][0]['geometry']['viewport']['southwest']['lng']
            }
            # eviar las coordenadas al server de tiendacerca y obtine los la lista de todas las tienda de un municipio
            datos_tiendas = scraper.get_data_stores(coordenadas=da)
            # se encarga de escribir todas las tiendas que encuentre para un municipio
            escribir.write_data_into_file(nombre_departamento=municipios_array['nombre'], nombre_municipio=municipio,
                                          datos_tiendas=datos_tiendas)
        except IndexError:
            print('index fuera de rango')
            pass

        pass
    pass


def get_departamentos():
    with open('Departamentos.json', 'r', encoding='utf8') as j:
        data = json.load(j)
        return data
        pass
    pass


if __name__ == "__main__":
    # scraper = Scraper()
    # escribir = EscribeExcel()
    depatamentos = get_departamentos()
    numero_departamento = 0
    inicio_programa(numero_departamento)
    pass
