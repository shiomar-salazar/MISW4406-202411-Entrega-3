# Entrega 4: 

Repositorio del equipo Optimizers de la Materia MISW4406-2024-11

## Integrantes:

|   Nombre                         |   Correo                      | Codigo    | 
|----------------------------------|-------------------------------|-----------|
| Jhon Fredy Guzmán Caicedo        | jf.guzmanc1@uniandes.edu.co   | 202216872 |
| Haiber Humberto Galindo Sanchez  | h.galindos@uniandes.edu.co    | 202216850 |
| Jorge M. Carrillo                | jm.carrillo@uniandes.edu.co   | 200426097 |
| Shiomar Alberto Salazar Castillo | s.salazarc@uniandes.edu.co    | 202213359 |

## Lanzar Gitpod

<a href="https://shiomarsala-misw4406202-j32zbu6sb2p.ws-us108.gitpod.io/" style="padding: 10px;">
    <img src="https://gitpod.io/button/open-in-gitpod.svg" width="150" alt="Push" align="center">
</a>
<br/><br/>


### Estructura del proyecto

1. Este proyecto fue creado usando un fork del tutorial #5 de clase obtenido del siguiente [enlace](https://github.com/MISW4406/tutorial-5-cqrs-eventos)
2. El codigo fuente del servicio implementado puede verse en la siguiente estructura:

```
├── .gitignore
├── .gitpod.yml
├── docker-compose.Dockerfile
├── Dockerfile
├── pyproject.toml
├── README.md
├── requirements.txt
└── src
    └── propiedadesalpes
        ├── __init__.py
        └── api
            ├── __init__.py
			├── compania.py
			├── contrato.py
            └── propiedad.py
        └── config
            ├── __init__.py
            ├── db.py
            ├── config.py
            └── uow.py
        └── modulos
            ├── __init__.py
            └── companias
                ├── __init__.py
                └── aplicacion
                    ├── __init__.py
                    ├── dto.py
                    ├── handlers.py
                    ├── mapeadores.py
                    ├── servicios.py
                    ├── comandos
                        ├── __init__.py
                        ├── base.py
                        └── crear_companias.py
                    └── queries
                        ├── __init__.py
                        ├── base.py
                        └── obtener_todas_companias.py
                └── dominio
                    ├── __init__.py
                    ├── entidades.py
                    ├── eventos.py
                    ├── excepciones.py
                    ├── fabricas.py
                    ├── objetos_valor.py
                    └── repositorios.py
                └── infraestructura
                    ├── __init__.py
                    ├── consumidores.py
                    ├── despachadores.py
                    ├── dto.py
                    ├── excepciones.py
                    ├── fabricas.py
                    ├── mapeadores.py
                    ├── repositorios.py
                    └── schema
                        ├── __init__.py
                        └── v1
                            ├── __init__.py
                            ├── comandos.py
                            ├── mensajes.py
                            └── eventos.py          
            └── contratos
                ├── __init__.py
                └── aplicacion
                    ├── __init__.py
                    ├── dto.py
                    ├── handlers.py
                    ├── mapeadores.py
                    ├── servicios.py
                    └── comandos
                        ├── __init__.py
                        ├── base.py
                        └── crear_contrato.py
                    └── queries
                        ├── __init__.py
                        ├── base.py
                        └── obtener_todos_contratos.py
                └── dominio
                    ├── __init__.py
                    ├── entidades.py
                    ├── eventos.py
                    ├── excepciones.py
                    ├── fabricas.py
                    ├── objetos_valor.py
                    └── repositorios.py
                └── infraestructura
                    ├── __init__.py
                    ├── consumidores.py
                    ├── despachadores.py
                    ├── dto.py
                    ├── excepciones.py
                    ├── fabricas.py
                    ├── mapeadores.py
                    ├── repositorios.py
                    └── schema
                        ├── __init__.py
                        └── v1
                            ├── __init__.py
                            ├── comandos.py
                            ├── mensajes.py
                            └── eventos.py  
            └── propiedades
                ├── __init__.py
                └── aplicacion
                    ├── __init__.py
                    ├── dto.py
                    ├── handlers.py
                    ├── mapeadores.py
                    ├── servicios.py
                    ├── comandos
                        ├── __init__.py
                        ├── base.py
                        └── crear_propiedad.py
                    └── queries
                        ├── __init__.py
                        ├── base.py
                        └── obtener_todas_propiedades.py
                └── dominio
                    ├── __init__.py
                    ├── entidades.py
                    ├── eventos.py
                    ├── excepciones.py
                    ├── fabricas.py
                    ├── objetos_valor.py
                    └── repositorios.py
                └── infraestructura
                    ├── __init__.py
                    ├── consumidores.py
                    ├── despachadores.py
                    ├── dto.py
                    ├── excepciones.py
                    ├── fabricas.py
                    ├── mapeadores.py
                    ├── repositorios.py
                    └── schema
                        ├── __init__.py
                        └── v1
                            ├── __init__.py
                            ├── comandos.py
                            ├── mensajes.py
                            └── eventos.py  
        └── seedwork
            ├── __init__.py
            └── aplicacion
                ├── __init__.py
                ├── comandos.py
                ├── dto.py
                ├── hablder.py
                ├── queries.py
                ├── comandos.py
                └── servicios.py
            └── dominio
                ├── __init__.py
                ├── entidades.py
                ├── eventos.py
                ├── excepciones.py
                ├── fabricas.py
                ├── mixins.py
                ├── objetos_valor.py
                ├── reglas.py
                ├── repositorios.py
                └── servicios.py
            └── infraestructura
                ├── __init__.py
                ├── uow.py
                ├── utils.py
                ├── vistas.py
                └── schema
                    ├── __init__.py
                    └── v1
                        ├── __init__.py
                        ├── comandos.py
                        ├── mensajes.py
                        └── eventos.py       
            └── presentacion
                ├── __init__.py
                └── api.py
```

