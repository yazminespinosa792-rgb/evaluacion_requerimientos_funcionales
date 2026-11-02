async function evaluacion(){
    try{

        const uri = "https://localhost:11434/v1/systemone"; 
        const requerimiento = "Cuando el entrenador programa una nueva práctica en el calendario, el módulo de entrenamientos debe registrar una nueva sesión de entrenamiento con la fecha y hora, habilitando la sesión para realizar el registro de asistencias.";

        const data = {
            "state": requerimiento,
            "questions": {
                "condicion": {
                    "type": "noul",
                    "instructions": "¿Incluye una situación que detone el evento?",
                    "criteria": {
                        "true": "Especifica claramente el evento o situación detonante.",
                        "false": "No menciona qué acción dispara el evento."
                    }
                },
                "condicion_1": {
                    "type": "noul",
                    "instructions": "¿El requerimiento funcional tiene un sujeto?",
                    "criteria": {
                        "true": "Especifica el sistema qué acción debe realizar el sujeto.",
                        "false": "El requerimiento no menciona qué acción debe realizar el sujeto."
                    }
                },
                "condicion_2": {
                    "type": "noul",
                    "instructions": "¿Tiene el verbo normativo (debe) el requerimiento?",
                    "criteria": {
                        "true": "Especifica el verbo debe.",
                        "false": "No especifica el verbo debe."
                    }
                },
                "condicion_3": {
                    "type": "noul",
                    "instructions": "¿Se encuentra la acción que realizará el objeto?",
                    "criteria": {
                        "true": "Especifica qué acción debe realizar el objeto o entidad.",
                        "false": "No menciona la acción que realizará el objeto o entidad."
                    }
                },
                "condicion_4": {
                    "type": "noul",
                    "instructions": "¿Se encuentra el objeto o entidad que realizará la acción?",
                    "criteria": {
                        "true": "Especifica el objeto o entidad que realizará la acción.",
                        "false": "No menciona el objeto o entidad."
                    }
                },
                "condicion_5": {
                    "type": "noul",
                    "instructions": "¿Se encuentra el criterio de dicho requerimiento?",
                    "criteria": {
                        "true": "Especifica el criterio que se tomará en cuenta para el requerimiento.",
                        "false": "No especifica el criterio."
                    }
                }
            }
        };

        const response = await fetch(
            uri,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        );

        const resultado = await response.json();

        console.log("Conexion con la API exitosa: ", resultado);

        // Se colocan los valores numéricos correspondientes dentro de cada botón
        document.getElementById("condicion").innerText = resultado.answers.condicion.noul;
        document.getElementById("sujeto").innerText = resultado.answers.condicion_1.noul;
        document.getElementById("verbo").innerText = resultado.answers.condicion_2.noul;
        document.getElementById("accion").innerText = resultado.answers.condicion_3.noul;
        document.getElementById("objeto").innerText = resultado.answers.condicion_4.noul;
        document.getElementById("criterio").innerText = resultado.answers.condicion_5.noul;
        
    } catch (error){
        console.log("Ups algo fallo", error.message);
        throw error;
    }
}pruebas 