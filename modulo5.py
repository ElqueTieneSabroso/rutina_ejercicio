def main():
    usuario = capturar_datos_usuario()
    ejercicios = obtener_ejercicios(usuario["objetivo"])
    rutina = generar_rutina(usuario, ejercicios)
    
    for r in rutina:
        print(r)

    consejos_salud()

if name_ == "_main_":
    main()