### Escenarios de Calidad Seleccionados

#### Esceneario de Calidad #1: Desempeño
![image](https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3/assets/111320185/52eff4a1-20c8-40da-85b9-d627c5c3b4f9)

#### Esceneario de Calidad #2: Disponibilidad
![image](https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3/assets/111320185/c6d25f10-3638-4dbf-9768-8f69655add90)

#### Esceneario de Calidad #2: Seguridad
![image](https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3/assets/111320185/42f7a336-0f69-44de-a43c-f2adaed72240)

### Pre-requisitos para el despliegue con docker-compose

#### Docker:
- En primera instancia se debe tener instalado **Docker**. Para esto se comparten los siguientes enlaces:
  - **Instalación de docker en Windows**: https://docs.docker.com/desktop/install/windows-install
  - **Instalación de docker en Linux Ubuntu**: https://docs.docker.com/engine/install/ubuntu
  - **Instalación de docker en Mac**: https://docs.docker.com/desktop/install/mac-install/.

### Despliegue del Proyecto con docker-compose

Para el despliegue del proyecto utilizamos docker-compose que nos permitirá realizar el lanzamiento de cada uno de los contenedores de nuestro proyecto. Para ejecutar docker-compose, utilizamos el siguiente comando:
```bash
docker-compose -f "<RUTA_DEL_ARCHIVO_DOCKER_COMPOSE>" up -d
```
Ejemplo

```bash
docker-compose -f "docker-compose.yml" up -d
```

### Pre-requisitos para probar el servicio

#### Postman:

- Para realizar las pruebas del servicio, se debe instalar **Postman**.Para esto se comparten los siguientes enlaces:
  - **Instalación de docker en Windows**: https://dl.pstmn.io/download/latest/win64
  - **Instalación de docker en Linux Ubuntu**: https://dl.pstmn.io/download/latest/linux_64
  - **Instalación de docker en Mac**: https://dl.pstmn.io/download/latest/osx_arm64

#### Collection Postman:

- La coleccion de pruebas de los diferentes servicios se encuentra [aqui](https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3-4-5/blob/main/collections/MISW4406-2024-11-PDA.postman_collection.json), descargar e importar a Postman.

### Pruebas del servicio con Postman

- Se debe realizar el cambio de las variables HOST_COMPANIAS, HOST_CONTRATOS y HOST_PROPIEDADES, con los apuntamientos obtenidos del despliegue realizado con anterioridad.

![image](https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3-4-5/assets/110913673/69a5c7ca-940d-496a-a368-164d20dd4761)

- Una vez se realice el cambio, ejecutar pruebas del servicio

![image](https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3-4-5/assets/110913673/64930eac-0d51-4326-a3ce-b19fc73eb44d)

