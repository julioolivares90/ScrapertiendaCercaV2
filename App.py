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
            da2 = {
                "center": {
                    "lat": dt['geometry']['location']['lat'],
                    "lng": dt['geometry']['location']['lng']
                },
                "zoom": 18,
                "country_code": "sv",
                "east": dt['geometry']['viewport']['northeast']['lng'],
                "north": dt['geometry']['viewport']['northeast']['lat'],
                "south": dt['geometry']['viewport']['southwest']['lat'],
                "west": dt['geometry']['viewport']['southwest']['lng']
            }
            datos_tienda = scraper.get_data_stores(coordenadas=da2)
            # se encarga de escribir todas las tiendas que encuentre para un municipio
            escribir.write_data_into_file(nombre_departamento=municipios_array['nombre'], nombre_municipio=municipio,
                                          datos_tiendas=datos_tienda)
        except IndexError:
            print("ocurrio un error")
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
