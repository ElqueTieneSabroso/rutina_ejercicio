#definimos las respuestas dependiendo de la eleccion de la persona
def obtener_ejercicios(objetivo):
    ejercicios = {
        "perder peso": ["Cardio", "Caminata rápida", "Burpees", "Jumping Jacks"], #elecciones basadas en perder grasa eda
        "ganar músculo": ["Sentadillas con peso", "Flexiones", "Dominadas", "Peso muerto"], #ponerse mamei
        "mantenerse": ["Yoga", "Bicicleta", "Natación", "Caminata"] #cosas mas tranquilas que no terminen con tu vida
    }
    return ejercicios.get(objetivo, ["Ejercicio general"]) #returneamos un ejercicio general pues, general 