## Decisiones de arquitectura
Acorde al problema planteado por propiedades de los Alpes se ha diseñado una arquitectura que cumpla con las características necesarias para su operación, a continuación, se detallan las decisiones de arquitectura más relevantes. 

* **Arquitectura Hexagonal:**  también conocida como arquitectura de puertos y adaptadores permite aislar la lógica de negocio de las conexiones externas con otros componentes mediante la separación en componentes con bajo acoplamiento. 

* **CQRS:** Es un patrón de diseño que nos permite separar las lecturas y los comandos, tanto a nivel de código e incluso llegar hasta el escalamiento independiente, para propiedades de los Alpes cada componente tiene independiente la lógica de consulta de la lógica de los comandos de creación. 

* **Estilo de Arquitectura Microservicios:** El estilo de arquitectura basada en microservicios nos permite generar servicios independientes con responsabilidades claramente definidas acorde a su contexto acotado, cada microservicio tiene la posibilidad de escalar horizontalmente independientemente acorde a la carga que su funcionalidad requiera, así como su despliegue. El estilo de arquitectura de microservicios aumenta la dificultad de implementación y monitoreo. 

* **Comunicación basada en Eventos:** para favorecer la flexibilidad y bajo acoplamiento del sistema, se busca una comunicación basada en eventos, lo que permite realizar llamadas asíncronas, mejoras tiempos de respuesta añadiendo respuestas simuladas y permitiendo que otros componentes puedan escalar acorde a la carga que sea inyectada.  

### AVRO
Decidicmos usar Avro porque es un proyecto de código abierto que proporciona servicios de serialización e intercambio de datos. Estos servicios se pueden utilizar juntos o separados. Avro facilita el intercambio de big data entre programas escritos en cualquier lenguaje. Con el servicio de serialización, los programas pueden serializar datos de manera eficiente en archivos o mensajes. El almacenamiento de datos es compacto y eficiente. Avro almacena tanto la definición de datos como los datos juntos en un mensaje o archivo.\
Avro almacena la definición de datos en formato JSON, lo que facilita su lectura e interpretación. Los datos en sí se almacenan en formato binario, lo que los hace compactos y eficientes.\
Una de las características principales de Avro es su sólida compatibilidad con esquemas de datos que cambian con el tiempo, lo que a menudo se denomina evolución de esquema. Avro gestiona cambios de esquema como campos faltantes, campos agregados y campos modificados; como resultado, los programas antiguos pueden leer datos nuevos y los programas nuevos pueden leer datos antiguos.
### Event Sourcing
En la arquitectura propuesta, se implementó event sourcing como patrón de almacenamiento, pues este es un patrón que permite almacenar los eventos de forma indefinida, proporcionando a la aplicación un registro de auditoría de cambios que garantiza su precisión. También permite que una aplicación reconstruya el estado histórico de un agregado. Por otro lado, crea un desafío, porque la estructura de los eventos a menudo cambia con el tiempo.
#### Ventajas que nos proporciona event sourcing:
#### 1. Publica de manera confiable eventos de dominio:
Un beneficio importante de evento sourcing es que publica eventos de manera confiable cada vez que cambia el estado de un agregado. Esa es una buena base para una arquitectura de microservicios basada en eventos. Además, debido a que cada evento puede almacenar la identidad del usuario que realizó el cambio, evento sourcing proporciona un registro de auditoría cuya exactitud se garantiza. El flujo de eventos se puede utilizar para una variedad de otros fines, incluida la notificación a los usuarios, la integración de aplicaciones, el análisis y la supervisión.
#### 2. Preserva la historia de los agregados:
Otro beneficio de evento sourcing es que almacena el historial completo de cada agregado. Puede implementar fácilmente consultas temporales que recuperen el estado pasado de un agregado. Para determinar el estado de un agregado en un momento dado, se suman los eventos que ocurrieron hasta ese momento.
#### 3. Proporciona a los desarrolladores una máquina del tiempo:
Event sourcing almacena un historial de todo lo que sucedió durante la vida útil de una aplicación.


### Video de la Entrega 4

https://uniandes-edu-co.zoom.us/rec/share/IWswfiKii2DxWzs8H6L3M90EuNwA6qchW7-xLRrwtpHHQiDFobSPQils02o7Rivi.1keraYaOW53Z-Tuh
Código de acceso:  aKE1%41^
