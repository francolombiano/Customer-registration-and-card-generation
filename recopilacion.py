# Número de clientes a registrar
num_clientes = int(input("¿Cuántos clientes deseas registrar? "))

# Bucle para registrar y mostrar las tarjetas
for i in range(num_clientes):
    print(f"\n=== Cliente {i + 1} ===")
    nombre = input("Nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese edad: "))
    mail = input("Ingrese el correo electrónico: ")

    # Crear la tarjeta de presentación
    print("\n===== Tarjeta de Presentación =====")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad}")
    print(f"Correo Electrónico: {mail}")
    print("===================================")