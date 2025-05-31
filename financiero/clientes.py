#lista de clientes
clientes = ["shiuli", "Shaida", " ", "Guisem", " ", "Faraz"]

for i, nombre in enumerate(clientes):    #enumerate proporciona automáticamente la posición del elemento sin necesidad de contador manual
    if nombre.strip():  # Verifica que el nombre no esté vacío o sea solo espacios
        print(f"Cliente {i}: {nombre.capitalize()}")
    else:
        print(f"Cliente {i}: Nombre no válido")


