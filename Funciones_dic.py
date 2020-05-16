import os
directorio_actual = os.getcwd()#Busca en el directorio actual
#print (directorio_actual)
#print ("\n",os.listdir(directorio_actual))##LISTA los documentos que estan dentro del directorio actual
directorio = (directorio_actual+"/Base")#Le agregag el nombre de la carpeta que suponemos se encutra dentro del archvi pre instalado
#print ("\n",directorio)
def dic_usu(directorio):
    """
    Funcion que parte de un documento ubicado en la posicion
    directorio y crea un diccionario con esa informacion,
    en este caso un directorio con la infomacion de los usuarios
    """
    usuarios = open(directorio+"/usuarios.txt","r")#busca el documento con nombre de los usuarios
    dic_usuarios = {}#crea el directorio vacio
    for i in usuarios:
        """
        For que en base a la cantida de lineas  que hay en usuario bsuca 
        la coma sigueinte por el orden de las claves y de las coantidades
        asi que crea un diccionario con una clave igual a la cantidad que
        hay antes de la coma y con un valor despues de la coma
        """
        pos = i.find(",")#bsuca la coma y devuelve una posicion
        rt = i[pos+1:]
        #print (rt)
        lista = []
        for a in range (3):
            """
            Por cada vuelta crea un lista con su clave y su contenido
            """
            pos_rt = rt.find(",")
            lista.append(rt[:pos_rt])
            rt = rt [pos_rt+1:]
        #print ("\n",lista)
        i = (i[:pos],lista)
        #print (i)
        dic_usuarios[i[0]] = i[1]#Agrega dicha informacion al diccionario
    #print ("\n",dic_usuarios)
    usuarios.close()#Cierra el documento
    return dic_usuarios
dic_usuarios = dic_usu(directorio)#aplicacion de la funcion anterior
#print ("\n",dic_usuarios)
def dic_1 (directorio):
    """
    Resibe una direccion o ubicacion y retorna un diccionario
    y segun la cantidad de lineas que ingresa da un orden y ubicaicon
    de cada uno
    """
    municipios = open(directorio+"/municipios.txt","r")#bsuca el documento municipios.txt
    #print (municipios.read())
    lista_municipios = municipios.readlines()#crea una lista cona las lineas ingresadas
    #print("\n",lista_municipios)
    key = []#crea otra lista a la que le agregaremos las claves
    for i in range(0,len(lista_municipios)):
        """
        Quita del del final de la lista anterior la el nueva lienea /n
        para terner una lista solo con el str de cada municipio
        """
        lista = []
        lista.append(lista_municipios[i][:-1])#elinina el finla \n
        lista_municipios[i] = lista# y te reubica en la poscion presidasda 
        key.append(i+1)#agrega a la lista vacia cada poscion en el ordenpredestinado
    #print("\n",lista_municipios)
    #print ("\n",key)
    dic_municipios = dict(zip(key,lista_municipios))#crea el diccionario con base a dos listas
    #print ("\n",dic_municipios)
    municipios.close()#Cierra el documento
    return dic_municipios#Retorna el diccionario creado
