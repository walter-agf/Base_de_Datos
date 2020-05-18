import datetime
#from Funciones_save import save
#from Funciones_ini import Error#,visua_visi # Vasiables de uso en bsuqueda
#from Funciones_arh import dic_usu,dic_1,dic_2,dic_3# #importamos de Funciones_dic, dic_usu para creal el direcorio y lo usamos en la verificacion 
#arh = open("Base.txt","r")#busca el documento con nombre de los usuarios
#dic_usuarios = dic_usu(arh)
#dic_municipios,lista_municipios = dic_1(arh)
#print (dic_municipios)
#print (lista_municipios)
#dic_muni,est,dic_est = dic_2(arh,dic_municipios)
#print (dic_muni)
#print (dic_est)
#est = dic_3(arh,est)
#print (est)
#arh.close()
def Error_float(tex):
    """

    Parameters
    ----------
    tex : strig
        Solcita el ingreso de un numero que tiene, por lo que en caso de no serlo genra un error 
        y prosige otra vez el codigo hasta que se entrege un entero

    Returns
    -------
    y : float
        Conrla infromacion de los valroes ingresadas para cada valor pedidio
        en las mediciones necesarias
    """
    y = ""
    while type(y) is str :#Repite miestras el numerop sea un string
        try:
            print (tex)#imprime lo ingresado previamente en tex
            y = (input("---> "))
            if y == "ND" or y == "-999" or y == "Nd" or y == "nD" or y == "nd":
                y = float(-999)
            else:
                y = float(y)
        except ValueError:#en caso de ser incorrecto sige con el programa hasta que sea correcto imprimiendo un mensaje de valor incorrecto
            print (("\n"*224)+"Valor Incorrecto reingrese")
    return y#retorna el valro entero
