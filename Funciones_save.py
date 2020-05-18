from Funciones_arh import dic_usu,dic_1,dic_2,dic_3# #importamos de Funciones_dic, dic_usu para creal el direcorio y lo usamos en la verificacion 
arh = open("Base.txt","r")#busca el documento con nombre de los usuarios
dic_usuarios = dic_usu(arh)
dic_municipios,lista_municipios = dic_1(arh)
dic_muni,est,dic_est = dic_2(arh,dic_municipios)
#print ("\n",dic_usuarios)
#print ("\n",dic_municipios)
#print ("\n",lista_municipios)
#print ("\n",dic_muni)
#print ("\n",dic_est)
est = dic_3(arh,est)
arh.close()
#print ("\n",est)
def save(dic_usuarios,lista_municipios,dic_est,est):
    """
    

    Parameters
    ----------
    dic_usuarios : dict
        diccionario con toda la infromacion de los usuarios con clave codigo de identidad
        y valro los contenidos de dicha infromacion
    lista_municipios : list
        lista con el nombre de cada uno de los municipios
    dic_est : dict
        diccionario con el nombre de cada estacion analizada
    est : dict
        diccionario con los datos ingresados

    Returns
    -------
    dic_municipios : dict
        diccionario que contine los municipjos y su subdiccionario vacio para 
        llenar con las estaciones
    dic_muni : dict
        diccionario que contine la infromacion por minicipio listo para
        llenar con las estaciones
    dic_usuarios : dict
        diccionario con las claves y los valores de los diccionarios
    lista_municipios : list
        lista de los municipios que se tienen registrados
    dic_est : dict
        diccioanrio con las estaciones numeradas
    est : dict
        diccioanrio ingresado de los valores analizados

    """
    x = open("Base.txt","w")
    x.close() #Abre y elimina todos los valores que hay en en el documento base 
    x = open("Base.txt","a") #reabre el documetno base con la intencion de agregar datos
    for i in dic_usuarios:
        s = ("<"+i)
        for a in range (3):
            s = (s+";"+dic_usuarios[i][a])#imprime los valores organnizados en el formato pedido de usurario
        s = (s+">\n")
        #print (s)
        x.write(s) #agrega dicha edicion al documetno append
    x.write("\n")
    #print ("\n")
    s = (":")
    for i in lista_municipios:
        s = (s+i[0]+",")
    s = s[:-1]
    s = (s+"\n")
    #print (s)
    x.write(s) #agrega la lista de municipios al documento
    x.write("\n")
    #print ("\n")
    for i in dic_est:
        s = (i+","+dic_est[i]+"\n")
        #print (s)
        x.write(s)
    x.write("\n") #imprime un end line en d el docuemtno para conocer bien la separacion dada
    #print("\n")
    dic = {}#crea un diccioanrio para poder agregar todos los datos al documetno final
    for i in est:
        for a in est[i]:
            ubi = a
            a = (a+";"+i+";")
            dic[a]= est[i][ubi]
    for i in dic:
        s = (i+dic[i]+"\n") #Para cada dato ade line se le agrega el docuemtno final
        x.write(s)
    x.write("\n")
    x.close()
    print ("\n")
    #vuelve a importar los valores de la funciones, y da el resultado para volver a crear los datos
    from Funciones_arh import dic_usu,dic_1,dic_2,dic_3# #importamos de Funciones_dic, dic_usu para creal el direcorio y lo usamos en la verificacion
    arh = open("Base.txt","r")#busca el documento con nombre de los usuarios
    dic_usuarios = dic_usu(arh)
    dic_municipios,lista_municipios = dic_1(arh)
    dic_muni,est,dic_est = dic_2(arh,dic_municipios)
    est = dic_3(arh,est)
    arh.close()
    return dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est #retorna los nuevos valores
#dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est = save(dic_usuarios,lista_municipios,dic_est,est)
#print ("\n",dic_usuarios)
#print ("\n",dic_municipios)
#print ("\n",lista_municipios)
#print ("\n",dic_muni)
#print ("\n",dic_est)
#print ("\n",est)