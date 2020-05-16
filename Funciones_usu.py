def verifi_usu(dic_usuarios,Error):
    """
    Verifica si los valores ingresdos por el usuario, pretenenecen a la base
    de datos de manera comparativa y usando una base de datos como diccionario

    Parameters
    ----------
    dic_usuarios : dict
        diccionario con toda la informacion de la bse de datos de usuarios
        que depues se modifia para saber si algunos valores ingresados por
        el usuario se encuentran dentro de la base de datos
    Error : fuction
        es muy util su uso para asegurarse de optener un entero

    Returns
    -------
    conti : booleano
        nos avisa si se hallo un usuario y contraseña validos o si el susuario solo 
        quiere volver al menu inicial
    tipo : string
        que nos muestra el tipo de usuario si este de tipo administrador o operador

    """
    ava = False #Valida ava
    print ("\n"*224)#imprime nueva pantalla
    while ava == False:#se repite miestras el usuario no de  con clave y usaurio o quiera salir
        ava = 0
        while ava == 0:#wuile que se repite hasta que el usuario ingrese un valor dentro del rango y que sea int
            ava = Error("Desea ingresar Usuario o volver a menu anterio\n\n\n\t1) Ingresar Usuario\n\n\t2) Volver al menú anterio")
            if ava > 2:#verifica que el valor este dentro del rango
                print ("Valor fuera del rango\n")
                ava = 0
        if ava == 1:#en caso de que el usuario quiera ingresar datos
            print ("\n\n\tIngrese su usuario (Documento o identificacion) y contraseña\n")
            usu = input("Usuario ---- >  ")#ingresa str
            pas = input("\n\nContraseña ---- >  ")
            if usu in dic_usuarios:#conpara con los str guardados en el diccionoario de la bsae de datos
                if dic_usuarios[usu][1] == pas:
                    conti = True #en caso de continaur le da un valor a conti
                    tipo = dic_usuarios[usu][2]#tambien averigua el valor de tipo
                    ava = True#sale de ciclo while
                    #imprime un ultimo mensaje personalizado
                    print (("\n"*224)+"Bienvenido  "+dic_usuarios[usu][0]+"  Eres  "+dic_usuarios[usu][2]+"\n\n")
                else:#en caso de que el usuario este pero la contraseña sea incorrecta
                    print ("\n\nContraseña Incorrecta\n\n")
                    ava = 0
            else:#en caso de no encotrar el usuario
                print ("\n\nUsuario no esta registrado\n\n")
                ava = 0
        elif ava == 2:#en caso de que el usuario no quiera ingresar datos
            conti = False#sale con conti
            ava = True#sale del ciclo while
            tipo = ""#para darle un valor a tipo que no se usara
    return conti,tipo#retorna un valor booleno y un tipo de dato