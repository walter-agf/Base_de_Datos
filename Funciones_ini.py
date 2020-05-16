import os #Importamos la libreria os para saber en que acarpeta estamos
import datetime #Importamos esta libreria para saber la fecha actual
from Funciones_dic import dic_1,dic_2 #Importamos estas dos funciones de del documento Funciones Dic para funcionar mas adelante 
directorio_actual = os.getcwd()#Busca en el directorio actual
#print (directorio_actual)
#print ("\n",os.listdir(directorio_actual))##LISTA los documentos que estan dentro del directorio actual
directorio = (directorio_actual+"/Base")#Le agregag el nombre de la carpeta que suponemos se encutra dentro del archvi pre instalado
#print ("\n",directorio)
def presentacion(directorio):
    """
    Solo hace el proceso de imprecion del menu inicial y un comentario
    """
    x = open(directorio+"/presentacion.txt","r")
    print (("\n"*2)+x.read())
    print ("La administración departamental, consciente de los problemas") 
    print ("que el cambio climático y la contaminación del aire puede")
    print ("causar a sus habitantes, decidió iniciar un proyecto para")
    print ("instalar estaciones de monitoreo de variables ambientales y") 
    print ("de calidad del aire en las diferentes subregiones del")
    print ("departamento, para recolectar datos que sirvan de insumo")
    print ("para diseñar políticas públicas que permitan mitigar los efectos")
    print ("de estos fenómenos en la población.")
def Error(tex):
    """

    Parameters
    ----------
    tex : strig
        Solcita el ingreso de un numero que tiene, por lo que en caso de no serlo genra un error 
        y prosige otra vez el codigo hasta que se entrege un entero

    Returns
    -------
    y : int

    """
    y = ""
    while type(y) is str :#Repite miestras el numerop sea un string
        try:
            print (tex)#imprime lo ingresado previamente en tex
            y = int(input("---> "))
        except ValueError:#en caso de ser incorrecto sige con el programa hasta que sea correcto imprimiendo un mensaje de valor incorrecto
            print (("\n"*224)+"Valor Incorrecto reingrese")
    return y#retorna el valro entero
