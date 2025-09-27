titulos = []
ejemplares = []

opcion = 0

while opcion != 8:
    entrada = input("\n--- Ingrese el número de la acción que desea realizar --- \n1. Ingresar títulos \n2. Ingresar ejemplares \n3. Mostrar el catálogo de libros \n4. Consultar disponibilidad \n5. Lista de libros agotados \n6. Agregar un nuevo libro \n7. Actualizar ejemplares \n8. Salir del menú \n")

    if entrada.isdigit():
        opcion = int(entrada)
    else:
        opcion = 0

    match opcion:
        #1. Ingresar títulos
        case 1:
            titulo = input("Ingresar el título: ")

            #Si el título ya se encuentra en títulos o el usuario no ingresó nada, le aparece un mensaje indicandole que vuelva a escribirlo
            while titulo in titulos or titulo == "":
                titulo = input("El título esta repetido o en blanco, por favor ingrese el título nuevamente: ")
            
            #Muestra el título ingresado y lo agrega a la lista
            print(f"El título ingresado es: {titulo}")
            titulos.append(titulo)
            posicion = titulos.index(titulo)
            ejemplares.insert(posicion, 0)
        
        #2. Ingresar ejemplares
        case 2:
            #Si no existe ningún título, le sale un mensaje al usuario
            if not titulos:
                print("No existe ningún título en el catálogo. Primero ingrese un título en la opción 1 o 6 del menú si desea ingresar cantidad de ejemplares.")
                continue

            print("\n-- Nuestro catálogo --")
            for i, titulo in enumerate(titulos):
                print(f"{i + 1}- {titulo}")
            
            while True:
                entrada = input("\nSeleccione el número del título que desea para ingresar ejemplares: ")

                #Valida que el usuario ingrese al menos algo, evitando que solo presione "Enter"
                if not entrada.isdigit():  
                    print("\nDebe ingresar un número válido.")
                    continue
                
                posicion = int(entrada) - 1

                #Valida que se encuentre dentro del rango de nuestra lista
                if 0 <= posicion < len(titulos):   
                    break
                else:
                    print("\nPosición inválida. Seleccione el número del título correctamente.")

            #Pedir cantidad de ejemplares con validación
            while True:
                entrada = input("\nIngrese la cantidad de ejemplares que desea agregar: ")
                if not entrada.isdigit():
                    print("Debe ingresar un número válido.")
                    continue
                cantidad = int(entrada)
                break

            #Actualización de ejemplares
            ejemplares[posicion] += cantidad
            print(f"\nEjemplares disponibles para: {titulos[posicion]} --> {ejemplares[posicion]}")
        
        #3. Mostrar el catálogo de libros
        case 3:
            if not titulos:
                print("No existe ningún título en el catálogo. Primero ingrese un título en la opción 1 o 6 del menú si desea ver nuestro catálogo.")
                continue

            print("\n-- Nuestro catálogo --")

            for i in range(len(titulos)):
                print(f"Libro: '{titulos[i]}' - Stock: {ejemplares[i]}")
        
        #4. Consultar disponibilidad
        case 4:
            if not titulos:
                print("No existe ningún título en el catálogo. Primero ingrese un título en la opción 1 o 6 del menú si desea consultar nuestra disponibildad")
                continue

            print("\nNuestros libros: ")
            for i, titulo in enumerate(titulos):
                print(f"- {titulo}")
            
            busqueda_titulo = input("\nIngrese el título que desea consultar: ").lower()

            volver_menu = "salir"   #Se crea una variable con la palabra que te permite volver al menú, para evitar que futuros cambios afecten al código
            while busqueda_titulo != volver_menu:

                #Si existe el título muestra el mensaje con los ejemplares que tiene y vuelve al menú
                if busqueda_titulo in titulos:
                    posicion = titulos.index(busqueda_titulo)
                    print(f"\nHay {ejemplares[posicion]} ejemplares disponibles, para el título: {busqueda_titulo}")
                    break

                #Si no existe el título muestra un mensaje y vuelve a habilitar la búsqueda
                else:
                    print(f"\nEl título: {busqueda_titulo} no se encuentra en nuestro catálogo.")
                    busqueda_titulo = input(f"Vuelva a ingresar un nombre válido. Si desea volver al menú escriba: {volver_menu}. ").lower()
        
        #5. Lista de libros agotados
        case 5:
            if not titulos:
                print("No existe ningún título en el catálogo. Primero ingrese un título en la opción 1 o 6 del menú si desea consultar nuestros agotados.")
                continue

            agotados = False    #Bandera

            #Recorro los ejemplares y con una bandera encuentro al menos uno con cero ejemplares
            for i in ejemplares:
                if i == 0:
                    agotados = True
                    break
            
            #Si la bandera fue verdadera, se muestran los libros agotados
            if agotados: 
                print("Libros agotados: ")
                for titulo in titulos:
                    posicion = titulos.index(titulo)
                    if ejemplares[posicion] == 0:
                        print(f"- {titulo}")
            else:
                print("En este momento no tenemos libros agotados.")

        
        #6. Agregar un nuevo libro
        case 6:
            nuevo_titulo = input("Ingresar un nuevo título: ")

            #Si el título ingresado ya existe o esta en blanco, le sale un mensaje al usuario para que lo ingrese correctamente
            while nuevo_titulo in titulos or nuevo_titulo == "":
                nuevo_titulo = input(f"El título: {nuevo_titulo} esta repetido o en blanco, por favor ingrese el título nuevamente: ").lower()
            
            titulos.append(nuevo_titulo)

            #Pedir cantidad de ejemplares con validación
            while True:
                entrada = input("\nIngrese la cantidad de ejemplares que desea agregar: ")

                #Se evita que el usuario ingrese un número no válido
                if not entrada.isdigit():
                    print("Usted ha ingresado un número inválido o cero ejemplares. Debe ingresar un número válido.")
                    continue
                cantidad = int(entrada)
                break

            #Si pasa la validación se agrega a la lista con su número de ejemplares y muestra un mensaje al usuario
            posicion = titulos.index(nuevo_titulo)
            ejemplares.insert(posicion, cantidad)
            print(f"El título: '{nuevo_titulo}' con {cantidad} ejemplares, ha sido agregado con éxito!")

        #7. Actualizar ejemplares (préstamo --> Disminuye en 1 la cantidad de ejemplares del libro seleccionado || devolución --> Aumenta en 1 la cantidad de ejemplares del libro seleccionado)
        case 7:
            if not titulos:
                print("No existe ningún título en el catálogo. Primero ingrese un título en la opción 1 o 6 del menú si desea realizar una actualización de ejemplares. ")
                continue

            #Muestro el catálogo para que el usuario elija
            print("\n -- Catálogo disponible --")
            for i, titulo in enumerate(titulos):
                print(f"{i + 1} - {titulo}")

            entrada = input("\nSeleccione el número del título que desea para actualizar ejemplares: \n(Si desea volver al menu escriba 'salir') ")

            while entrada != "salir" and (not entrada.isdigit() or int(entrada) < 1 or int(entrada) > len(titulos)):
                entrada = input("\nEntrada inválida. Ingrese un número válido o 'salir' para volver al menú. ")

                if entrada == "salir":
                    break
            
            if entrada == "salir":
                continue

            posicion = int(entrada) - 1

            accion = input("\n¿Qué acción desea realizar? Ingrese 'p' para préstamo o 'd' para devolución: \n(Ingrese 'salir' para volver al menú.) ").lower()

            while accion != "salir":
                match accion:
                    case "p":
                        if ejemplares[posicion] > 0:
                            ejemplares[posicion] -= 1
                            print(f"\nPrestamo realizado! Ejemplares disponibles para '{titulos[posicion]}' : {ejemplares[posicion]}")
                        else:
                            print(f"\nNo hay ejemplares disponibles de {titulos[posicion]}")
                    
                    case "d":
                        ejemplares[posicion] += 1
                        print(f"\nDevolución realizada! Ejemplares disponibles para '{titulos[posicion]}' : {ejemplares[posicion]}")

                    case _:
                        print("Acción inválida.")
                        
                accion = input("\n¿Qué acción desea realizar? ('p', 'd'). \n(Ingrese 'salir' para volver al menú.) ").lower()

        #8. Salir del menú
        case 8:
            print("Gracias por visitar nuestro sitio. Que vuelva pronto.")
        
        #Si el usuario no ingresa ninguna de las opciones disponibles en el menú
        case _:
            print("La opción ingresada es incorrecta.")
