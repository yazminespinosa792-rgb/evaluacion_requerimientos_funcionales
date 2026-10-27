import ollama

#EJEMPLO#
requerimiento = (
    "El usuario ingresa su matrícula y contraseña, posteriormente presiona el botón de iniciar sesión."
    "el sistema de autenticación"
    "debe"
    "validar silos datos son correctos, el sistema permitirá el acceso al usuario segun su rol" 
    "en la base de datos en la tabla de usuarios"
    "verifica que exista un usuario un usuario con esa matrícula y contraseña"
)
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
            },
        },

        "condicion_1":{
            "type": "noul",
            "instructions": "¿El requerimiento funcinal tiene un sujeto?",
            "criteria":{
                "true": "Especifica el sistema que accion debe de realizar el sujeto.",
                "false": "El requerimiento no menciona que acción debe realizar el sujeto."
            },
        },

        "condicion_2":{
            "type": "noul",
            "instructions": "¿Tiene el verbo normativo (debe) el requerimiento?",
            "criteria":{
                "true": "Especifica el verbo debe.",
                "false": "No especifica el verbo debe."
            },
        },

        "condicion_3":{
            "type": "noul",
            "instructions": "¿Se encuentra la acción que realizará el objeto?",
            "criteria":{
                "true": "Especifica que acción debe realizar el objeto o entidad.",
                "false": "No menciona la acción que realizará el objeto o entidad."
            },
        },

        "condicion_4":{
            "type": "noul",
            "instructions": "¿Se encuentra el objeto o entidad que realizará la acción?",
             "criteria":{
                "true": "Especifica el objeto o entidad que realizará la acción.",
                "false": "No menciona el objeto o entidad ."
             },
        },

        "condicion_5":{
            "type": "noul",
            "instructions": "¿Se encuentra el criterio de dicho requerimiento?",
            "criteria":{
                "true": "Especifica el criterio que se tomará en cuaenta para el requerimiento.",
                "false": "No especificael criterio."
            },
        },
    }
)

condicion = response.answers["condicion"].noul
condicion_1 = response.answers["condicion_1"].noul
condicion_2 = response.answers["condicion_2"].noul
condicion_3 = response.answers["condicion_3"].noul
condicion_4 = response.answers["condicion_4"].noul
condicion_5 = response.answers["condicion_5"].noul

if condicion >= 0.05:
    print(f"1. Cumple con la condición: {condicion}")
else:
    print(f"1. No cumple con la condición: {condicion}")

if condicion_1 >= 0.05:
    print(f"1. Cumple con la condición: {condicion_1}")
else:
    print(f"1. No cumple con la condición: {condicion_1}")

if condicion_2 >= 0.05:
    print(f"1. Cumple con la condición: {condicion_2}")
else:
    print(f"1. No cumple con la condición: {condicion_2}")

if condicion_3 >= 0.05:
    print(f"1. Cumple con la condición: {condicion_3}")
else:
    print(f"1. No cumple con la condición: {condicion_3}")

if condicion_4 >= 0.05:
    print(f"1. Cumple con la condición: {condicion_4}")
else:
    print(f"1. No cumple con la condición: {condicion_4}")

if condicion_5 >= 0.05:
    print(f"1. Cumple con la condición: {condicion_5}")
else:
    print(f"1. No cumple con la condición: {condicion_5}")

print(response.answers["condicion"])