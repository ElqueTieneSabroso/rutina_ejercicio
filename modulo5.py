from modulo1 import capturar_datos_usuario
from ejerciciomodulo2 import obtener_ejercicios
from modulo3 import generar_rutina
from modulo4 import consejos_salud

def main():
    usuario = capturar_datos_usuario()
    ejercicios = obtener_ejercicios(usuario["objetivo"])
    rutina = generar_rutina(usuario, ejercicios)
    
    for r in rutina:
        print(r)

    consejos_salud()

if __name__ == "_main_":
    main()