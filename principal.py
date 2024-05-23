from BD.conexion import DAO
import funciones

def menuPrincipal():
    continuar = True
    while (continuar):
        opcionCorrecta = False
        while (not opcionCorrecta):
            print("===========MENÚ PRINCIPAL=========")
            print("1. Listar cursos")
            print("2. Registrar cursos")
            print("3. Actualizar cursos")
            print("4. Eliminar cursos")
            print("5. Salir")
            print("==================================")
            opcion = int(input("Seleccione la opción: "))
            
            if opcion < 1 or opcion > 5:
                print("La opción es incorrecta, ingrese nuevamente")
            elif opcion == 5:
                continuar =False
                print ("Gracias por usar este sistema")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()
    if opcion == 1:
        try:
            cursos = dao.listarCursos()
            if len (cursos)> 0:
                funciones.listarCursos(cursos)
            else:
                print("No se encontraron cursos....")
        except:
                print ("Ocurrio un error")
    elif opcion == 2:
        curso = None
        try:
            dao.registrarCurso(curso)
        except:
            print ("Ocurrio un error")
        print ("registro")
    elif opcion == 3: 
        print ("Actualización")
    elif opcion == 4:
         try:
             cursos=dao.listarCursos()
             if len (cursos)> 0:
                 codigoEliminar=funciones.pedirDatosEliminacion(cursos)
                 if not (codigoEliminar == " "):
                    dao.eliminarCursos(codigoEliminar)
                else:
                    print("El código del curso no se encontro")
            else:
                print ("Opción no válida")
        except:
            print("Ocurrio un error")
    
                
    menuPrincipal()
