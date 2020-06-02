from Funciones_ini import presentacion,Error,visua_visi # Vasiables de uso en bsuqueda
from Funciones_usu import verifi_usu #Variable de verificaion de usuario
from Funciones_reg import registrado,Error_float #Variables que operan con el registro
from Funciones_arh import dic_usu,dic_1,dic_2,dic_3,dic_val #importamos de Funciones_dic, dic_usu para creal el direcorio y lo usamos en la verificacion 
from Funciones_save import save
ava = False # Validaar para iniciar
arh = open("Base.txt","r")#busca el documento con nombre de los usuarios
dic_usuarios = dic_usu(arh)
dic_municipios,lista_municipios = dic_1(arh)
#print (dic_municipios)
#print (lista_municipios)
dic_muni,est,dic_est = dic_2(arh,dic_municipios)
#print (dic_muni)
#print (dic_est)
arh,val = dic_val(arh)
#print ("\n",val,"\n")
est = dic_3(arh,est)
#print (est)
arh.close()
presentacion()#imprime la presentacion del programa
while ava == False:
    """
    while que se repite segun lo quiera el usuario
    """
    #Trabaja con error epara optenr un valor que nos permita trabajar de menu
    ava = Error("\n"+("\t"*3)+"Ingrese su tipo de usuario"+"\n\n"+("\t"*3)+"1. Usuario Registrado\n"+("\t"*3)+"2. Usuario Visitante"+"\n\n"+("\t"*3)+"3. SALIR")
    if ava == 1:#en caso de que sea ususario registrado
        ava,tipo = verifi_usu(dic_usuarios,Error)#averigua si el codigo de usuario esta
        if ava == True:#en caso de que el usuario alla sido validado
            arh = open("Base.txt","r")#busca el documento con nombre de los usuarios
            dic_usuarios = dic_usu(arh)
            dic_municipios,lista_municipios = dic_1(arh)
            dic_muni,est,dic_est = dic_2(arh,dic_municipios)
            arh,val = dic_val(arh)
            est = dic_3(arh,est)
            arh.close()
            ava = registrado(tipo,Error,Error_float,dic_usuarios,dic_municipios,dic_muni,est,dic_est,lista_municipios,val,save) #realice la funcion correspondiente al usuario
            print ("\n"*224)
            presentacion()#imprime la presentacion del programa
        else:
            print ("\n"*224)
            presentacion()#imprime la presentacion del programa
    elif ava == 2:#en caso de que sea un visitante        
        arh = open("Base.txt","r")#busca el documento con nombre de los usuarios
        dic_usuarios = dic_usu(arh)
        dic_municipios,lista_municipios = dic_1(arh)
        dic_muni,est,dic_est = dic_2(arh,dic_municipios)
        arh,val = dic_val(arh)
        est = dic_3(arh,est)
        arh.close()
        ava = visua_visi(dic_municipios,dic_muni,est,dic_est,Error,val)#imprima la infromacion que solicita el visitante
        print ("\n"*224)
        presentacion()#imprime la presentacion del programa
    elif ava == 3:#en caso de no queres contiuar salga
        ava = True
    else:
        print ("\n"*224)
        presentacion()#imprime la presentacion del programa
        print ("\nValor fuera del rango") #Aviso en caso de que se selccionoa una obcion fiera del rango
        ava = False
print ("Adios :D")#Comentario de despedida