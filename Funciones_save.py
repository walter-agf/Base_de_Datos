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
    x = open("Base.txt","w")
    x.close()
    x = open("Base.txt","a")
    for i in dic_usuarios:
        s = ("<"+i)
        for a in range (3):
            s = (s+";"+dic_usuarios[i][a])
        s = (s+">\n")
        #print (s)
        x.write(s)
    x.write("\n")
    #print ("\n")
    s = (":")
    for i in lista_municipios:
        s = (s+i[0]+",")
    s = s[:-1]
    s = (s+"\n")
    #print (s)
    x.write(s)
    x.write("\n")
    #print ("\n")
    for i in dic_est:
        s = (i+","+dic_est[i]+"\n")
        #print (s)
        x.write(s)
    x.write("\n")
    #print("\n")
    dic = {}
    for i in est:
        for a in est[i]:
            ubi = a
            a = (a+";"+i+";")
            dic[a]= est[i][ubi]
    for i in dic:
        s = (i+dic[i]+"\n")
        x.write(s)
    x.write("\n")
    x.close()
    print ("\n")
    from Funciones_arh import dic_usu,dic_1,dic_2,dic_3# #importamos de Funciones_dic, dic_usu para creal el direcorio y lo usamos en la verificacion
    arh = open("Base.txt","r")#busca el documento con nombre de los usuarios
    dic_usuarios = dic_usu(arh)
    dic_municipios,lista_municipios = dic_1(arh)
    dic_muni,est,dic_est = dic_2(arh,dic_municipios)
    est = dic_3(arh,est)
    arh.close()
    return dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est
#dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est = save(dic_usuarios,lista_municipios,dic_est,est)
#print ("\n",dic_usuarios)
#print ("\n",dic_municipios)
#print ("\n",lista_municipios)
#print ("\n",dic_muni)
#print ("\n",dic_est)
#print ("\n",est)