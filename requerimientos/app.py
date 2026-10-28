import ollama

requerimiento = ("El usuario ingresa su email y contraseña, y el sistema autentica los datos.")
response = ollama.systemone(
    model="d1-omni:600m",
    state=requerimiento,
    questions={
        "condicion": {
            "type": "noul",
            "instructions": "¿Incluye una situación que detone el evento?",
            "criteria": {
                "true": "Especifica claramente el evento o situación detonante.",
                "false": "No menciona qué acción dispara el evento."
            }
        }
    }
)

condicion = response.answers["condicion"].noul

if condicion >= 0.05:
    print(f"1. Cumple con la condición: {condicion}")
else:
    print(f"1. No cumple con la condición: {condicion}")


print(response.answers["condicion"])