def visua_visi(directorio,Error):
    """
    
    Parameters
    ----------
    directorio : string
        ubciacion de la carpeta donde se encuentras los archivos de infromacion
    Error : fuction
        de tipo funcion para usarla en el trabajo a realizar

    Returns
    -------
    TYPE Boleano
        Despues de imprimir todo lo solicitado imprime resulta un booleano para saber si se desea
        continuar usando esta funcion de uso de trabajo

    """
    def cambio_fecha(d,day,month,year):
        """
    
        Parameters
        ----------
        d : int
            dato que define cuentos dais atras se dea buscar, por parametro de meses 
            solo se permite un valor hasta 28 por logica de analizis, ya que dependido
            del mes puede fallar y en tal caso es mejor usar el analicis por fehcas espesificas
        day : int
            dia actual analizado
        month : int
            mes actual analizado
        year : int
            año actual analizado

        Returns
        -------
        day : int
            dependiendo de la cantidad de dias analizados atras devuelve un dia 
            atras de la fecha actual antes ingresada
        month : int
            dependiedo de las fechas previas si al ir a tras cambia de mes
            se guarda el mes en cambio 
        year : int
            igual en caso de cambiar de año se guarda el cambio 
            para retornar un año diferente al definido

        """
        day -= d #la cantidad e dias actuales menos los dias predefinidos
        if day < 1:#si ocurrec unc cambio de mes
            """
            este if pregunta en que mes fue el cambio para saber a que mes hay 
            que restar y reunbicar cantidad segun la cantidad de dias
            """
            if month in [1,2,4,6,8,9,11]:
                day = 31 + day
                if month == 1:
                    year -= 1
                    month = 12
            elif month in [3]:
                month -= 1
                """
                en cos de que el cambi hata sido en marzo, preugnta si dicho mes de febrero
                fue bisisesto o no dependido del año
                """
                if year%4 == 0 and year%100 != 0 or year%100 == 0 and year%400 == 0:
                    day = 29 + day #en caso de año bisiesto
                else:
                    day = 28 + day #en caso contrario
            elif month in [5,7,10,12]:
                month -=1
                day = 30 + day
        return day,month,year#retorna los nuevos valores de fecha predefinidos
    def ingreso_fecha(Error):
        """
        
        Parameters
        ----------
        Error : fuction
            funcion que se usa para evitar el error en casod e que alguien ingrese un valor 
            string 

        Returns
        -------
        day : int
            devuelve un valor, predefinidos por el usuario
        month : int
            devuelver un valor para los meses predefinidos por el usuario
        year : int
            devuelve un valor para el año ingresado por el usuario

        """
        tex = ("\n\n\tAño [NUMERO UNICO]?")
        year = Error(tex)#se evita el error y el ususario ingresa un numero
        tex = ("\n\n\tMes [NUMERO UNICO]?")
        month = Error(tex) #se evita el error y el usuario ingresa numero
        while month > 12 or month <= 0:
            """
            en caso de que el mes ingresado sea ilogico por ser mayor a doce
            solicita que se reingrese hasta que dicho valor sea logioc
            """
            print (("\n"*224)+"Valor imposible, Reingrese")
            month = Error(tex) #ingreso del mes
        tex = ("\n\n\tDia [NUMERO UNICO]?")
        day = Error(tex) #ingreos del dia
        """
        dependiedo del mes que se analiza hay una cantidad e dias distintos
        por ende se analiza que segun el mes se siga ingresando el numero
        """
        if month in [1,3,5,7,8,10,12]:
            while day > 31 or day <= 0:
                print (("\n"*224)+"Valor imposible, Reingrese")
                day = Error(tex)
        if month in [4,6,9,11]:
            while day > 30 or day <= 0:
                print (("\n"*224)+"Valor imposible, Reingrese")
                day = Error(tex)
        if month in [2]:
            if year%4 == 0 and year%100 != 0 or year%100 == 0 and year%400 == 0:
                while day > 29 or day <= 0:
                    print (("\n"*224)+"Valor imposible, Reingrese")
                    day = Error(tex)
            else:
                while day > 28 or day <= 0:
                    print (("\n"*224)+"Valor imposible, Reingrese")
                    day = Error(tex)
        return day,month,year #retorna los valores dados anteriormete para los nuevos en fecha
    def muni_est_val(directorio,Error):
        """
        

        Parameters
        ----------
        directorio : string
            la ubicacion actual en la que no encontramos para el uso de
            algun documento dentro
        Error : fuction
            para el uso de dicha funcion delntro del codigo

        Returns
        -------
        muni : list
            Una lista de los municipios que usuaurio quiere usar
        est : list
            una lista de las estaciones dependiendo del municipio
        val : list
            una lista de los valores que el ususario desea concoer

        """
        muni = [] #Crea la lista de los municipios
        print (("\n"*224)+"Elige en que municipios deseas buscar\n")
        dic_municipios = dic_1(directorio) #Crea un diccionario con los municipios
        for i in dic_municipios.keys():#dependiendo de las claves del diccionario
            if i < 10 : #solo organiza por estetica
                print (i," => ",dic_municipios[i][0])
            else:
                print (i,"=> ",dic_municipios[i][0])
        ava = 0 #regresa el valor de ava para continuar
        while ava > 2 or ava <= 0:# Pregunta si desea buscar en todos los municipios o en municipios en espesifico
            ava = Error("\n¿Desea buscar en ?\n\n\n\t1) Todos los municipios\n\n\t2) Escoger los municipios")
            print ("\nValor fuera del rango")#Descarta en caso de no estar dentro del rango de busqueda
        print ("\n"*224)
        if ava == 1:
            for i in dic_municipios.keys():
                muni.append(i)#un for para agregar todos los municipios posibles de analicis
        elif ava == 2:
            """
            se realiza en caso de que el ussuario queira ignresar los municipios
            """
            for i in dic_municipios.keys():
                if i < 10 :
                    print (i," => ",dic_municipios[i][0])
                else:
                    print (i,"=> ",dic_municipios[i][0])
            print ("\n\n Ingresa los municipios a buscar en la fecha escogida")
            print ("si no quieres buscar mas municipios pulsa [ 0 ]")
            ava = None
            while  ava != 0:
                """
                repite el proceso contando que este dentro del rango
                y termina cuando el usaurio ingrese 0
                """
                ava = Error("\nIngrese los municipios")
                if ava != 0:
                    muni.append(ava)
        dic_municipios = dic_2(directorio,dic_municipios)#crea el directorio con las estaciones de cada direcorio
        #print (muni)
        est = [] #Crea la lista de estaciones
        ava = 0
        while ava > 2 or ava <= 0: #Repite el proceso hasta que el ussuario ingrese lo que quiere hacer, si seleccionar cada esatcion o con todas las estaciones
            ava = Error("\n¿Desea buscar en ?\n\n\n\t1) Todos las estaciones \n\n\t2) Escoger las estaciones")
            print ("\nValor fuera del rango")
        print ("\n"*224)
        for i in muni:#Buscador y dependeido de lo que pdidio el usuario agrega o no a la lista
            lis = []
            lista = dic_municipios[i]
            can = len(lista[1])
            if ava == 1:#En caso de que el ususario no queira agregar presonalizadamente agregaa cada estacion dentro de muni
                for i in range (can):
                    lis.append(i+1)
                est.append(lis)
            elif ava == 2:#en caso de el el ussuario quiera agregar
                if can == 0:#en caso de que no haya estaciones para ese muicipio
                    print ("▓▓▓▓▓▓ EL Municipio de "+lista[0].upper()+" No tiene estaciones registradas ▓▓▓▓▓▓\n\n")    
                    est.append(lis)#lo agrega a lis
                else:
                    for a in range(can): #Repite el proceso segun el nuermo entro de la cantidad de estaciones del valor de muni
                        print ((a+1)," --> ",lista[1][a+1][0])
                        valor = None
                    while  valor != 0: #Repte el porcesopara cada esatcion de la lista lis,q ue tiene que esatr dentro de la lista lis
                        print ("\nPara el municipio de "+lista[0].upper())
                        valor = Error("\n\tIngrese las estaciones deseadas\n\tTerminar de ingresar [ 0 ]")
                        if valor > can or valor < 0:#en caso de que el valor no este dentro de la lista
                            print("\n\n\tValor inconcluso reintente\n")
                        elif valor != 0:
                            lis.append(valor)
                    est.append(lis) #Luego lis se agrega a la lista de esatciones apra hacer una listad e listas
                    print ("\n"*224)
        #print (est)
        print ("Ingrese las varianles que desea medir")
        ava = 0
        val = [] #Crea la listad de los valores
        while ava > 2 or ava <= 0:#sea asegura que lo que ingrese el usuario este dentro del valor
            ava = Error("\n¿Desea buscar en ?\n\n\n\t1) Todos las mediciones \n\n\t2) Escoger las mediciones\n\n\n\tRecuerda que si queires ver las medidicones en otro orden\n\tingresa en la opcion dos y da el orden")
            print ("\nValor fuera del rango")
        print ("\n"*224)
        if ava == 1: #Si el usuario quiere usuari todos los valores, los agrega en orne predetermiando 
            val = [1,2,3,4]
        elif ava == 2: #Si el usaurio queires ignresar los valores
            print ("Ingrese las variables que desea buscar")
            print ("Recuerda que orden ingresado orden impreso")
            ava = 0
            while ava == 0:#reite segun la cantidad de valores ingresados
                ava = Error("\n\t1) PM 10\n\t2) PM 2.5 \n\t3) Temperatura\n\t4) Humedad\n\nTermianr de ingresar [ 0 ]")
                if ava > 4 or ava < 0:#verifica que el valor este dentro del rango
                    print ("Valor fuera del rango reingrese")
                    ava = 0
                else:
                    if ava == 0:
                        print ("\n"*224)
                        ava = None
                    elif len(val) < 4:
                        val.append(ava)#agrega a val si el valor se puede definir si que se repita no se puede pasar de 4 valores
                        if len (val) == 4:
                            ava = None
                        else :
                            ava = 0
                    else:
                        ava = None
        return muni,est,val#retorna las cuatro lista de valores a analizar
    def busqueda(year,month,day,directorio,mun_est_val,Error):
        """
        Con base a una fecha busca los valores de datos que se encutran despues
        de dicha fehca hasta la actualidad
        Parameters
        ----------
        year : int
            valor de año a bsucar a partir
        month : int
            valor de mes a buscar
        day : int
            valor de dia a buscar
        directorio : string
            ubicacion actual dentro del computador
        mun_est_val : fuction
            para sus uso dentro de la funcion
        Error : fuction
            para su uso dentro de la funcion

        Returns
        -------
        continuar : boleano
            si se desa continaur despues de hacer la busqueda

        """
        dic_municipios = dic_1(directorio)#crea el diccionario con los municipios
        dic_municipios = dic_2(directorio,dic_municipios)#crea el diccionario con als esatciones incluidas tambien
        muni,est,val = mun_est_val(directorio,Error)
        texto = ["PM10 "," PM2.5 ","Temp","Humedad"]#posibles cantidades de datos
        tex = ["μg/m³","μg/m³"," °C ","  %   "]
        imp = ""
        sep = ""
        for i in val:
            """
            for que se repite para agregar un menu de texto que nos diga cuales 
            variable estamos analindo
            """
            imp = imp+texto[i-1]+" "
            sep = sep+tex[i-1]+"  " 
        print ("                      "+imp)
        print ("                      "+sep,end="\n\n")
        x = open(directorio+"/ingreso.txt","r")#abre el docuemnto ingreso
        for i in x:
            """
            busca en cadad linea del docuemtno ingreso
            para saber si corresponde dentro de los apramentos preestablecidos
            """
            pos = i.find(",")
            municipio = int(i[:pos])# averigua en que municipio esta el registro
            i = i[pos+1:]
            pos = i.find(";")
            estacion = int(i[:pos])#averigua en que estacion esta el municipio
            i = i[pos+1:]
            pos = i.find(",")
            ubi = i[:pos]#crea la ubicacion solo con la fecha y hora para luego usarlos como clave dentro del diccionario de imprecion
            if municipio in muni:
                pos = muni.index(municipio)#Averigua en que posisicon de la tabla muni esta dicho municipio dado,siempre la primera posicion caso de que le usuario repita el municipio por error
                if estacion in est[pos]:#si la estacion esta dentro de la lista esatacion
                    pos = i.find("-")
                    año = int(i[:pos])#averigua el año en que se encuentra dicha linea
                    i = i[pos+1:]
                    if año >= year :#conpara con el valor de year si es depues a antes del mismo año
                        pos = i.find("-")
                        mes = int(i[:pos])#averigua el mes en que esta
                        i = i[pos+1:]
                        if año == year and mes < month:#compara si ese mes el el mismo del mismo año y en casod de se antes no se cuenta la linea
                            print(end="")
                        else :#en caso de que la linea si cuente
                            pos = i.find(" ")
                            dia = int(i[:pos])#averigua en que dia se esta valorando
                            i = i[pos+1:]
                            if año == year and mes == month and dia < day:#conpara si dicho dia fue antes o depues de loa analizado
                                print (end ="")
                            else:#en caso de que dicho dia sea despues de lo analizado
                                pos = i.find(",")
                                i = i[pos+1:]
                                i = i[1:-1]
                                lis = {}#crea el diccionario en lis para su analizis de valores
                                for a in range (1,5):
                                    pos = i.find(",")
                                    lis [a] = i[:pos]#agrega ala diccionario de lis todas las posciones posibles analisis de valores las cuatro
                                    i = i[pos+1:]
                                lista = []
                                for a in val:#usando dicha lista el for itera segun las variables var y agrega solo estas posibilidades de lis a la lista listas
                                    lista.append(float(lis[a]))
                                """
                                imprime segun la lista definida lso valores de ubu como ubicacion, la lista ya creada con los valores dados la ubicacion en municipios y la ubicacion en esatacion
                                """
                                print (ubi," ",lista,"  -  ",dic_municipios[municipio][0]," _ ",dic_municipios[municipio][1][estacion][0])
        print ("\nDesea volver al menu anterior o reingresar valores\nde municipios,estaciones y valores")
        ava = 0
        while ava == 0:
            """
            while que se repite meistras el usuario ignrese un valor invalido preugndo si quiere continuar o no
            """
            ava = Error("\n\t1)Volver al menu anterior\n\t2)Reingresar")
            if ava > 2 or ava < 0 :
                print ("Valor incorrecto, reingrese")
                ava = 0
            elif ava == 1:
                continuar = False
            elif ava == 2:
                continuar = True
        x.close()
        return continuar
    def busqueda_2(year_1,month_1,day_1,year_2,month_2,day_2,directorio,mun_est_val,Error):
        """
        A difernecia de busqueda, busqueda_2 resibe dos fechas 
        y busca los valores dentro del docuemtno ingreso que se encuentran solo dentro
        de dichas fechas seleccionadas
        Parameters
        ----------
        year_1 : int
            Años de origen de busqueda
        month_1 : int
            mes de origen de busqueda
        day_1 : int
            dia de origen de busqueda
        year_2 : int
            año de final de busqueda
        month_2 : int
            mes de final e busqueda
        day_2 : int
            dia de final de busqueda
        directorio : string
            ubicacion en la que nos encontramos actualmente
        mun_est_val : fuction
            funcion que usaremos para averiguar los municipios estaciones y valores
        Error : fuction
            valro que usaremos para evitar errores

        Returns
        -------
        continuar : booleano
            despues de imprimir averigua si desea continuar, o volver al menu anterior 

        """
        dic_municipios = dic_1(directorio)#crea el diccionario dependiendo de los municipios
        dic_municipios = dic_2(directorio,dic_municipios)#crea el diccionario con las estaciones
        muni,est,val = mun_est_val(directorio,Error)#averigua la listas de municipios y estaciones
        texto = ["PM10 "," PM2.5 ","Temp","Humedad"]#valores posbiles de cantidades para val
        tex = ["μg/m³","μg/m³"," °C ","  %   "]
        imp = ""
        sep = ""
        for i in val:#crea un string que depues se sua para imprimri las cantidades den tipo de val
            imp = imp+texto[i-1]+" "
            sep = sep+tex[i-1]+"  " 
        print ("                      "+imp)
        print ("                      "+sep,end="\n\n")
        x = open(directorio+"/ingreso.txt","r")#abre el docuemtno de ignreso donde esta la base de datos
        for i in x:#se repite para cada line de ingreso.txt para realizar la busquea iterativa
            pos = i.find(",")#bsuca la posicion del año
            municipio = int(i[:pos])
            i = i[pos+1:]#reingre el valor de i para el analisis
            pos = i.find(";")
            estacion = int(i[:pos])
            i = i[pos+1:]
            pos = i.find(",")
            ubi = i[:pos]#crea un string dond se alaja la fehca y la hora
            if municipio in muni:#pregunta si dicho municipio esta dentro de mun
                pos = muni.index(municipio)#averigua la posicon dentro de muni
                if estacion in est[pos]:#averigua si la estacion es requerida
                    pos = i.find("-")
                    año = int(i[:pos])#averigua el valor del año
                    i = i[pos+1:]
                    if año >= year_1 and año <= year_2:#compara is el año del valor es valido
                        pos = i.find("-")
                        mes = int(i[:pos])
                        i = i[pos+1:]
                        if año == year_1 and mes < month_1 or año == year_2 and mes > month_2:
                            #compara is el mes es ibvalido por encontrarce fuera del rango de bsuqueda
                            print(end="")
                        else:#en caso de encontrarse dento del rango de busqueda
                            pos = i.find(" ")
                            dia = int(i[:pos])
                            i = i[pos+1:]
                            if año == year_1 and mes == month_1 and dia < day_1 or año == year_2 and mes == month_2 and dia > day_1:
                                #averigua di el dia esta dentro del rango de busqueda
                                print(end="")
                            else:#en caso de que el dia si este dentro del rango de busquda
                                pos = i.find(",")
                                i = i[pos+1:]
                                i = i[1:-1]
                                lis = {}#Crea el diccionario de trabajo
                                for a in range (1,5):
                                    pos = i.find(",")
                                    lis [a] = i[:pos]
                                    i = i[pos+1:]#agrega a lis todo los valores posibles de ingreso
                                lista = []
                                for a in val:
                                    lista.append(float(lis[a]))#agrega los valores selecionados a la lista que leuga se imprimira
                                #Imprecion completa de la lista segun los parametro seleccionados anteriormente 
                                print (ubi," ",lista,"  -  ",dic_municipios[municipio][0]," _ ",dic_municipios[municipio][1][estacion][0])
        print ("\n Dese volver al menu anterior o reingresar valores de municipios,estaciones y valores")
        ava = 0
        while ava == 0:
            """
            se repite miestras el usuario ingrese valores invalidos 
            para la deccion de continaur o no
            """
            ava = Error("\n\t1)Volver al menu anterior\n\t2)Reingresar")
            if ava > 2 or ava < 0:
                print ("Valor incorrecto, reingrese")
                ava = 0
            elif ava == 1:
                continuar = False
            elif ava == 2:
                continuar = True
        x.close()
        return continuar 
    ava = True
    print ("\n"*224)
    while ava == True:
        """
        while del programa que realiza todos los proceso de las funciones en caso de 
        que el usuario quera seguir ingresando datos
        """
        day = datetime.date.today().day #Averigua el dia actial segun la fecha del sistema
        month = datetime.date.today().month #Averigua el mes del sistema
        year = datetime.date.today().year #Averigua el año del sistema
        ava = 0
        while ava == 0:#se repte para saber lo que quiere hacer le usuario
            ava = Error("\nIngresa el periodo de tiempo a buscar\n\n\t1) Ultimos 7 Dias\n\t2) Ultimos 30 dias\n\t3) Elegir fechas manualmente\n\n\n\t4) Volver al menu principal")
            if ava > 4 or ava < 0:
                print ("Valor fuera del rango reingrese")
                ava = 0
        if ava == 4:#si ava es 4 el programa nos se ejecuta y sale del procesos
            ava = False
        elif ava == 1:#si es uno realiza la reta de dias y realiza la busqueda
            day,month,year = cambio_fecha(7,day,month,year)#averigua la fecha hace 7 dias
            #print (day,"/",month,"/",year)
            ava = True
            while ava == True:#realia la busqueda segun la cantidad de veces que el usuario quiera cambiando municipios estaciones o valores
                ava = busqueda(year,month,day,directorio,muni_est_val,Error)
            ava = True#reorganiza el valor de ava que viene igual False
            print ("\n"*224)
        elif ava == 2:#en caso de que se quiera contar hace una semana 
            day,month,year = cambio_fecha(30,day,month,year)#Averigua la fehca hace 30 dias
            ava = True
            while ava == True:#Realiza la busqueda la cantidad de veces que el usuario quiera
                ava = busqueda(year,month,day,directorio,muni_est_val,Error)   
            ava = True
            print ("\n"*224)
        elif ava == 3:#EN casod e querer una fecha predestinada
            print ("\n"*224)
            print ("\nIngresa la fecha de origen de busqueda")
            day_1,month_1,year_1 = ingreso_fecha(Error)#Se ingresa la fecha de origen para buscar 
            while year_1>year or year_1 == year and month_1 > month or year_1 == year and month_1 == month and day_1 > day:  
                print (("\n"*224)+"Valor imposible ya que es en el futuro de la fecha actual")
                day_1,month_1,year_1 = ingreso_fecha(Error)#se repite miestras dicha fecha sea futura a la actula ya que no se tienen registros futuros
            print (("\n"*224)+"¿Dese buscar hasta la fecha actual o hasta una fecha en espesifico?")
            #en caso de tener un fecha real se pregunta si se queire contar hasta la fecha actual o tomar un fecha tope
            ava = Error("\n\t1) Bucar con fecha Actual\n\n\t2) Ingresar otra fecha")
            while ava > 2 or ava < 0:#si se quiere con la fecha actual se realiza la funcion busqueda
                ava = Error(("\n"*224)+"\nValor fuera del rango\n\n\n\t1) Bucar con fecha Actual\n\n\t2) Ingresar otra fecha")
            if ava == 1:#si se desa con otra fecha se busca otra funcion
                ava = True
                while ava == True:# en caso de ser con la fecha actual se hace con la fecha actual la funcion bsuqueda
                    ava = busqueda(year_1,month_1,day_1,directorio,muni_est_val,Error)
                ava = True
                print ("\n"*224)
            elif ava == 2:
                #en caso de ser con troa fecha se pregunta la otra fecha y se usa la funcion busqueda_2
                day_2,month_2,year_2 = ingreso_fecha(Error)#se pregunta la otra fecha
                while year_2<year_1 or year_2 == year_1 and month_2 < month_1 or year_2 == year_1 and month_2 == month_1 and day_2 < day_1: 
                    print (("\n"*224)+"Valor imposible ya que es en el pasado de la fecha antes ingresada")
                    day_2,month_2,year_2 = ingreso_fecha(Error)#se asegura que la fecha sea en el futuro de la fecha deseada
                ava = True
                while ava == True:#si se tienen amabsa fechas se hace las busqueda
                    ava = busqueda_2(year_1,month_1,day_1,year_2,month_2,day_2,directorio,muni_est_val,Error)#funcion busqueda_2
                ava = True
                print ("\n"*224)
    return ava#se retorna ava segun como halla quedado
#conti = visua_visi(directorio,Error)