def listarCursos(cursos):
    print ("Cursos")
    contador = 1
    for cur in cursos:
        datos = "{0}. Codigo: {1} | Nombre: {2} ({3}creditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
        print ("  ")

def pedirDatosRegistro():
    codigoCorrecto = False
    while (not codigoCorrecto):
        codigo=input("Ingrese codigo:")
        if len (codigo)==6:
            codigoCorrecto = True
        else:
            print("Código incorrecto")
    nombre=input("Ingrese nombre:")
    creditosCorrecto=False
    while(not  creditosCorrecto):
        creditos= (input ("ingrese creditos"))
        if creditos.isnumeric():
            creditosCorrecto= True
            creditos = int (creditos)
        else:
            print ("creditos incorrectos")
        curso = (codigo, nombre, creditos)
    return curso

def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del curso a eliminar: ")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break
    
    if not existeCodigo:
        codigoEliminar = ""
    return codigoEliminar
