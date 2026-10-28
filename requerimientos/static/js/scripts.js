async function evaluacion(){
    try{

        const uri = "https://localhost:11434/v1/systemone"; //corregir
        const requerimiento = "El usuario ingresa su email y contraseña, y el sistema autentica los datos"

        const data = {
            "condicion": {
            "type": "noul",
            "instructions": "¿Incluye una situación que detone el evento?",
            "criteria": {
                "true": "Especifica claramente el evento o situación detonante.",
                "false": "No menciona qué acción dispara el evento."
                }
            }
        }

        const response = await fetch(
            uri,
            {
                metodo:"POST",
                headers: {
                    "Constent-Type" : "aplication/json"
                },
                body: JSON.stringify(data)
            }
        );

        const resultado = await response.json

        console.log("Conexion con la API exitosa: ", resultado)
        console.log("Criterio: ", resultado.answers.)
        

    } catch (error){
        console.log("Ups algo fallo", error.message)
        throw error;
    }
}