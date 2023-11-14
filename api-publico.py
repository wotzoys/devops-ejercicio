import json

def lambda_handler(event, context):
    # HTML con formato - Algo extra para el API HTTP
    html_body = """
        <html>
        <head>
            <style>
                body {
                    background-color: #f0f0f0; 
                    font-family: Arial, sans-serif;
                    color: #333; 
                    max-width: 600px; 
                    margin: auto; 
                    padding: 20px; 
                }
                h1 {
                    color: #0066cc; /* Color del encabezado */
                }
                p {
                    margin-bottom: 10px;
                }
            </style>
        </head>
        <body>
            <h1>¡Hola desde AWS Lambda! - Proyecto Dev VANA</h1>
            <p>Mi nombre es Wilhelm Otzoy.</p>
            <div>
                <h2>Mi Perfil</h2>
                <p>Soy una persona entusiaste de las tecnologias, me gusta invovar y seguir aprendiendo cada dia mas</p>
            </div>
            <div>
                <h2>Mi Experiencia</h2>
                <p>Mi experiencia en los ultimos 5 anios en DevOps, manejando AWS y Azure especialmente, pero en los ultimos meses me he estado sacando cursos de CiberSeguridad Cloud y la Nube huawei.</p>
            </div>
        </body>
        </html>
    """
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
        },
        "body": html_body,
    }
    return response
