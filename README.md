# Ejercicio DevOps VANAGT - Api HTTP y Python

###  
[Definición del proyecto:](https://vanagt.notion.site/Prueba-t-cnica-DevOps-64621cd5671b457ca55ecaec77600f8e?pvs=4)

[Solucion requerida](https://acortar.link/9MS2Hj)

## Paso 1
Primero realicé el Fork del repositorio según las instrucciones, dejando el mismo nombre del repositorio. 
Clono mi repositorio creado anteriormente en mi equipo local, con los siguientes comandos. 

```sh
$ git clone https://github.com/wotzoys/devops-ejercicio.git
$ cd devops-ejercicio
```

## Paso 2
Crear el codigo en AWS SAM dada la instrucción a utilizar. 

## Paso 3
El siguiente diagrama detalla cuál es el flujo de trabajo segun las instrucciones
1. El DEV hace el push del con los cambios del codigo.
2. Esto desencadena todo el flujo de CI/CD de Github y Github Actions.
3. El flujo de trabajo activa AWS SAM para aprovisionar e implementar tanto Lambda como API Gateway. (En el S3 se guarda el template a utilizar)
4. El cliente final activa la Lambda haciendo peticiones en la URL. (https://acortar.link/9MS2Hj)
   
![Diagrama](https://github.com/wotzoys/devops-ejercicio/blob/main/AWS%20API%20HTTP.png)

## Paso 4 Diseño el flujo de Github Actions
El codigo se encuentra en la ruta (https://github.com/wotzoys/devops-ejercicio/blob/main/.github/workflows/main.yml)
```
name: Deploy AWS SAM
on:
  push:
    branches:
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    - name: Setup AWS SAM CLI
      uses: aws-actions/setup-sam@v2
      with:
        use-installer: true
    - name: Configure AWS Credentials
      uses: aws-actions/configure-aws-credentials@v2
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-west-2
    - name: Run SAM Build
      run: sam build --use-container
    - name: Run SAM Deploy
      run: |
        sam deploy \
        --template-file template.yml \
        --resolve-s3 \
        --stack-name sam-stack \
        --capabilities CAPABILITY_IAM \
        --no-confirm-changeset \
        --no-fail-on-empty-changeset
```
## Paso 5 Diseño del Template para AWS SAM
### El template.yaml crea una función Lambda y un API Gateway HTTP con un GET endpoint para /api-publico.

```  
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: SAM Template for the DevOps
Resources:
  LambdaFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: .
      Handler: api-publico.lambda_handler
      FunctionName: api-publico
      Runtime: python3.10
      Events:
        ApiGateway:
          Type: HttpApi
          Properties:
            Path: /api-publico
            Method: GET
            ApiId: !Ref ApiGateway
  ApiGateway:
    Type: AWS::Serverless::HttpApi
    Properties:
      StageName: dev
Outputs:
  endpoint:
    Description: 'API Gateway endpoint URL for the Lambda function'
    Value: !Sub 'https://${ApiGateway}.execute-api.${AWS::Region}.amazonaws.com/dev/api-publico'
```
## Paso 6 Configuración de Credenciales del Repositorio de Github
"Como el sistema de GitHub hace automáticamente todo el proceso de poner en marcha los procesos, es importante configurar unas 'keys' especiales en el espacio de trabajo de GitHub. Estas keys' son como claves secretas que ayudan a que todo funcione sin problemas."

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

## Resultado del proceso de Github Actions
![Resultado](https://github.com/wotzoys/devops-ejercicio/blob/main/githubactions.png)

## Resultado Final prueba
Con esto se finaliza el proyecto de prueba para el proceso de DevOps
![Final](https://github.com/wotzoys/devops-ejercicio/blob/main/result.png)

Agradezco el tiempo brindado. :) 
