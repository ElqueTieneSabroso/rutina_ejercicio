# main.py

from modulo1 import capturar_datos_usuario
from ejerciciomodulo2 import obtener_ejercicios
from modulo3 import generar_rutina
from modulo4 import consejos_salud
from modulo5 import main

datos = capturar_datos_usuario()
ejercicios = obtener_ejercicios(datos["objetivo"])
rutina = generar_rutina(datos, ejercicios)
consejos = consejos_salud()

print(f"\n--- Rutina diaria para {datos['nombre']} ---")
for r in rutina:
    print(f"- {r}")

    print("\n--- Consejos de salud ---")


main()

