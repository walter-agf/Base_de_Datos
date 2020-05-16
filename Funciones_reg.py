import os
import datetime
from Funciones_dic import dic_1,dic_2,dic_usu
from Funciones_ini import Error
directorio_actual = os.getcwd()
directorio = (directorio_actual+"/Base")
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
def registrado(directorio,tipo,Error,Error_float,dic_1,dic_2,dic_usu):
    ava = True
    while ava == True:
        if tipo == "Administrador":
            while ava == True:
                conti = 0
                while conti == 0:
                    conti = Error("Que accion desea realizar\n\n\n\t1) Gestionar estaciones\n\n\t2) Gestionar Usuario\n\n\t3) Volver al menu principal")
                    if conti > 3 or conti <= 0:
                        print ("\n"*224)
                        print ("Valor Fuera del rango")
                        conti = 0
                if conti == 3:
                    ava = False
                elif conti == 1 :
                    avanzar = 0
                    print ("\n"*224)
                    while avanzar == 0:
                        avanzar = Error("¿ Que accion desea hacer ?\n\n\n\t1) Crear estacion\n\n\t2) Editar estacion\n\n\t3) Eliminar estacion")
                        if avanzar > 3 or avanzar <= 0:
                            print ("\n"*224)
                            print ("Valor inconcluso Reingrese\n\n")
                            avanzar = 0
                    if avanzar == 1:
                        dic_municipios = dic_1(directorio)
                        print ("\n\n")
                        muni = 0
                        while muni == 0:
                            for i in dic_municipios.keys():
                                if i < 10 :
                                    print (i," => ",dic_municipios[i][0])
                                else:
                                    print (i,"=> ",dic_municipios[i][0])
                            muni = Error("\n\nSeleccione en que municipio quieres crear la estacion")
                            if muni > i or muni <= 0:
                                print ("\n"*224)
                                print ("Valor fuera del rango\n")
                                muni  = 0
                        print ("\n"*224)
                        dic_municipios = dic_2(directorio,dic_municipios)
                        if len(dic_municipios[muni][1]) == 0:
                            print ("El municipio ",dic_municipios[muni][0].upper(),"No tiene estaciones registradas")
                            i = 0
                        else:
                            for i in dic_municipios[muni][1]:
                                print (i," --> ",dic_municipios[muni][1][i][0])
                        print ("\n\n\nIngrese el nombre de la nueva estacion")
                        i = i + 1
                        esta = input("---> ")
                        x = open(directorio+"/estaciones.txt","a")
                        st = str(muni)
                        st = (st+","+esta+"\n")
                        #print (x.read())
                        x.write(st)
                        x.close()
                        print ("\n\n\n\n\n\nYa fue agregada la nueva estacion")
                        print ("Recuerda que se agrega en la ultima posicon de estacion disponible para el municipio")
                        ava = False
                        while ava != True: 
                            ava = Error("\nVolver al menu anterior, presiona [ 0 ]")
                            if ava != 0:
                                print ("Valor invalido reintentar\n\n")
                            else:
                                ava = True
                    elif avanzar == 2 :
                        dic_municipios = dic_1(directorio)
                        print ("\n\n")
                        muni = 0
                        while muni == 0:
                            for i in dic_municipios.keys():
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
                        dic_municipios = dic_2(directorio,dic_municipios)
                        if len(dic_municipios[muni][1]) == 0:
                            print ("El municipio ",dic_municipios[muni][0].upper(),"No tiene estaciones registradas")
                            i = 0
                        else:
                            for i in dic_municipios[muni][1]:
                                print (i," --> ",dic_municipios[muni][1][i][0])
                            esta = 0
                            while esta == 0:
                                esta = Error("\n\nSeleccione la estacion a editar")
                                if esta > i or esta <= 0:
                                    print ("Valor fuera del rango Reingresar")
                                    esta = 0
                            print ("\n\nPara la estacion ",end = "\t")
                            print (dic_municipios[muni][1][esta][0].upper())
                            print ("\n\nComo desea renombrar la estacion ? ")
                            name = input(" --> ")
                            name = (name+"\n")
                            x = open(directorio+"/estaciones.txt","r")
                            lis = x.readlines()
                            for a in range (len(lis)):
                                lis[a] = lis[a][:-1]
                            x.close()
                            w = open(directorio+"/estaciones.txt","w")
                            w.close()
                            s = open(directorio+"/estaciones.txt","a")
                            for i in lis:
                                pos = i.find(",")
                                mu = i[:pos]
                                a = i
                                a = (a+"\n")
                                i = i[pos+1:]
                                if int(mu) == muni:
                                    if i == dic_municipios[muni][1][esta][0]:
                                       name = (mu+","+name)
                                       s.write(name)
                                    else:
                                       s.write(a)
                                else:
                                    s.write(a)                        
                            s.close()
                            print ("\n"*224)
                            print ("Edicion completada\n\n")
                    elif avanzar == 3 :
                        dic_municipios = dic_1(directorio)
                        print ("\n\n")
                        muni = 0
                        while muni == 0:
                            for i in dic_municipios.keys():
                                if i < 10 :
                                    print (i," => ",dic_municipios[i][0])
                                else:
                                    print (i,"=> ",dic_municipios[i][0])
                            muni = Error("\n\nSeleccione en que municipio quieres eliminar la estacion")
                            if muni > i or muni <= 0:
                                print ("\n"*224)
                                print ("Valor fuera del rango\n")
                                muni  = 0
                        print ("\n"*224)
                        dic_municipios = dic_2(directorio,dic_municipios)
                        if len(dic_municipios[muni][1]) == 0:
                            print ("El municipio ",dic_municipios[muni][0].upper(),"No tiene estaciones registradas")
                            i = 0
                        else:
                            for i in dic_municipios[muni][1]:
                                print (i," --> ",dic_municipios[muni][1][i][0])
                            esta = 0
                            while esta == 0:
                                esta = Error("\n\nSeleccione la estacion a Eliminar")
                                if esta > i or esta <= 0:
                                    print ("Valor fuera del rango Reingresar")
                                    esta = 0
                            x = open(directorio+"/estaciones.txt","r")
                            lis = x.readlines()
                            for a in range (len(lis)):
                                lis[a] = lis[a][:-1]
                            x.close()
                            w = open(directorio+"/estaciones.txt","w")
                            w.close()
                            s = open(directorio+"/estaciones.txt","a")
                            for i in lis:
                                pos = i.find(",")
                                mu = i[:pos]
                                a = i
                                i = i+"\n"
                                if int(mu) == muni:
                                    pos = i.find(",")
                                    a = a[pos+1:]
                                    if a == dic_municipios[muni][1][esta][0]:
                                        print ("")
                                    else:
                                       s.write(i)
                                else:
                                    s.write(i)                        
                            s.close()
                            print ("\n"*224)
                            print ("Edicion completada\n\n")
                elif conti == 2 :
                    while ava == True:
                        avanzar = 0
                        print ("\n"*224)
                        while avanzar == 0:
                            avanzar = Error("¿ Que accion desea hacer ?\n\n\n\t1) Crear Usuario\n\n\t2) Editar Usuario\n\n\t3) Eliminar Usuario")
                            if avanzar > 3 or avanzar <= 0:
                                print ("\n"*224)
                                print ("Valor inconcluso Reingrese\n\n")
                                avanzar = 0
                        if avanzar == 1:
                            dic_usuarios = dic_usu(directorio)
                            print ("\n\n")
                            for i in dic_usuarios.keys():
                                print (i," --> ",dic_usuarios[i][0])
                            doc = "1"
                            while len(doc) < 10:
                                print ("\nIngrese usuario debe ser un numero y tener minimo 10 caracteres")
                                doc = str(Error("Ingrese el Documento"))
                                if len(doc) < 10:
                                    print ("\n\n\nValor invalido, Reingrese")
                                elif doc in dic_usuarios.keys():
                                    print ("\n\n\nDocumento ya esta en la base de datos")
                                    doc = "1"
                            lis = (doc+",")
                            print ("Ingrese el nombre del usuario")
                            name = input("--> ")
                            lis = (lis+name+",")
                            pas = "1"
                            while len(pas) < 4:
                                print ("\nIngrese la contraseña de usuario debe tener minimo 4 caracteres")
                                pas = input(" --> ")
                                if len(pas) < 4:
                                    print ("\n\n\nValor invalido, Reingrese")
                            lis = (lis+pas+",")
                            print("\n"*224)
                            ti = 3
                            while ti != 1 and ti != 2:
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
                            x = open(directorio+"/usuarios.txt","a")
                            x.write(lis)
                            x.close()
                            print ("\n\n\n\n\n\nYa fue agregado el nuevo usuario")
                            ava = False
                            while ava != True: 
                                ava = Error("\nVolver al menu anterior, presiona [ 0 ]")
                                if ava != 0:
                                    print ("Valor invalido reintentar\n\n")
                                else:
                                    ava = True   
                        elif avanzar == 2:
                            dic_usuarios = dic_usu(directorio)
                            print ("\n\n")
                            for i in dic_usuarios.keys():
                                print (i," --> ",dic_usuarios[i][0])
                            doc = "1"
                            while len(doc) < 10:
                                doc = str(Error("\n\nIngrese el Documento a editar"))
                                if len(doc) < 10:
                                    print ("\n\n\nValor invalido, Reingrese")
                                elif doc in dic_usuarios.keys():
                                    print ("")
                                else:
                                    print ("\n\n\nDocumento NO esta en la base de datos")
                                    doc = "1"
                            x = open(directorio+"/usuarios.txt","r")
                            lis = x.readlines()
                            for a in range (len(lis)):
                                lis[a] = lis[a][:-1]
                            x.close()
                            w = open(directorio+"/usuarios.txt","w")
                            w.close()
                            s = open(directorio+"/usuarios.txt","a")
                            for i in lis:
                                pos = i.find(",")
                                do = i[:pos]
                                a = i
                                a = (a+"\n")
                                i = i[pos+1:]
                                if do == doc:
                                    pos = i.find(",")
                                    name = i[:pos]
                                    i = i[pos+1:]
                                    pos = i.find(",")
                                    pas = i[:pos]
                                    tip = i[pos+1:]
                                    edi = 0
                                    while edi == 0:
                                        edi = Error("\n\n\nQue desea editar ?\n\n\t1) El nombre\n\n\t2) La contraseña\n\n\t3) El tipo de usuario")
                                        if edi > 3 or edi <= 0:
                                            print ("\n\nValor inconcluso Reintente")
                                        elif edi == 1:
                                            print ("\n\nEditar nombre  ",name.upper())
                                            print ("\n\nIngrese nuevo Nombre")
                                            name = input(" --> ")
                                        elif edi == 2:
                                            for a in range (4):
                                                print ("Ingrese la contraseña, tiene 4 intentos")
                                                con = input(" -- >")
                                                if con == pas:
                                                    print ("\n\nEdita contraseña  ",pas.upper())
                                                    print ("\n\nIngrese nueva Contraseña")
                                                    pas = input(" --> ")
                                                    break
                                                else:
                                                    print ("\n\nReingrese")
                                        elif edi == 3:
                                            print ("\n\nEdita tipo de Usuario  ",tip.upper())
                                            ti = 3
                                            while ti != 1 and ti != 2:
                                                ti = Error("Seleccione el tipo de usuario\n\n\n\t1) Administrador\n\n\t2) Operador")
                                                if ti != 1 and ti != 2:
                                                    print ("\n"*224)
                                                    print ("Valor invalido reintentar")
                                            if ti == 1:
                                                tip = "Administrador"
                                            elif ti == 2:
                                                tip = "Operador"
                                    a =(doc+","+name+","+pas+","+tip+"\n")
                                    s.write(a)
                                else:
                                    s.write(a)                        
                            s.close()
                            print ("\n"*224)
                            print ("Edicion completada\n\n")
                            ava = False
                        elif avanzar == 3:
                            dic_usuarios = dic_usu(directorio)
                            print ("\n\n")
                            for i in dic_usuarios.keys():
                                print (i," --> ",dic_usuarios[i][0])
                            doc = "1"
                            while len(doc) < 10:
                                doc = str(Error("\n\nIngrese el Documento a eliminar"))
                                if len(doc) < 10:
                                    print ("\n\n\nValor invalido, Reingrese")
                                elif doc in dic_usuarios.keys():
                                    print ("")
                                else:
                                    print ("\n\n\nDocumento NO esta en la base de datos")
                                    doc = "1"
                            x = open(directorio+"/usuarios.txt","r")
                            lis = x.readlines()
                            for a in range (len(lis)):
                                lis[a] = lis[a][:-1]
                            x.close()
                            w = open(directorio+"/usuarios.txt","w")
                            w.close()
                            s = open(directorio+"/usuarios.txt","a")
                            for i in lis:
                                pos = i.find(",")
                                do = i[:pos]
                                i = (i+"\n")
                                if do != doc:
                                    s.write(i)                        
                            s.close()
                            print ("\n"*224)
                            print ("Edicion completada\n\n")
                            ava = False
                    ava = True
        elif tipo == "Operador":
            ava = True
            while ava == True:
                dic_municipios = dic_1(directorio)
                for i in dic_municipios.keys():
                    if i < 10 :
                        print (i," => ",dic_municipios[i][0])
                    else:
                        print (i,"=> ",dic_municipios[i][0])
                muni = Error("\n\nEscoger municipio (solo puedes escoger uno)\n\n[ 0 ] si quieres volver al menu principla")
                if muni == 0:
                    ava = False
                elif muni < i+1:
                    dic_municipios = dic_2(directorio, dic_municipios)
                    if len(dic_municipios[muni][1]) == 0:
                        print ("\n"*224)
                        print ("\n\n▓▓▓▓▓ El municipio de "+dic_municipios[muni][0].upper()+" NO tiene estaciones registradas ▓▓▓▓▓\n\n")
                        print ("Reingrese el municipio\n")
                    else:
                        ava = 0 
                        while ava == 0:
                            print ("\n\nEl municipio de "+dic_municipios[muni][0].upper()+" tiene las siguientes estaciones :")
                            for i in dic_municipios[muni][1].keys():
                                print ("\n",i,"--> ",dic_municipios[muni][1][i][0])
                            esta = Error(("\n\n\t1) Escoger estacion\n\n\t2) Volver a escoger municipio"))
                            if esta > 2 or esta <= 0:
                                print ("\n"*224)
                                print ("Valor inconcluso reingrese\n")
                            elif esta == 2:
                                ava = True
                            elif esta == 1:
                                ava = 0
                                print ("\n"*224)
                                while ava == 0:
                                    for i in dic_municipios[muni][1].keys():
                                        print ("\n",i,"--> ",dic_municipios[muni][1][i][0])
                                    ava = Error("")
                                    if ava > i + 1 or ava <= 0:
                                        print ("\n"*224)
                                        print ("\n\nValor fuera de rango")
                                        ava = 0
                                    else:
                                        print ("\n"*224)
                                        ava = 0
                                        while ava == 0:
                                            ava = Error("Que accion desea realizar\n\n\t1) Listar medidas\n\n\t2) Ingresar medidas\n\n\t3) Volver a ingresar estacion")
                                            print ("\n"*224)
                                            if ava > 3 or ava <= 0:
                                                print ("\n\nValor fuera del rango")
                                                ava = 0
                                            elif ava == 1:
                                                print ("\n\n La informacion es del municipio de ",dic_municipios[muni][0].upper()," para la estacion de ",dic_municipios[muni][1][esta][0].upper(),"\n\n")
                                                texto = ["   PM10 "," PM2.5 ","Temp","Humedad"]#posibles cantidades de datos
                                                tex = ["   μg/m³","μg/m³"," °C ","  %   "]
                                                imp = ""
                                                sep = ""
                                                val = [1,2,3,4]
                                                for i in val:
                                                    """
                                                    for que se repite para agregar un menu de texto que nos diga cuales 
                                                    variable estamos analindo
                                                    """
                                                    imp = imp+texto[i-1]+" "
                                                    sep = sep+tex[i-1]+"  " 
                                                print ("                      "+imp)
                                                print ("                      "+sep,end="\n\n")
                                                x = open(directorio+"/ingreso.txt","r")
                                                for i in x:
                                                    pos = i.find(",")
                                                    m = int(i[:pos])
                                                    if muni == m:
                                                        i = i[pos+1:]
                                                        pos = i.find(";")
                                                        m = int(i[:pos])
                                                        if esta == m:
                                                            i = i[pos+1:]
                                                            pos = i.find(",")
                                                            a = i[pos+1:]
                                                            a = a[1:-1]
                                                            lista = []
                                                            for s in range(4):
                                                                ubi = a.find(",")
                                                                val = float(a[:ubi])
                                                                lista.append(val)
                                                                a = a[ubi+1:]
                                                            print (i[:pos],"    ",lista)
                                                x.close()
                                                print ("\n\n\nDesea volver al menu anterior")
                                                ava = 0
                                                while ava == 0:
                                                    ava = Error("\n\n\nPresiona [ 0 ] para volver al menu anterior")
                                                    if ava == 0:
                                                        print ("\n"*224)
                                                        ava = 1
                                                    else:
                                                        print ("\n"*224)
                                                        print ("Valor fuera del rango\n\n")
                                                        ava = 0
                                            elif ava == 2:
                                                while ava == 2: 
                                                    x = open(directorio+"/ingreso.txt","a")
                                                    print ("\n\n Para el municipio de ",dic_municipios[muni][0].upper()," para la estacion de ",dic_municipios[muni][1][esta][0].upper(),"\n\n")
                                                    now = datetime.datetime.now()
                                                    now = now.strftime("%Y-%m-%d %T")
                                                    print ("Con un codigo que es la siguiente fecha y hora = ",now)
                                                    conti = 0
                                                    while conti == 0:
                                                        pm10 = Error_float("\n\nIngrese el valor para PM 10 , el valor debe estar en μg/m³\ndentro de un rango de [ 0.0 : 100.0 ]\nEn caso de no tener registro PM 10 ingresar [ ND] o -999")
                                                        if pm10 == -999 or pm10 <= 100 and pm10 >= 0:
                                                            conti = 1
                                                        else:
                                                            print ("\n"*224)
                                                            print ("Valor fuera del rango\n")
                                                    pm10 = str(pm10)
                                                    conti = 0
                                                    while conti == 0:
                                                        pm25 = Error_float("\n\nIngrese el valor para PM 2.5 , el valor debe estar en μg/m³\ndentro de un rango de [ 0.0 : 200.0 ]\nEn caso de no tener registro PM 2.5 ingresar [ ND] o -999")
                                                        if pm25 == -999 or pm25 <= 200 and pm25 >= 0:
                                                            conti = 1
                                                        else:
                                                            print ("\n"*224)
                                                            print ("Valor fuera del rango\n")
                                                    pm25 = str(pm25)
                                                    conti = 0
                                                    while conti == 0:
                                                        tem = Error_float("\n\nIngrese el valor para la TEMPERATURA , el valor debe estar en grados [ °C ]\ndentro de un rango de [ -20.0 : 50.0 ]\nEn caso de no tener registro TEMPERATURA ingresar [ ND] o -999")
                                                        if tem == -999 or tem <= 50 and tem >= -20:
                                                                conti = 1
                                                        else:
                                                            print ("\n"*224)
                                                            print ("Valor fuera del rango\n")
                                                    tem = str(tem)
                                                    conti = 0
                                                    while conti == 0:
                                                        hum = Error_float("\n\nIngrese el valor para la HUMEDAD , el valor debe estar en porcentaje [ % ]\ndentro de un rango de [ 0.0 : 100.0 ]\nEn caso de no tener registro de HUMEDAD ingresar [ ND] o -999")
                                                        if hum == -999 or hum <= 100 and hum >= 0:
                                                                conti = 1
                                                        else:
                                                            print ("\n"*224)
                                                            print ("Valor fuera del rango\n")
                                                    hum = str(hum)
                                                    mun = str(muni)
                                                    es = str(esta)
                                                    s = str(mun+","+es)
                                                    p = str(";"+now)
                                                    w = str(",["+pm10+","+pm25+","+tem+","+hum+"]\n")
                                                    g = (s+p+w)
                                                    print (g)
                                                    x.write(g)
                                                    x.close()
                                                    ava = 0
                                                    print ("\n"*224)
                                                    while ava == 0:
                                                        ava = Error("Que desea hacer\n\n\t1) Volver al menu anterior\n\n\t2) Ingresar otra medida")
                                                        if ava > 2 or ava <= 0:
                                                            print ("\n"*224)
                                                            print ("Valor fuera del rango\n\n")
                                                            ava = 0
                                                    print ("\n"*224)
                                            elif ava == 3:
                                                ava = 2
                                            if ava == 1:
                                                ava = 0
                                if ava == 2:
                                    ava = 0

        else:
            print ("\n\nValor fuera del rango\n\n")
    return ava
#tipo =  "Administrador"
#s  = registrado(directorio,tipo,Error,Error_float,dic_1,dic_2,dic_usu)