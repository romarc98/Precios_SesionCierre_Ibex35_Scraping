AUTOR; MARC ROMÁN PORRAS

PROYECTO; LECTURA DE LOS PRECIOS DE LA SESIÓN EN CIERRE DE LAS EMPRESAS DEL IBEX 35

PRESENTACIÓN DEL PROYECTO:
El objetivo de este trabajo es mostrar la evolución de los precios de cierre de las acciones de una empresa
(la que el usuario elija) del IBEX 35 (valores Últ./Máx./Mín. de dichas acciones) a lo largo de un periodo
determinado mediante el scrapping de la web:

                    https://www.borsabcn.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000

El resultado de web scrapping se corresponde con un fichero .csv para cada día de la semana en el momento de cierre
diario de la bolsa y la representación de la evolución de los valores anteriores para cada empresa a lo largo del
periodo semanal. Para más información, consultar el pdf adjunto de dicho proyecto.


EJECUCIONES/OBTENCIÓN DE RESULTADOS:

Al ejecutar main_Ibex35.py se obtiene el conjunto de datos relativo a la situación actual de los precios de la Sesión
de la Bolsa de valores. Si lo ejecutamos cada día cuando la Bolsa cierra, como se ha procedido, obtenemos los datos
de cierre diarios.

Al ejecutar plotting_IBEX35.py se obtiene el contenido gráfico relativo al precio de las acciones de una empresa
del IBEX en cuestión (QUE SERÁ DEMANDADA Y QUE EL USUARIO DEBERÁ ESCOGER E INTRODUCIR POR CONSOLA).


REQUIREMENTS.TXT
Para la ejecución del proyecto y universalmente tal y como se define los paquetes necesarios de los que se debe disponer
para la correcta ejecución del proyecto, se dispone de un archivo requirements.txt. En dicho archivo se encuentran
los paquetes/librerías de los que se debe disponer correc tamente instalados en el momento de la ejecución del proyecto.

Se pueden instalar directamente desde consola:

        $pip install requests
        $pip install beautifulsoup4
        $pip install matplotlib

o desde el IDE (PYCHARM por ejemplo) File-Settings-Project_Python Interpreter


EJECUCIÓN/OBTENCIÓN DE RESULTADOS DESDE GITHUB MEDIANTE ZIPFILE DEL PROYECTO:


Para leer acerca de la ejecución/instalación que se debe llevar a cabo para la ejecución del proyecto, ver:

1: Inicialmente, llevamos a cabo una descarga del material desde Github obteniendo una carpeta en zip.
2: Posteriormente, una vez tengamos nuestra carpeta descargada en el pc, abrimos desde pycharm_community
(como IDE) dicha carpeta desde: File-Open... (seleccionando la carpeta global llamada "PEC_WebScraping".
En el interior de dicha carpeta se encuentran (output, main, scr, venv, etc...) y pycharm la establece como CWD.
3: En este punto, la estructura del proyecto yacerá sobre la parte izquierda de Pycharm, según la estructura
que se ha definido en su creación. En nuestro caso, deberemos disponer de lo siguiente:

        Precios_sesion_Ibex35
            output
                PreciosSesionEmpresasIbex35_01/mm/yy.csv
                PreciosSesionEmpresasIbex35_02/mm/yy.csv
                PreciosSesionEmpresasIbex35_03/mm/yy.csv
                (...)
            src
                __init__.py
                ibex_scrapping.py
            venv (library root)
            main_ibex35.py
            plotting_IBEX35.py
            README.txt
            requirements.txt
            License.txt
            respuestas.pdf (documento donde se adjuntan las respuestas de la actividad)


EJECUCIÓN main_Ibex35.py | SCREPPING DE LA WEB:

4: En este punto, SI NO DISPONEMOS DE CONFIGURACIÓN DE EJECUCIÓN, podemos establecer una yendo a Add configuration
(en la parte superior derecha) para establecer una configuración de ejecución. En este punto, dotamos de una
configuración de ejecicución de main_Ibex35.py, que obtiene cada vez que ejecutamos dicho main un fichero .csv que
almacena en output fruto del scrapping de los precios de la Sesión de la Bolsa de Valores para un día determinado
en su momento de cierre. Al clicar Add configuration, deberemos añadir la conf. clicando encima del botón " + "
y seleccionando Python de la lista que nos aparecerá a la izquierda.
5: En este punto, se nos abre una pestaña. En ella únicamente introduciremos como script path a main_Ibex35.py y nos
fijamos que el intérprete se sitúa en python3.8 (PEC_WebScraping) - PEC_WebScraping/venv/bin/python de acorde al virtual
env del que dispone nuestro proyecto. El intérprete deberá ser siempre este por lo que deberemos activar el venv si
este no estñá en funcionamiento.

La configuración del main ya está seleccionada y podemos ejecutar el proyecto obteniendo los diferentes .csv de los
precios de cierre a lo largo de un periodo de tiempo que posteriormente analizaremos gráficamente.

Si ya disponemos de una configuración de ejecucióon TAMBIÉN PODEMOS DIRECTAMENTE SITUARNOS ENCIMA DE main_Ibex35.py Y
MEDIANTE CLIC CON EL BOTÓN DERECHO, SELECCIONAR LA OPCIÓN Run'main'. DE ESTE MODO, SE EJECUTA EL main_Ibex35.py
PROPORCIONÁNDONOS EL .CSV EN OUTPUT Y ADEMÁS, SE AÑADE DICHA EJECUCIÓN COMO CONFIGURACIÓN DE EJECUCIÓN
AUTOMÁTICAMENTE EN VEZ DE CREARLA MANUALMENTE COMO SE HA DEFINIDO PREVIAMENTE.

* Si no disponemos de alguno de los módulos que utiliza el proyecto; aquellos que se especifican en requirements.txt,
deberemos instalarlo previamente a la ejecución, o esta nos devolverá error.


CONFIGURACÓN EJECUCIÓN PLOTS:

Una vez hemos obtenido los diferentes .csv fruto del Scrapping de la web de la Bolsa de Barcelona en su cierre
diario, nos disponemos a graficar, como objetivo tras dicho Scraping, los valores de los precios de las acciones
para la empresa que seleccionemos en cuestión durante los diferentes días que hayamos obtenido los precios de cierre.
Por ende, se habrá tenido que llevar a cabo el scrapping de la web durante diversos días (ejecución del main_Ibex35.py
en dichos días una única vez) obteniendo cada día un .csv cuyo formato se describe en el documento .pdf que se adjunta
en dicho módulo de Python y es resultado de la PEC.

Para ejecutar la imagen gráfica de la evolución de el precio de las acciones, nos disponemos sobre el archivo
plotting_IBEX35.py y lo ejecutamos procediendo de la misma manera en que se ha hecho con main_Ibex35.py y creando
una configuración de ejecución en caso de no disponerla.