def registrado(tipo,Error,Error_float,dic_usuarios,dic_municipios,dic_muni,est,dic_est,lista_municipios,save):
    """
    Parameters
    ----------
    tipo : str
        el tipo define que tipo de usuario es si un Operador o un Administrador
    Error : fuction
        Funcion que sirve para validar errores a la hora de la fabricacion
    Error_float : fuction
        Funcion que retorna solo valores de tipo flotante
    dic_usuarios : dict
        Diccionario que contine toda la informacion de los Usuarios que se analiza
    dic_municipios : dict
        diccioanrio que contiene una listad e los municipios analizados
    dic_muni : dict
        Diccionario que contiene cada variable del municipio
        con s varibale de de datos
    est : dict
        diccioanrio que contine todas las varibales de ingreso
    dic_est : dict
        Diccionario que contine todas las estaciones que se analizan dentro
        del documento
    lista_municipios : list
        lista que contine todos los municipios que se analizan
    save : fuction
        Funcion para guardar los datos de la edicion en las nuevas variables

    Returns
    -------
    ava : Booleano
        retora el deseo de continuar en caso de que se quiera

    """
    ava = True
    while ava == True:
        """
        Dentro de este while se crea el menu y se hacen miestras el usuraio
        quiera todas las ediciones del administrador
        """
        if tipo == "Administrador":
            while ava == True:
                conti = 0
                while conti == 0: #en caso de que el usuario quiera hacer algun accion se repite hasta que la accion sea lo suficientemente logica
                    conti = Error("Que accion desea realizar\n\n\n\t1) Gestionar estaciones\n\n\t2) Gestionar Usuario\n\n\t3) Volver al menu principal")
                    if conti > 3 or conti <= 0:
                        print ("\n"*224)
                        print ("Valor Fuera del rango")
                        conti = 0
                if conti == 3: #En caso de que el usuario queira salir
                    ava = False
                elif conti == 1 :#En caso de que administrador queira trabajar ocn la informacion de las estaciones
                    avanzar = 0
                    print ("\n"*224)
                    while avanzar == 0:#se repite hasta que el adminsitrador indique exactamente que accion desea realizar
                        avanzar = Error("¿ Que accion desea hacer ?\n\n\n\t1) Crear estacion\n\n\t2) Editar estacion\n\n\t3) Eliminar estacion")
                        if avanzar > 3 or avanzar <= 0:
                            print ("\n"*224)
                            print ("Valor inconcluso Reingrese\n\n")
                            avanzar = 0
                    if avanzar == 1:#en caso de de que lo que dese hacer es la creacion de una nueva estacion
                        print ("\n\n")
                        muni = 0
                        while muni == 0:#se muestras los municipios para su ingreso
                            for i in dic_municipios.keys():
                                if i < 10 :
                                    print (i," => ",dic_municipios[i][0])
                                else:
                                    print (i,"=> ",dic_municipios[i][0])
                            muni = Error("\n\nSeleccione en que municipio quieres crear la estacion")
                            if muni > i or muni <= 0:# en caso de que valor ignresado para muni no este dentro de la posible informacion
                                print ("\n"*224)
                                print ("Valor fuera del rango\n")
                                muni  = 0
                        print ("\n"*224)
                        if len(dic_muni[muni][1]) == 0: # en caso de que dicho municipio no tenga estacione sregistradas
                            print ("El municipio ",dic_muni[muni][0].upper(),"No tiene estaciones registradas")
                            i = 0
                        else:
                            for i in dic_muni[muni][1]:# en caso de que si tenga estaciones registardsas imprime el nombre de dichas estaciones
                                print (i," --> ",dic_muni[muni][1][i][0])
                        print ("\n\n\nIngrese el nombre de la nueva estacion")
                        i = i + 1
                        esta = input("---> ")#perminte ingresar el nombre de una nueva estacion
                        nume = int(max(dic_est))
                        nume = str(nume + 1)
                        st = dic_municipios[muni][0]
                        st = (esta+","+st)
                        dic_est[nume] = st #agrega dicho nombre a la varibale dic_est que es la que contine la infomacion de las estaciones 
                        #print (dic_est)
                        dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est = save(dic_usuarios,lista_municipios,dic_est,est)
                        print ("\n\n\n\n\n\nYa fue agregada la nueva estacion")
                        print ("Recuerda que se agrega en la ultima posicon de estacion disponible para el municipio")
                        ava = False
                        while ava != True: #imprime para volver al menu anterior
                            ava = Error("\nVolver al menu anterior, presiona [ 0 ]")
                            if ava != 0:
                                print ("Valor invalido reintentar\n\n")
                            else:
                                ava = True
                    elif avanzar == 2 : #en caso de que se queira editar una estaciones
                        print ("\n\n")
                        muni = 0
                        while muni == 0:
                            for i in dic_municipios.keys():#dicha esatcion a edtar debe estar dentro de los municipios disponibles
                                if i < 10 :
                                    print (i," => ",dic_municipios[i][0])
                                else:
                                    print (i,"=> ",dic_municipios[i][0])
                            muni = Error("\n\nSeleccione en que municipio quieres editar la estacion")
                            if muni > i or muni <= 0:
                                print ("\n"*224)
                                print ("Valor fuera del rango\n")
                                muni  = 0
                        print ("\n"*224)
                        if len(dic_muni[muni][1]) == 0: #EN caso de que el municipio not enga niguna estacion registrada
                            print ("El municipio ",dic_muni[muni][0].upper(),"No tiene estaciones registradas")
                            i = 0
                        else:
                            for i in dic_muni[muni][1]:#  Imprime las estacioens que estan registradas dentro del municipio
                                print (i," --> ",dic_muni[muni][1][i][0])
                            esta = 0
                            while esta == 0:# seleccionamos la estacion que queramos editar 
                                esta = Error("\n\nSeleccione la estacion a editar")
                                if esta > i or esta <= 0:
                                    print ("Valor fuera del rango Reingresar")
                                    esta = 0
                            print ("\n\nPara la estacion ",end = "\t")#Con dicho deato e la estacion trabajamos para realizar el analisis de la informacion proporcioanda
                            print (dic_muni[muni][1][esta][0].upper())
                            print ("\n\nComo desea renombrar la estacion ? ")
                            name = input(" --> ")
                            st = dic_municipios[muni][0]
                            estacion = dic_muni[muni][1][esta][0]
                            name = (name+","+st)
                            st = (estacion+","+st)
                            for i in dic_est: #itera la cantidad de veces que se tenga que para averiguar a que estacion pertenece en dic_est el valor de dic_muni estacional
                                if dic_est[i] == st:
                                    esta = i
                            dic_est[esta] = name
                            #GUarda toda la infmacion en las nuevas varibales de archivos que conserve datos
                            dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est = save(dic_usuarios,lista_municipios,dic_est,est)
                            print ("\n"*224)
                            print ("Edicion completada\n\n")
                    elif avanzar == 3 : #EN caso de que el administrador quiera eliminar alguna estacion
                        print ("\n\n")
                        muni = 0
                        while muni == 0:
                            for i in dic_municipios.keys():#imprime los municipios de datos como valores
                                if i < 10 :
                                    print (i," => ",dic_municipios[i][0])
                                else:
                                    print (i,"=> ",dic_municipios[i][0])
                            muni = Error("\n\nSeleccione en que municipio quieres eliminar la estacion")
                            if muni > i or muni <= 0:#en caso de que el valro asociado a muni sea incoherente
                                print ("\n"*224)
                                print ("Valor fuera del rango\n")
                                muni  = 0
                        print ("\n"*224)
                        if len(dic_muni[muni][1]) == 0: #En caso de que no haya ninguan estacion en ese dispositivo
                            print ("El municipio ",dic_muni[muni][0].upper(),"No tiene estaciones registradas")
                            i = 0
                        else:#en caso de que si haya estaciones que se puedan elimianr
                            for i in dic_muni[muni][1]:
                                print (i," --> ",dic_muni[muni][1][i][0])
                            esta = 0
                            while esta == 0:#preugnta vlaores logicos de la estacion que se desea eliminar
                                esta = Error("\n\nSeleccione la estacion a Eliminar")
                                if esta > i or esta <= 0:
                                    print ("Valor fuera del rango Reingresar")
                                    esta = 0
                            st = dic_municipios[muni][0]
                            estacion = dic_muni[muni][1][esta][0]
                            st = (estacion+","+st)
                            for i in dic_est:# averigua si dicha estacion seleccionada su poscion en el dicicoanrio dic_est
                                if dic_est[i] == st:
                                    esta = i
                            if len(est[esta]) != 0: #en caso de que esta vairbale tenga datos asociados 
                                seguir = 0
                                while seguir == 0: #Pregunta si se desea que se borre dicha estacion con todos los datos selecicoandos
                                    seguir = Error("\n\nValriable llena desea eliminar contenido\n\n\n\t1) SI\n\n\t2) NO")
                                    if seguir > 2 or seguir <= 0:
                                        print ("Valor fuera del rango Reingresar")
                                        seguir = 0
                                if seguir == 1: # en casod e que si se quiera borrar con todos los datos seleccioandos
                                    del est[esta] #elimina los datos dentro e est
                                    del dic_est[esta] #elimina la estacion como tal
                                    dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est = save(dic_usuarios,lista_municipios,dic_est,est)
                                    print ("\n"*224)
                                    print ("Edicion completada\n\n")
                                elif seguir == 2:
                                    print ("\n"*224)
                                    print ("Edicion NO realizada\n\n")
                            else:
                                del est[esta] #en caso de que no haya datos asocidos directaemnte elimina la variable
                                del dic_est[esta] #elimina la varibel dentro del diccionario de etaciones
                                dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est = save(dic_usuarios,lista_municipios,dic_est,est)
                                print ("\n"*224)
                                print ("Edicion completada\n\n")
                elif conti == 2 : # En caso de que se quiera trabajar ocn los usuarios
                    while ava == True:
                        avanzar = 0
                        print ("\n"*224)
                        while avanzar == 0:#infroma de manera logica la accion que desea realizar el usuario
                            avanzar = Error("¿ Que accion desea hacer ?\n\n\n\t1) Crear Usuario\n\n\t2) Editar Usuario\n\n\t3) Eliminar Usuario")
                            if avanzar > 3 or avanzar <= 0:
                                print ("\n"*224)
                                print ("Valor inconcluso Reingrese\n\n")
                                avanzar = 0
                        if avanzar == 1:# en caso de que administrador queira crear un nuemvo usuario
                            print ("\n\n")
                            for i in dic_usuarios.keys():# imprime los documentos y los nombres de los usuarios
                                print (i," --> ",dic_usuarios[i][0])
                            doc = "1"
                            while len(doc) < 10: #Solicita el ingreso de un nuevo numero que debe tenr omo minimom 10 caracteres
                                print ("\nIngrese usuario debe ser un numero y tener minimo 10 caracteres")
                                doc = str(Error("Ingrese el Documento"))
                                if len(doc) < 10:
                                    print ("\n\n\nValor invalido, Reingrese")
                                elif doc in dic_usuarios.keys():
                                    print ("\n\n\nDocumento ya esta en la base de datos")
                                    doc = "1"
                            lis = (doc+",") # con dicho documento se comienza a crear un tipo de cadena de caracteres para agregar
                            print ("Ingrese el nombre del usuario")
                            name = input("--> ")
                            lis = (lis+name+",")
                            pas = "1"
                            while len(pas) < 4:#se solicita que se ingrse una contraseña para analizar el tipo de dato
                                print ("\nIngrese la contraseña de usuario debe tener minimo 4 caracteres")
                                pas = input(" --> ")
                                if len(pas) < 4:
                                    print ("\n\n\nValor invalido, Reingrese")
                            lis = (lis+pas+",")
                            print("\n"*224)
                            ti = 3
                            while ti != 1 and ti != 2:#se solcitar ingresar el tipo de usuario para convalidad
                                ti = Error("Seleccione el tipo de usuario\n\n\n\t1) Administrador\n\n\t2) Operador")
                                if ti != 1 and ti != 2:
                                    print ("\n"*224)
                                    print ("Valor invalido reintentar")
                            if ti == 1:
                                ti = "Administrador"
                            elif ti == 2:
                                ti = "Operador"
                            lis = (lis+ti)
                            lis = (lis+"\n")
                            lista = []
                            pos = lis.find(",")
                            clave = lis[:pos]# se agrega cada infromacion auna lista que luego se agregagra a la varibel dic_usuarios
                            lis = lis[pos+1:]
                            for h in range (3):
                                pos = lis.find(",")
                                lista.append(lis[:pos])
                                lis = lis[pos+1:]
                            dic_usuarios[clave] = lista# se agrega la variable a la lista de usuarios
                            #se guarda la infromacion con la funcion save
                            dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est = save(dic_usuarios,lista_municipios,dic_est,est)
                            #print (dic_usuarios)
                            print ("\n\n\n\n\n\nYa fue agregado el nuevo usuario")
                            ava = False
                            while ava != True: #pregunta si se quierer continuar validado con 0
                                ava = Error("\nVolver al menu anterior, presiona [ 0 ]")
                                if ava != 0:
                                    print ("Valor invalido reintentar\n\n")
                                else:
                                    ava = True   
                        elif avanzar == 2:# en caso de que usuario queira editar un canridad de la linea de usuario
                            print ("\n\n")
                            for i in dic_usuarios.keys():# repite imprimeito todos los usuarios registrados
                                print (i," --> ",dic_usuarios[i][0])
                            doc = "1" # da un valor a doc para ingresar en forma de variable
                            while len(doc) < 10:
                                doc = str(Error("\n\nIngrese el Documento a editar"))
                                if len(doc) < 10:
                                    print ("\n\n\nValor invalido, Reingrese")
                                elif doc in dic_usuarios.keys():
                                    print ("")
                                else:
                                    print ("\n\n\nDocumento NO esta en la base de datos")
                                    doc = "1"
                            dato = dic_usuarios[doc] #BUsca el valor de documetno en caso de que este no sea variable
                            name = dato[0]
                            pas = dato[1]
                            tip = dato[2]
                            edi = 0
                            while edi == 0:#pregunta que accion desea hacer espesificamente el usuario su editar la contraseña o el nombre o el tipo de usuario
                                edi = Error("\n\n\nQue desea editar ?\n\n\t1) El nombre\n\n\t2) La contraseña\n\n\t3) El tipo de usuario")
                                if edi > 3 or edi <= 0:
                                    print ("\n\nValor inconcluso Reintente")
                                    edi = 0
                                elif edi == 1:
                                    print ("\n\nEditar nombre  ",name.upper())
                                    print ("\n\nIngrese nuevo Nombre")
                                    name = input(" --> ")
                                    dato[0] = name
                                elif edi == 2:
                                    for a in range (4):#otorga la posibilidad de ignresar la contrasela cuatro veses en caso de reinsidecia en fallos
                                        print ("Ingrese la contraseña, tiene 4 intentos")
                                        con = input(" -- >")#ingreso de contraseña para covalidar la infromacion que me otrogan 
                                        if con == pas:
                                            print ("\n\nEdita contraseña  ",pas.upper())
                                            print ("\n\nIngrese nueva Contraseña")
                                            pas = input(" --> ")
                                            dato[1] = pas
                                            break
                                        else:
                                            print ("\n\nReingrese")
                                elif edi == 3:# en caso de que se queira editar el tipo de usuario al que pertenesco
                                    print ("\n\nEdita tipo de Usuario  ",tip.upper())
                                    ti = 3
                                    while ti != 1 and ti != 2:#Nos permite seleccioanr el tipo de ususario para mejorar 
                                        ti = Error("Seleccione el tipo de usuario\n\n\n\t1) Administrador\n\n\t2) Operador")
                                        if ti != 1 and ti != 2:
                                            print ("\n"*224)
                                            print ("Valor invalido reintentar")
                                    if ti == 1:#en caso del dato acteriormete asiga un valor a tip
                                        tip = "Administrador"
                                    elif ti == 2:
                                        tip = "Operador"
                                    dato[2] = tip
                            dic_usuarios[doc] = dato
                            #guarda la informacion para continuar trabajando
                            dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est = save(dic_usuarios,lista_municipios,dic_est,est)
                            print ("\n"*224)
                            print ("Edicion completada\n\n")
                            ava = False
                        elif avanzar == 3:#en caso de que el administrador quiera eliminar a un usuario
                            print ("\n\n")
                            for i in dic_usuarios.keys(): # imprimer todos los usuarios
                                print (i," --> ",dic_usuarios[i][0])
                            doc = "1"
                            while len(doc) < 10:#nos pide ingresar un valro real de un usuario dentro de la lista para poder eliminarlo
                                doc = str(Error("\n\nIngrese el Documento a eliminar"))
                                if len(doc) < 10:
                                    print ("\n\n\nValor invalido, Reingrese")
                                elif doc in dic_usuarios.keys():
                                    print ("")
                                else:
                                    print ("\n\n\nDocumento NO esta en la base de datos")
                                    doc = "1"
                            del dic_usuarios[doc] #directaemnte elimina el usuario  
                            #guarda la informacon en los documentos
                            dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est = save(dic_usuarios,lista_municipios,dic_est,est)
                            print ("\n"*224)
                            print ("Edicion completada\n\n") #imprime que la edicion ha sido completanda
                            ava = False
                    ava = True
        elif tipo == "Operador":# en caso de que le usuario sea un oeprador
            ava = True
            while ava == True:
                for i in dic_municipios.keys(): # imprime la lista de muicipios y le dje aesoger solo un municipio
                    if i < 10 : #el valor debe estar dentro den rango requerido
                        print (i," => ",dic_municipios[i][0])
                    else:
                        print (i,"=> ",dic_municipios[i][0])
                muni = Error("\n\nEscoger municipio (solo puedes escoger uno)\n\n[ 0 ] si quieres volver al menu principla")
                if muni == 0:
                    ava = False
                elif muni < i+1:
                    if len(dic_muni[muni][1]) == 0: # si dicho municipio no tiene estaciones registradas
                        print ("\n"*224)
                        print ("\n\n▓▓▓▓▓ El municipio de "+dic_muni[muni][0].upper()+" NO tiene estaciones registradas ▓▓▓▓▓\n\n")
                        print ("Reingrese el municipio\n")
                    else:#en caso de que municipi si tenga estaciones registradas
                        ava = 0 
                        while ava == 0:
                            print ("\n\nEl municipio de "+dic_muni[muni][0].upper()+" tiene las siguientes estaciones :")
                            for i in dic_muni[muni][1].keys():
                                print ("\n",i,"--> ",dic_muni[muni][1][i][0])
                            esta = Error(("\n\n\t1) Escoger estacion\n\n\t2) Volver a escoger municipio"))
                            if esta > 2 or esta <= 0:#valida que se desa esciger la estacion o volver al menu prinsipal
                                print ("\n"*224)
                                print ("Valor inconcluso reingrese\n")
                            elif esta == 2:
                                ava = True
                            elif esta == 1:
                                esta = 0
                                print ("\n"*224)
                                while esta == 0:# define la estacion en la que estamos trabajadno
                                    for i in dic_muni[muni][1].keys():
                                        print ("\n",i,"--> ",dic_muni[muni][1][i][0])
                                    esta = Error("")
                                    if esta > i + 1 or esta <= 0:#si dicha estacion no esta dentro el rango imprime este comentario
                                        print ("\n"*224)
                                        print ("\n\nValor fuera de rango")
                                        esta = 0
                                    else:#si la estacion si esta dentro del rango
                                        ubi = esta
                                        print ("\n"*224)
                                        ava = 0
                                        while ava == 0:#pregunta que accion queremos realizar si ingresar o listar dicha estacion
                                            ava = Error("Que accion desea realizar\n\n\t1) Listar medidas\n\n\t2) Ingresar medidas\n\n\t3) Volver a ingresar estacion")
                                            print ("\n"*224)
                                            if ava > 3 or ava <= 0:
                                                print ("\n\nValor fuera del rango")
                                                ava = 0
                                            elif ava == 1:#en caos de que queramos listar
                                                print ("\n\n La informacion es del municipio de ",dic_muni[muni][0].upper()," para la estacion de ",dic_muni[muni][1][esta][0].upper(),"\n\n")
                                                texto = ["   PM10 "," PM2.5 ","Temp","Humedad"]#posibles cantidades de datos
                                                tex = ["   μg/m³","μg/m³"," °C ","  %   "]
                                                imp = ""
                                                sep = ""
                                                val = [1,2,3,4]
                                                for i in val:#toma las valores completas val para el trabajo completo
                                                    """
                                                    for que se repite para agregar un menu de texto que nos diga cuales 
                                                    variable estamos analindo
                                                    """
                                                    imp = imp+texto[i-1]+" "
                                                    sep = sep+tex[i-1]+"  " 
                                                print ("                      "+imp)
                                                print ("                      "+sep,end="\n\n")
                                                st = dic_municipios[muni][0]
                                                estacion = dic_muni[muni][1][ubi][0]
                                                st = (estacion+","+st)
                                                for i in dic_est:#averigua a que estacion pertene en el dic_est
                                                    if dic_est[i] == st:
                                                        estac = i
                                                for i in est[estac]:
                                                    st = est[estac][i]
                                                    st = st[1:-1]
                                                    lista = []
                                                    for h in range (4):
                                                        pos = st.find(",")
                                                        lista.append(float(st[:pos]))
                                                        st = st[pos+1:]
                                                    print (i,"    ",lista)#imprime la lista correspondiete al valor
                                                print ("\n\n\nDesea volver al menu anterior")
                                                ava = 24 # para seleccioanr la continuidad
                                                while ava == 24:
                                                    ava = Error("\n\n\nPresiona [ 0 ] para volver al menu anterior")
                                                    if ava == 0:
                                                        print ("\n"*224)
                                                        ava = 0
                                                    else: # en caso de que el valor de continua este fuera del rango
                                                        print ("\n"*224)
                                                        print ("Valor fuera del rango\n\n")
                                                        ava = 24
                                            elif ava == 2:#en caso de que el usuario queira ingresar datos
                                                while ava == 2:
                                                    print ("\n\n Para el municipio de ",dic_muni[muni][0].upper()," para la estacion de ",dic_muni[muni][1][esta][0].upper(),"\n\n")
                                                    now = datetime.datetime.now()
                                                    now = now.strftime("%Y-%m-%d %T")
                                                    print ("Con un codigo que es la siguiente fecha y hora = ",now)
                                                    conti = 0
                                                    while conti == 0:#repite para el ingreso de pm10
                                                        #debe retornar un valor de tipo flotante
                                                        pm10 = Error_float("\n\nIngrese el valor para PM 10 , el valor debe estar en μg/m³\ndentro de un rango de [ 0.0 : 100.0 ]\nEn caso de no tener registro PM 10 ingresar [ ND] o -999")
                                                        if pm10 == -999 or pm10 <= 100 and pm10 >= 0:
                                                            conti = 1
                                                        else:
                                                            print ("\n"*224)
                                                            print ("Valor fuera del rango\n")
                                                    pm10 = str(pm10)#vuelve eld ato ingresado que es de tipo flotate una cadena de caracteres
                                                    conti = 0
                                                    while conti == 0:# trabaja para el ingreso de pm25
                                                        #debe retornar un valro de tipo flotante
                                                        pm25 = Error_float("\n\nIngrese el valor para PM 2.5 , el valor debe estar en μg/m³\ndentro de un rango de [ 0.0 : 200.0 ]\nEn caso de no tener registro PM 2.5 ingresar [ ND] o -999")
                                                        if pm25 == -999 or pm25 <= 200 and pm25 >= 0:
                                                            conti = 1
                                                        else:
                                                            print ("\n"*224)
                                                            print ("Valor fuera del rango\n")
                                                    pm25 = str(pm25) #convierte a str el valor float de pm25
                                                    conti = 0
                                                    while conti == 0:#trabaja para le ingreso de tem
                                                        tem = Error_float("\n\nIngrese el valor para la TEMPERATURA , el valor debe estar en grados [ °C ]\ndentro de un rango de [ -20.0 : 50.0 ]\nEn caso de no tener registro TEMPERATURA ingresar [ ND] o -999")
                                                        if tem == -999 or tem <= 50 and tem >= -20:
                                                                conti = 1
                                                        else:
                                                            print ("\n"*224)
                                                            print ("Valor fuera del rango\n")
                                                    tem = str(tem)#conierte a str el valor de tem
                                                    conti = 0
                                                    while conti == 0:#trabaja con el valor de hum
                                                        hum = Error_float("\n\nIngrese el valor para la HUMEDAD , el valor debe estar en porcentaje [ % ]\ndentro de un rango de [ 0.0 : 100.0 ]\nEn caso de no tener registro de HUMEDAD ingresar [ ND] o -999")
                                                        if hum == -999 or hum <= 100 and hum >= 0:
                                                                conti = 1
                                                        else:
                                                            print ("\n"*224)
                                                            print ("Valor fuera del rango\n")
                                                    hum = str(hum)# crea una cadena de caracteres el valor de hum
                                                    st = dic_municipios[muni][0]
                                                    estacion = dic_muni[muni][1][ubi][0]
                                                    st = (estacion+","+st)#forma la lista segun al esatcion que se solicita
                                                    for i in dic_est:
                                                        if dic_est[i] == st:
                                                            estac = i#conocemos e estacion estamos trabajado en el diccionario dic_est
                                                    est[estac][now]= ("{"+pm10+","+pm25+","+tem+","+hum+"}")#imprime dicho vlaor en el diccioanrio est
                                                    ava = 24
                                                    #guarda toda la infomraicon el documento
                                                    dic_municipios,dic_muni,dic_usuarios,lista_municipios,dic_est,est = save(dic_usuarios,lista_municipios,dic_est,est)
                                                    print ("\n"*224)
                                                    while ava == 24:#preungta la continuidad
                                                        ava = Error("Que desea hacer\n\n\t1) Volver al menu anterior\n\n\t2) Ingresar otra medida")
                                                        if ava > 2 or ava <= 0:
                                                            print ("\n"*224)
                                                            print ("Valor fuera del rango\n\n")
                                                            ava = 24
                                                        elif ava == 1:
                                                            ava = 0
                                                    print ("\n"*224)
                                            elif ava == 3:#con valida enc aso de que de que se quiera volver al menu anterior
                                                ava = 1
                                        if ava == 1:#convalida enc asod e que se quiera volver al menu de selecicon de municipio
                                            ava = 0
        else:
            print ("\n\nValor fuera del rango\n\n")#en caso de que el valro este duera del rango de type
    return ava#retorna el valro de ava como falso en ambos casos
#tipo =  "Operador"
#s  = registrado(tipo,Error,Error_float,dic_usuarios,dic_municipios,dic_muni,est,dic_est,lista_municipios,save)