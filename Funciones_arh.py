def dic_usu(arh):
    x = arh.readline()
    lis = []
    while x != "\n":
        x = x[1:-1]
        lis.append(x)
        x = arh.readline()
    #print (lis)
    dic_usuarios = {}#crea el directorio vacio
    for i in lis:
        """
        For que en base a la cantida de lineas  que hay en usuario bsuca 
        la coma sigueinte por el orden de las claves y de las coantidades
        asi que crea un diccionario con una clave igual a la cantidad que
        hay antes de la coma y con un valor despues de la coma
        """
        pos = i.find(";")#bsuca la coma y devuelve una posicion
        rt = i[pos+1:]
        #print (rt)
        lista = []
        for a in range (3):
            """
            Por cada vuelta crea un lista con su clave y su contenido
            """
            pos_rt = rt.find(";")
            lista.append(rt[:pos_rt])
            rt = rt [pos_rt+1:]
        #print ("\n",lista)
        i = (i[:pos],lista)
        #print (i)
        dic_usuarios[i[0]] = i[1]#Agrega dicha informacion al diccionario
    #print ("\n",dic_usuarios)
    return dic_usuarios
def dic_1 (arh):
    """
    Resibe una direccion o ubicacion y retorna un diccionario
    y segun la cantidad de lineas que ingresa da un orden y ubicaicon
    de cada uno
    """
    x = arh.readline()
    lista_municipios = []
    z = x.count(",")
    x = x[1:]
    for i in range (z+1):
        pos = x.find(",")
        s = x[:pos]
        lista_municipios.append(s)
        x = x[pos+1:]
    #print (municipios.read())
    #print("\n",lista_municipios)
    key = []#crea otra lista a la que le agregaremos las claves
    for i in range(0,len(lista_municipios)):
        """
        Quita del del final de la lista anterior la el nueva lienea /n
        para terner una lista solo con el str de cada municipio
        """
        lista = []
        lista.append(lista_municipios[i])#elinina el finla \n
        lista_municipios[i] = lista# y te reubica en la poscion presidasda 
        key.append(i+1)#agrega a la lista vacia cada poscion en el ordenpredestinado
    #print("\n",lista_municipios)
    #print ("\n",key)
    dic_municipios = dict(zip(key,lista_municipios))#crea el diccionario con base a dos listas
    #print ("\n",dic_municipios)
    return dic_municipios,lista_municipios#Retorna el diccionario creado
#arh = open("Base.txt","r")#busca el documento con nombre de los usuarios
#dic_municipios = dic_1(arh)#Probando la funcion anterior
#print ("\n",dic_municipios)
def dic_2(arh,dic_municipios):
    """
    Con base en una ubicacion de directorio, buca un docuemntoq ue contega
    las estaciones y su respectivo orden, por lo que crea un diccionario
    respetano el orden de los municipios y el avance del mismo
    """
    diccio = dic_municipios.copy()
    for i in diccio:
        diccio[i] = diccio[i].copy()
        diccio[i].append({})
    arh.readline()
    lista_estaciones = arh.readline()#Crea una lista con la cantidad de estaciones y sus repectiva ubicacion    
    lis = []
    est = {}
    dic_est = {}
    while lista_estaciones != "\n":
        """
        Quita del final de la posicion de cada lista que es un nueva linea (\n)
        para conservar la integridad y la calidad de cada lista
        """
        pos = lista_estaciones.find(",")
        est[lista_estaciones[:pos]] = {}
        dic_est[lista_estaciones[:pos]] = lista_estaciones[pos+1:-1]
        lis.append(lista_estaciones[pos+1:-1])
        lista_estaciones = arh.readline()
    #print (est)
    for i in lis:
        pos = i.find(",")
        name = i[:pos]
        city = i[pos+1:]
        for a in diccio.keys():
            if diccio[a][0] == city:
                can = len(diccio[a][1])
                sa = []
                sa.append(name)
                sa.append({})
                diccio[a][1][can+1] = sa 
    return diccio,est,dic_est#Retorna el nuevo diccionario que es en realidad el original mutado
#dic_municipios_2 = dic_2(dic_municipios)
#print ("\n",dic_municipios_2)
def dic_val(arh):
    x = arh.readline()
    z = x.count(";")
    val = {}
    for i in range (z+1):
        pos = x.find(";")
        con = x[:pos]
        x = x[pos+1:]
        pos = con.find("[")
        val[con[:pos]] = con[pos:]
    x = arh.readline()
    return arh,val
def dic_3(arh,est):
    #print (est)
    x = arh.readline()
    while x != "":
        #print (x)
        pos = x.find(";")
        date = x[:pos]
        x = x[pos+1:]
        pos = x.find(";")
        esta = x[:pos]
        info = x[pos+1:-1]
        #print(esta)
        #print(date)
        est[esta][date] = info
        x = arh.readline()
    return est
        