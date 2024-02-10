def validar_longitud(cadena, min_longitud, max_longitud):
    return min_longitud <= len(cadena) <= max_longitud

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 10

def validar_correo(correo):
    return "@" in correo and "." in correo and validar_longitud(correo, 5, 50)

def new_user(id_counter):
    nombre = input('Ingresa tu nombre: ')
    apellidos = input("Ingresa tus apellidos: ")
    telefono = input("Ingresa tu número de teléfono: ")
    email = input("Ingresa tu correo electrónico: ")

    while not (validar_longitud(nombre, 5, 50) and
               validar_longitud(apellidos, 5, 50) and
               validar_telefono(telefono) and
               validar_correo(email)):
        print("Error: Ingresa datos válidos.")
        nombre = input('Ingresa tu nombre: ')
        apellidos = input("Ingresa tus apellidos: ")
        telefono = input("Ingresa tu número de teléfono: ")
        email = input("Ingresa tu correo electrónico: ")

    id_counter[0] += 1
    return id_counter[0], {"nombre": nombre, "apellidos": apellidos, "telefono": telefono, "email": email}

def show_user(user_id, users):
    for user in users:
        if user[0] == user_id:
            print(f"Información del usuario con ID {user_id}:")
            print(f"Nombre: {user[1]['nombre']}")
            print(f"Apellidos: {user[1]['apellidos']}")
            print(f"Teléfono: {user[1]['telefono']}")
            print(f"Correo electrónico: {user[1]['email']}")
            return
    print("Usuario no encontrado.")

def edit_user(user_id, users):
    for i, user in enumerate(users):
        if user[0] == user_id:
            print(f"Editando información del usuario con ID {user_id}:")
            nombre = input('Ingresa el nuevo nombre: ')
            apellidos = input("Ingresa los nuevos apellidos: ")
            telefono = input("Ingresa el nuevo número de teléfono: ")
            email = input("Ingresa el nuevo correo electrónico: ")

            while not (validar_longitud(nombre, 5, 50) and
                       validar_longitud(apellidos, 5, 50) and
                       validar_telefono(telefono) and
                       validar_correo(email)):
                print("Error: Ingresa datos válidos.")
                nombre = input('Ingresa el nuevo nombre: ')
                apellidos = input("Ingresa los nuevos apellidos: ")
                telefono = input("Ingresa el nuevo número de teléfono: ")
                email = input("Ingresa el nuevo correo electrónico: ")

            users[i] = (user_id, {"nombre": nombre, "apellidos": apellidos, "telefono": telefono, "email": email})
            print("Usuario actualizado.")
            return
    print("Usuario no encontrado.")

def delete_user(user_id, users):
    for i, user in enumerate(users):
        if user[0] == user_id:
            del users[i]
            print(f"Usuario con ID {user_id} eliminado.")
            return
    print("Usuario no encontrado.")

def list_users(users):
    print("ID de los usuarios registrados:")
    for user in users:
        print(user[0])

def menu():
    print("\n*** Menú de opciones ***")
    print("A. Registrar nuevos usuarios")
    print("B. Listar usuarios")
    print("C. Ver información de un usuario")
    print("D. Editar información de un usuario")
    print("E. Eliminar un usuario")
    print("F. Salir")

cantidad_usuarios = int(input("Ingresa la cantidad de usuarios a capturar: "))
usuarios = []
id_counter = [0]

for _ in range(cantidad_usuarios):
    usuario = new_user(id_counter)
    usuarios.append(usuario)

opcion = ""
while opcion != "F":
    menu()
    opcion = input("Elige una opción (A, B, C, D, E o F): ").upper()

    if opcion == "A":
        usuario = new_user(id_counter)
        usuarios.append(usuario)
        print("Usuario registrado exitosamente.")
    elif opcion == "B":
        list_users(usuarios)
    elif opcion == "C":
        id_usuario = int(input("Ingresa el ID del usuario que deseas ver: "))
        show_user(id_usuario, usuarios)
    elif opcion == "D":
        id_usuario = int(input("Ingresa el ID del usuario que deseas editar: "))
        edit_user(id_usuario, usuarios)
    elif opcion == "E":
        id_usuario = int(input("Ingresa el ID del usuario que deseas eliminar: "))
        delete_user(id_usuario, usuarios)
    elif opcion == "F":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, elige una opción válida.")