dic_municipios = dic_1(directorio)#Probando la funcion anterior
#print ("\n",dic_municipios)
def dic_2(directorio,dic_municipios):
    """
    Con base en una ubicacion de directorio, buca un docuemntoq ue contega
    las estaciones y su respectivo orden, por lo que crea un diccionario
    respetano el orden de los municipios y el avance del mismo
    """
    estaciones = open(directorio+"/estaciones.txt","r")#Abre el documento estaciones
    #print (estaciones.read())
    lista_estaciones = estaciones.readlines()#Crea una lista con la cantidad de estaciones y sus repectiva ubicacion    
    for a in range (len(lista_estaciones)):
        """
        Quita del final de la posicion de cada lista que es un nueva linea (\n)
        para conservar la integridad y la calidad de cada lista
        """
        lista_estaciones[a] = lista_estaciones[a][:-1]
    #print (lista_estaciones)
    for i in dic_municipios.keys():
        """
        Con base en cada clave de el diccionario de municipios ingresado
        anteriormente, ingresa la informacion de la lista de esatcion si esta
        corresponde al municipio seleccionado, respecto al primer nuero de 
        del poscionamiento de cada estacion
        """
        lista = []#Crea una lista donde se almacena las estaciones que pertenecen a cada municipio
        for a in range (len(lista_estaciones)):
            """
            Busca cada poscion de municipio y crea una lista que contega
            por cantidad de lista estaciones que son la posicon de indice
            de cada cantidad
            """
            pos_est = lista_estaciones[a].find(",")
            if int(lista_estaciones[a][:pos_est]) == i :
                lista.append(lista_estaciones[a][pos_est+1:])#corta el tramo de la posicon para solo conocer la nuemracion de las estaciones
        #print ("\n",lista)
        dic = {}
        if len(lista)>0 :
            for y in range (len(lista)):
                """
                Agrega a cada estacion una numeroacion para depues colocarlo
                clave
                """
                lista[y]= (str(y+1)+","+lista[y])
            #print ("\n",lista)
            for a in lista:
                """
                Crea una lista con el nombre solo sin la ubicacion de la
                estacion y ademas le agrega en una segunda posicion el nombre
                el diccionario que luego usaremos para agregacion la 
                informacion deseada.
                """
                pos_est = a.find(",")#BUsca la coma su poscion dentro del str
                lista_est = []#Crea la lsita a agregar
                #print (pos_est)
                lista_est.append(a[pos_est+1:])#con la posicion quita el espacio que esta en la coma
                lista_est.append({})#Agrega el diccionario al final
                #print (lista_est)
                dic [int(a[:pos_est])] = lista_est#Agrega al diccionario del luagr la estacion
            #print (dic_municipios[i][0])
            dic_municipios[i].append(dic)#Agrega a la lista donde esta la ubicacion la estacion
        else:
            #print (dic_municipios[i][0])
            dic_municipios[i].append(dic)#En caso de esta vacio solo agrega el diccionario Vacio
        #print ("\n",dic)
    estaciones.close()#Cierra el docuemtno estaciones
    return dic_municipios#Retorna el nuevo diccionario que es en realidad el original mutado
dic_municipios_2 = dic_2(directorio,dic_municipios)
#print ("\n",dic_municipios_2)
def dic_3(directorio,dic_municipios):
    """
    Funcion diseñada para resibir una ubciacion donde buscar 
    los archivos de ingreso y agrega segun cada ubicacion al diccionario
    general donde se coloca en cada estacion correspondiete a loq eu queremos
    agregar
    """
    ingreso = open(directorio+"/ingreso.txt","r")#busca dentro del directorio el archivo ingreso
    #print ("\n"+ingreso.read())
    lista_ingreso = ingreso.readlines()#Crea un lista con la informacion line por liena de los ingreos
    for i in range (len(lista_ingreso)):
        #Les quita el (\n) del final a cada cantidad del cad indise de la lista
        lista_ingreso[i] = lista_ingreso[i][:-1]
    #print (lista_ingreso)
    for i in lista_ingreso:
        """
        Busca y accede a la posicion que se defina como la forma segun los
        datos anteriormete que deven permitir acceder a una posicon espesifica
        del diccionario
        """
        #print(i)
        pos = i.find(",")#busca la coma dentro del dato de linea analizado
        muni = int (i[:pos])#sabemos la psocion del diccionario dentor de los municipios
        i = i[pos+1:]#quita es parte dentro de la linea de texto
        pos = i.find(";")
        esta = int (i[:pos])
        #print (esta)
        i = i[pos+1:]
        #print (i)
        dic = dic_municipios[muni]
        #print (dic)
        dic = dic[1]
        #print (dic)
        dic = dic[esta]
        #print (dic)
        dic = dic[1]
        #print (dic)
        """
        Se busco dentor del diccionario las posiciones dadas anteriormente 
        ya que si conserva la fidelidad de la infromacion
        """
        pos = i.find(",")
        lista_val = []
        lista = i[pos+1:]
        lista = lista[1:-1]#Crea un str con la informacion separada por str 
        #print (lista)
        for a in range(4):
           pos = lista.find(",")#hace las iteraciones segun los 4 tipos de datos
           #print (pos)
           lista_val.append(float(lista[:pos]))#Crea un lista con cada valro pasandolo de srt a list
           lista = lista[pos+1:]#Elimina en el str la posiciones inecesarias
        #print(lista_val)
        pos = i.find(",")
        dic[i[:pos]] = lista_val#Agrega al diccionario genral segun el diccionario de la posicion en el que estabamos previamente
        #print (dic)
    ingreso.close()#Cierra el formularion ingreso
    return dic_municipios
dic_municipios_3 = dic_3(directorio,dic_municipios_2)
#print ("\n",dic_municipios_3)
