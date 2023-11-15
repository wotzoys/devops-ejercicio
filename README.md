# Ejercicio DevOps VANAGT - Api HTTP y Python

###  
[Definición del proyecto:](https://vanagt.notion.site/Prueba-t-cnica-DevOps-64621cd5671b457ca55ecaec77600f8e?pvs=4)

[Solucion requerida](https://acortar.link/9MS2Hj)

## Paso 1
Primero realicé el Fork del repositorio según las instrucciones, dejando el mismo nombre del repositorio. 
Clono mi repositorio creado anteriormente en mi equipo local, con los siguientes comandos. 

```sh
$ git clone https://github.com/wotzoys/devops-ejercicio.git
$ cd devops-ejercicio```

## Paso 2
Crear el codigo en AWS SAM dada la instrucción a utilizar. 

## Paso 3
El siguiente diagrama detalla cuál es el flujo de trabajo segun las instrucciones
1. El DEV hace el push del con los cambios del codigo.
2. Esto desencadena todo el flujo de CI/CD de Github y Github Actions.
3. El flujo de trabajo activa AWS SAM para aprovisionar e implementar tanto Lambda como API Gateway. (En el S3 se guarda el template a utilizar)
4. El cliente final activa la Lambda haciendo peticiones en la URL.
(https://github.com/wotzoys/devops-ejercicio/blob/main/AWS%20API%20HTTP.png)

##Diseño el flujo de Github Actions

