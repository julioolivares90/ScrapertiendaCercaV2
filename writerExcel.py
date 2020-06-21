import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import openpyxl
from os import path
from openpyxl import load_workbook

NAME_FILE_EXCEL = 'DatosDeTiendaCerca.xlsx'


class EscribeExcel(object):
    def write_data_into_file(self, nombre_departamento, nombre_municipio, datos_tiendas):
        nombres_depatamentos = []
        nombres_municipios = []
        lista_id = []
        titulos = []
        direcciones = []
        telefonos = []
        codigos_pais = []
        codigos = []
        lista_latitudes = []
        lista_longitudes = []

        write = ExcelWriter(NAME_FILE_EXCEL, engine='openpyxl')
        for key, dt in datos_tiendas.items():
            nombres_depatamentos.append(nombre_departamento)
            nombres_municipios.append(nombre_municipio)
            lista_id.append(key)
            titulos.append(dt['title'])
            direcciones.append(dt['address'])
            telefonos.append(dt['phone'])
            codigos_pais.append(dt['country_code'])
            codigos.append(dt['code'])
            lista_latitudes.append(dt['lat'])
            lista_longitudes.append(dt['lng'])
            pass
        book = load_workbook(NAME_FILE_EXCEL)
        write.book = book
        df = pd.DataFrame({'departamento': nombres_depatamentos,
                           'municipios': nombres_municipios, 'id': lista_id, 'titulos': titulos, 'direccion': direcciones, 'telenofo': telefonos, 'country_code': codigos_pais, 'code': codigos, 'lat': lista_latitudes, 'lng': lista_longitudes})
        df.to_excel(write, nombre_municipio, index=False)
        write.save()
        print('tarea completada')
        pass
    pass
