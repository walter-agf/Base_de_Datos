import os
from Funciones_dic import dic_usu,dic_1,dic_2 #importamos de Funciones_dic, dic_usu para creal el direcorio y lo usamos en la verificacion 
from Funciones_ini import presentacion,Error,visua_visi # Vasiables de uso en bsuqueda
from Funciones_usu import verifi_usu #Variable de verificaion de usuario
from Funciones_reg import registrado,Error_float #Variables que operan con el registro
directorio_actual = os.getcwd() #averigua en que carpeta nos encotramos
directorio = (directorio_actual+"/Base")#Ingrea e la carpeta base en la carpeta en la que nos encontremos
dic_usuarios = dic_usu(directorio)#Crea el dic usuarios
ava = False # Validaar para iniciar
presentacion(directorio)#imprime la presentacion del programa
while ava == False:
    """
    while que se repite segun lo quiera el usuario
    """
    #Trabaja con error epara optenr un valor que nos permita trabajar de menu
    ava = Error("\n"+("\t"*3)+"Ingrese su tipo de usuario"+"\n\n"+("\t"*3)+"1. Usuario Registrado\n"+("\t"*3)+"2. Usuario Visitante"+"\n\n"+("\t"*3)+"3. SALIR")
    if ava == 1:#en caso de que sea ususario registrado
        ava,tipo = verifi_usu(dic_usuarios,Error)#averigua si el codigo de usuario esta
        if ava == True:#en caso de que el usuario alla sido validado
            ava = registrado(directorio,tipo,Error,Error_float,dic_1,dic_2,dic_usu) #realice la funcion correspondiente al usuario
            print ("\n"*224)
            presentacion(directorio)#imprime la presentacion del programa
        else:
            print ("\n"*224)
            presentacion(directorio)#imprime la presentacion del programa
    elif ava == 2:#en caso de que sea un visitante
        ava = visua_visi(directorio,Error)#imprima la infromacion que solicita el visitante
        print ("\n"*224)
        presentacion(directorio)#imprime la presentacion del programa
    elif ava == 3:#en caso de no queres contiuar salga
        ava = True
    else:
        print ("\n"*224)
        presentacion(directorio)#imprime la presentacion del programa
        print ("\nValor fuera del rango") #Aviso en caso de que se selccionoa una obcion fiera del rango
        ava = False
print ("Adios :D")#Comentario de despedida