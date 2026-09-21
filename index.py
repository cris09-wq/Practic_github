elementos=[]

print("Gestionamiento de operaciones en sucursales")

while True:
    print(" seleccione la accion que quieras agregar o hacer")
    print("1. Nombre del sucursal")
    print("2. Direccion completa")
    print("3. medio de contacto")
    print("4. Id de gerente o responsable")
    print("5. Editar datos")
    print("6. eliminar datos")
    print("7. Ver datos")
    print("8. salir")

    opcion=input("Elige tu opcion (1-8): ").strip()

    if opcion==1:
        item=input("Escribe el nombre del sucursal que quieres agregar: ").strip()
        if item:
            elementos.append(item)
            print("El nombre se agrego correctamente")
        else:
            print("Error, no puedes dejar esta casilla vacia")
    elif opcion==2:
        item=input("Escribe la direccion completa del sucursal: ").strip()
        if item:
            elementos.append(item)
        else:
            print("Error, no puedes dejar esta casilla vacia")
    elif opcion==3:
        while True:
            print("1. Telefono")
            print("2. Correo electronico")
            print("3. salir")

            opcion3=input("Escribe tu opcion (1-2): ").strip()

            if opcion3==1:
                item=input("Escribe el numero de telefono").strip()
                if item:
                    elementos.append(item)
                else:
                    print("Error, no puede quedar este campo vacio")
            elif opcion3==2:
                item=input("Escribe la direccion de correo electronico")
                if item:
                    elementos.append(item)
                else:
                    print("Error, no se puede dejar este csampo vacio")
            

