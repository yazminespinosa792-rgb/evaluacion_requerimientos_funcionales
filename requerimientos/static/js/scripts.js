async function evaluacion(){
    try{

        const uri = "https://noxious-cobweb-4q649qr5rj96f6xj-11434.app.github.dev/api/generate";
        const requerimiento = "El usuario ingresa su email y contraseña, y el sistema autentica los datos";

        const data = {
            model: "llama3.2:3b",
            prompt: `Requerimiento: ${requerimiento}. Condición: ¿Incluye una situación que detone el evento?`,
            stream: false,
            condicion: {
                type: "noul",
                instructions: "¿Incluye una situación que detone el evento?",
                criteria: {
                    true: "Especifica claramente el evento o situación detonante.",
                    false: "No menciona qué acción dispara el evento."
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
        console.log("Criterio: ", resultado.response); 

    } catch (error){
        console.log("Ups algo fallo", error.message);
        throw error;
    }
}