def generar_rutina(usuario, ejercicios):
    rutina = []
    if usuario["nivel"] == "principiante":
        repeticiones = 2
    elif usuario["nivel"] == "intermedio":
        repeticiones = 3
    else:
        repeticiones = 4

    print(f"\n--- Rutina diaria para {usuario['nombre']} ---")
    for ejercicio in ejercicios:
        rutina.append(f"{ejercicio} - {repeticiones} series")
    return rutina
