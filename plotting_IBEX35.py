import csv
import os
import matplotlib.pyplot as plt

# Le pido al usuaruio una empresa del IBEX 35 por pantalla:
empresa_escogida_usr = input("Escoge una para consultar los precios de la sesión a lo largo de un periodo (en MAYÚSCULAS):")
print(empresa_escogida_usr)

# COMPUTO EL GRÁFICO:
# Eje Y:
# Defino los vectores que voy a llenar  a representar:
valores_actuales_cierre = []
valores_minimos_cierre = []
valores_maximos_cierre = []
# Eje X:
vector_fechas = []

with os.scandir('output/') as dir:
    # Leeré cada uno de los csv en busca de la info que busco:
    for entry in dir:
        # identifico cada csv;
        # print(entry.name)
        # De cada nombre del csv, me quedo con la fecha y la almaceno en un vector:
        vector_nombre = entry.name.split(sep='_')
        fecha = vector_nombre[1]
        fecha_limpia= fecha.strip('.csv')
        # Añado el valor procesado de cada .csv al vector de fechas:
        vector_fechas.append(fecha_limpia)


        with open(entry, newline='') as File:
            reader = csv.reader(File)
            # Imprimo todas las filas (una por empresa)
            for row in reader:
                # Busco la empresa que el usr me ha pedido:
                if row[0] == empresa_escogida_usr:
                    # Proceso las comas y las transformaciones de formato:
                    if "," in row[1]:
                        row[1]= row[1].replace(",", ".")
                        #print(row[1])
                    if "," in row[3]:
                        row[3]= row[3].replace(",", ".")
                        #print(row[3])
                    if "," in row[4]:
                        row[4]= row[4].replace(",", ".")
                        #print(row[4])

                    # Añado a los vectores lso valores de cada día:
                    valores_actuales_cierre.append(float(row[1]))
                    valores_minimos_cierre.append(float(row[4]))
                    valores_maximos_cierre.append(float(row[3]))


                    print(row)

print("Valores actuales cierre: {}".format(valores_actuales_cierre))
print("Valores mínimos cierre: {}".format(valores_minimos_cierre))
print("Valores máximos cierre: {}".format(valores_maximos_cierre))
print("Fechas del vector de Fechas: {}".format(vector_fechas))


# Genero el plot:
plt.figure(figsize=(10,5))

# Ajusto la escala del eje y con los mínimos y máximos de la empresa:
max = max(valores_maximos_cierre)
min = min(valores_minimos_cierre)
max_fig = max + 5
min_fig = min - 5
plt.ylim(min_fig, max_fig)

# Muestro los 3 puntos de cada fec ha que me interesan:
plt.plot(vector_fechas, valores_maximos_cierre, '^', 'g')
plt.plot(vector_fechas, valores_minimos_cierre, 'v', 'r')
plt.plot(vector_fechas, valores_actuales_cierre, 'o-', 'm')

# Añado info adicional al plot:
plt.legend(('Máximo', 'Valor de Cierre', 'Mínimo'),
prop = {'size': 10}, loc='upper right')
plt.xlabel('Escala temporal de Días')
plt.ylabel('Valores de cierre')
plt.title('Análisis del mínimo, máximo y cierre de la empresa seleccionada en un periodo')
plt.minorticks_on()
plt.xticks(vector_fechas, size = 'small', color = 'b', rotation = 45)  # Colocamos las etiquetas, meses, en las posiciones, dias, con color azul y rotadas 45º

plt.show()