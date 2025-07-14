def obtener_ejercicios(objetivo):
    ejercicios = {
        "perder peso": ["Cardio", "Caminata rápida", "Burpees", "Jumping Jacks"],
        "ganar músculo": ["Sentadillas con peso", "Flexiones", "Dominadas", "Peso muerto"],
        "mantenerse": ["Yoga", "Bicicleta", "Natación", "Caminata"]
    }
    return ejercicios.get(objetivo, ["Ejercicio general"])