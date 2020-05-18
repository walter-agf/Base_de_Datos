from Funciones_arh import dic_usu,dic_1,dic_2,dic_3# #importamos de Funciones_dic, dic_usu para creal el direcorio y lo usamos en la verificacion 
arh = open("Base.txt","r")#busca el documento con nombre de los usuarios
dic_usuarios = dic_usu(arh)
dic_municipios,lista_municipios = dic_1(arh)
dic_muni,est,dic_est = dic_2(arh,dic_municipios)
est = dic_3(arh,est)
arh.close()
print ("\n",dic_usuarios)
#print ("\n",dic_municipios)
print ("\n",lista_municipios)
#print ("\n",dic_muni)
print ("\n",dic_est)
print ("\n",est)