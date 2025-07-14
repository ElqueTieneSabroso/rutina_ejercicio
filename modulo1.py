def capturar_datos_usuario():
    print("=== Bienvenido al Generador de Rutinas Personalizadas ===")
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    nivel = input("Nivel (principiante/intermedio/avanzado): ").lower()
    objetivo = input("Objetivo (perder peso/ganar músculo/mantenerse): ").lower()
    return {"nombre": nombre, "edad": edad, "nivel": nivel, "objetivo": objetivo}

