# Número de clientes a registrar
num_clientes = int(input("¿Cuántos clientes deseas registrar? "))

for i in range(num_clientes):
    print(f"\n=== Cliente {i + 1} ===")

    # Validar cada campo dentro del bucle
    while True:
        nombre = input("Ingrese el nombre: ").strip().title()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    while True:
        apellido = input("Ingrese el apellido: ").strip().title()
        if apellido:
            break
        print("El apellido no puede estar vacío.")

    while True:
        edad = input("Ingrese la edad: ").strip()
        if edad.isdigit():
            edad = int(edad)
            break
        print("La edad ingresada no es válida. Debe ser un número.")

    # Clasificar la edad y almacenar el resultado
    if edad < 15:
        clasificacion = "Niño"
    elif 15 <= edad <= 18:
        clasificacion = "Adolescente"
    else:
        clasificacion = "Adulto"

    while True:
        mail = input("Ingrese el correo electrónico: ").strip().replace(" ", "")
        if mail and mail.count("@") == 1:
            break
        print("El correo electrónico no puede estar vacío y debe contener solo una '@'.")

    # Crear la tarjeta de presentación para cada cliente
    print("\n===== Tarjeta de Presentación =====")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad} ({clasificacion})")
    print(f"Correo Electrónico: {mail}")
    print("===================================")
