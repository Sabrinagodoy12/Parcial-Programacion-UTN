titulos = []
ejemplares = []

opcion = 0

while opcion != 8:
    opcion= int(input("\n--- Ingrese el número de la acción que desea realizar --- \n1. Ingresar títulos \n2. Ingresar ejemplares \n3. Mostrar el catálogo de libros \n4. Consultar disponibilidad \n5. Lista de libros agorados \n6. Agregar un nuevo libro \n7. Actualizar ejemplares \n8. Salir del menú \n"))
    
    match opcion:
        #1. Ingresar títulos.
        case 1:
            titulo = input("Ingresar el título: ")
            #Si el título ya se encuentra en títulos o el usuario no ingresó nada, le aparece un mensaje indicandole que vuelva a escribirlo.
            
            while titulo in titulos or titulo == "":
                titulo = input("El título esta repetido o en blanco, por favor ingrese el título nuevamente: ")
            
            #Muestra el título ingresado y lo agrega a la lista.
            print(f"El título ingresado es: {titulo}")
            titulos.append(titulo)
            posicion = titulos.index(titulo)
            ejemplares.insert(posicion, 0)
        
        #2. Ingresar ejemplares
        case 2:
            if not titulos:
                print("No existe ningún título en el catálogo. Primero ingrese un título en la opción 1 del menú si desea ingresar cantidad de ejemplares.")
                continue

            for i, titulo in enumerate(titulos):
                print(f"{i + 1}- {titulo}")
            
            #El usuario selecciona una posición y validamos si es correcta
            posicion = int(input("Seleccione el número de título para ingresar ejemplares: ")) - 1

            while posicion < 0 or posicion >= len(titulos):
              posicion = int(input("Posición inválida. Seleccione el número del título correctamente para ingresar ejemplares: ")) - 1 
            
            cantidad = int(input("Ingrese la cantidad de ejemplares que desea agregar: ")) 
            ejemplares[posicion] += cantidad 
            print(f"Se han añadido: {ejemplares[posicion]} ejemplares a {titulos[posicion]} ")





            # #Solicita la entrada y valida que sea correcta
            # while True:
            #     entrada = input("\nSeleccione el número de título para ingresar ejemplares: ")

            #     #Validación: valida que el usuario ingrese al menos algo, evitando que solo presione "Enter".
            #     if not entrada.isdigit():  
            #         print("\nDebe ingresar un número válido.")
            #         continue
                
            #     posicion = int(entrada) - 1

            #     #Validación: que se encuentre dentro del rango de nuestra lista
            #     if 0 <= posicion < len(titulos):   
            #         break
            #     else:
            #         print("\nPosición inválida. Seleccione el número del título correctamente.")

            # #Pedir cantidad de ejemplares con validación
            # while True:
            #     entrada = input("\nIngrese la cantidad de ejemplares que desea agregar: ")
            #     if not entrada.isdigit():
            #         print("Debe ingresar un número válido.")
            #         continue
            #     cantidad = int(entrada)
            #     break

            # #Actualización de ejemplares
            # ejemplares[posicion] += cantidad
            # print(f"\nEjemplares disponibles para: {titulos[posicion]} --> {ejemplares[posicion]}")

                