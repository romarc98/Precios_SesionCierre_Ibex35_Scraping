import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def PreciosSesionIbex35_ScrappingData():
    # Defino la página de la que voy a obtener los datos:
    page = 'https://www.borsabcn.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'
    # Realizo la petición GET a dicha página:
    respuesta = requests.get(page)
    # Obtengo el status: p. ej: <Response [200]> conforme la petición se ha llevado con éxito:
    status_code = respuesta.status_code
    print('El código HTTP devueto por el servidor: {}'.format(respuesta))

    # WEB SCRAPING DATA ACQUISITION WITH SOUP:
    # Genero un Objeto de tipo Soup para analizar el contenido en bruto de la página:
    soup = BeautifulSoup(respuesta.content, 'html.parser')
    # Muestro el contenido total con prettify (comentado debido a su grandaria):
    #print(soup.prettify())

    # En este punto observo la página físicamente y con Firebug Lite.
    # Accedo a la tabla en cuestión por su id al observar con Firebug lite:
    tr = soup.find(attrs={'id':'ctl00_Contenido_tblAcciones'})
    # Genero un vector con las sub-etiquetas de la tabla:
    vector_tr = tr.contents
    # Recorrerá el vector anterior extrayendo la información de las sub-etiquetas sucesivas
    # hasta llegar a la información que me interesa para formar el .csv.

    # Creo un diccionario dict_data con:
    #       key = nombre columna
    #       value = List con los valores de la página
    # Dicho diccionario lo usará si necesito acceder facilmente a los datos.
    dict_data = {}
    # Defino un vector donde almacenará todas las "ROWS" de la tabla.
    # Cada ROW se corresponde con una empresa y su información.
    # De este modo irá escribiendo dinámicamente en el .csv
    csv_global = []

    # Inicio recorrido por la tabla:
    i = 1
    while i < (len(vector_tr) - 1):
        # Defino un vector con los sub-tags <tr> de table:
        vector_td = vector_tr[i].contents

        # La primera iteración la uso para determinar los HEADERS del .csv:
        if i == 1:
            # Itero sobre las etiquetas <th> de cada tag <tr>:
            a = 1
            while a < (len(vector_td) - 2):
                # AÃ±ado las Keys a dict_data en cada iteración:
                dict_data[vector_td[a].string] = []
                a = a + 1
        else:
            # Si ya no estoy en la primera iteración, solo me quedan datos:
            # Itero sobre las etiquetas <td> de cada tag <tr>:
            e = 1
            # Genero una lista donde almacenará cada ROW y posteriormente la añadire a csv_global:
            csv1 = []
            while e < (len(vector_td) - 1):
                # En función del valor de "e", dispondré de los diferentes atributos de cada empresa:
                if e == 1:
                    dict_data['Nombre'].append(vector_td[e].string)
                    csv1.append(vector_td[e].string)
                if e == 2:
                    dict_data['Últ.'].append(vector_td[e].string)
                    csv1.append(vector_td[e].string)
                if e == 3:
                    dict_data['% Dif.'].append(vector_td[e].string)
                    csv1.append(vector_td[e].string)
                if e == 4:
                    dict_data['Máx.'].append(vector_td[e].string)
                    csv1.append(vector_td[e].string)
                if e == 5:
                    dict_data['Mín.'].append(vector_td[e].string)
                    csv1.append(vector_td[e].string)
                if e == 6:
                    dict_data['Volumen'].append(vector_td[e].string)
                    csv1.append(vector_td[e].string)
                if e == 7:
                    dict_data['Efectivo (miles €)'].append(vector_td[e].string)
                    csv1.append(vector_td[e].string)
                if e == 8:
                    dict_data['Fecha'].append(vector_td[e].string)
                    csv1.append(vector_td[e].string)

                e = e + 1

            # Añado cada ROW entera (empresa y sus datos) a la lista csv_global:
            csv_global.append(csv1)

        i = i + 1

    # Proceso del nombre del csv. Obtengo un nombre para cada día de la semana
    # que quiera adquirir la situación del IBEX35. cada día viene identificado por
    # la fecha en cuestión:
    now = datetime.now().strftime('%d-%m-%y')
    nombre_csv = "output/" + "PreciosSesionEmpresasIbex35" + "_" + now + ".csv"
    print(nombre_csv)

    # Genero y escribo el CSV:
    with open(nombre_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        # Escribo el HEADER con las key del diccionario de datos:
        writer.writerow(dict_data.keys())
        # Escribo los datos de cada empresa con el vector csv:_global:
        writer.writerows(csv_global)

    # Por último, muestro la info ordenada almacenada en el dict_data:
    print(dict_data)
    print(csv_global)

    # Devuelvo el diccionario y el vector csv_global
    # para procesarlos:
    return dict_data, csv_global