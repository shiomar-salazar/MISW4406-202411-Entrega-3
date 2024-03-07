## Lanzar Gitpod

<a href="https://shiomarsala-misw4406202-j32zbu6sb2p.ws-us108.gitpod.io/" style="padding: 10px;">
    <img src="https://gitpod.io/button/open-in-gitpod.svg" width="150" alt="Push" align="center">
</a>
<br/><br/>


### Estructura del proyecto

1. Este proyecto fue creado usando un fork del tutorial #5 de clase obtenido del siguiente [enlace](https://github.com/MISW4406/tutorial-5-cqrs-eventos)
2. El codigo fuente del servicio implementado puede verse en la siguiente estructura:

```
├─ .gitignore
├─ .gitpod.yml
├─ collections
│  └─ MISW4406-2024-11-PDA.postman_collection.json
├─ companias.Dockerfile
├─ config.sh
├─ contratos.Dockerfile
├─ deployment-steps-gcp
├─ docker-compose.yml
├─ propiedades.Dockerfile
├─ pyproject.toml
├─ README.md
├─ requirements.txt
└─ src
   ├─ companias
   │  ├─ api
   │  │  ├─ recursos.py
   │  │  └─ __init__.py
   │  ├─ config
   │  │  ├─ config.py
   │  │  ├─ db.py
   │  │  ├─ uow.py
   │  │  └─ __init__.py
   │  ├─ modulos
   │  │  └─ companias
   │  │     ├─ aplicacion
   │  │     │  ├─ comandos
   │  │     │  │  ├─ base.py
   │  │     │  │  ├─ crear_compania.py
   │  │     │  │  └─ rollback.py
   │  │     │  ├─ dto.py
   │  │     │  ├─ handlers.py
   │  │     │  ├─ mapeadores.py
   │  │     │  ├─ queries
   │  │     │  │  ├─ base.py
   │  │     │  │  └─ obtener_todas_companias.py
   │  │     │  ├─ servicios.py
   │  │     │  └─ __init__.py
   │  │     ├─ dominio
   │  │     │  ├─ entidades.py
   │  │     │  ├─ eventos.py
   │  │     │  ├─ excepciones.py
   │  │     │  ├─ fabricas.py
   │  │     │  ├─ objetos_valor.py
   │  │     │  ├─ repositorios.py
   │  │     │  └─ __init__.py
   │  │     ├─ infraestructura
   │  │     │  ├─ consumidores.py
   │  │     │  ├─ despachadores.py
   │  │     │  ├─ dto.py
   │  │     │  ├─ excepciones.py
   │  │     │  ├─ fabricas.py
   │  │     │  ├─ mapeadores.py
   │  │     │  ├─ repositorios.py
   │  │     │  ├─ schema
   │  │     │  │  ├─ v1
   │  │     │  │  │  ├─ comandos.py
   │  │     │  │  │  ├─ eventos.py
   │  │     │  │  │  └─ __init__.py
   │  │     │  │  └─ __init__.py
   │  │     │  └─ __init__.py
   │  │     └─ __init__.py
   │  └─ seedwork
   │     ├─ aplicacion
   │     │  ├─ comandos.py
   │     │  ├─ dto.py
   │     │  ├─ handlers.py
   │     │  ├─ queries.py
   │     │  ├─ servicios.py
   │     │  └─ __init__.py
   │     ├─ dominio
   │     │  ├─ entidades.py
   │     │  ├─ eventos.py
   │     │  ├─ excepciones.py
   │     │  ├─ fabricas.py
   │     │  ├─ mixins.py
   │     │  ├─ objetos_valor.py
   │     │  ├─ reglas.py
   │     │  ├─ repositorios.py
   │     │  ├─ servicios.py
   │     │  └─ __init__.py
   │     ├─ infraestructura
   │     │  ├─ schema
   │     │  │  ├─ v1
   │     │  │  │  ├─ comandos.py
   │     │  │  │  ├─ eventos.py
   │     │  │  │  ├─ mensajes.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ uow.py
   │     │  ├─ utils.py
   │     │  ├─ vistas.py
   │     │  └─ __init__.py
   │     ├─ presentacion
   │     │  ├─ api.py
   │     │  └─ __init__.py
   │     └─ __init__.py
   ├─ contratos
   │  ├─ api
   │  │  ├─ recursos.py
   │  │  └─ __init__.py
   │  ├─ config
   │  │  ├─ config.py
   │  │  ├─ db.py
   │  │  ├─ uow.py
   │  │  └─ __init__.py
   │  ├─ modulos
   │  │  └─ contratos
   │  │     ├─ aplicacion
   │  │     │  ├─ comandos
   │  │     │  │  ├─ base.py
   │  │     │  │  ├─ crear_contrato.py
   │  │     │  │  └─ __init__.py
   │  │     │  ├─ dto.py
   │  │     │  ├─ handlers.py
   │  │     │  ├─ mapeadores.py
   │  │     │  ├─ queries
   │  │     │  │  ├─ base.py
   │  │     │  │  └─ obtener_todos_contratos.py
   │  │     │  ├─ servicios.py
   │  │     │  └─ __init__.py
   │  │     ├─ dominio
   │  │     │  ├─ entidades.py
   │  │     │  ├─ eventos.py
   │  │     │  ├─ excepciones.py
   │  │     │  ├─ fabricas.py
   │  │     │  ├─ objetos_valor.py
   │  │     │  ├─ repositorios.py
   │  │     │  └─ __init__.py
   │  │     ├─ infraestructura
   │  │     │  ├─ consumidores.py
   │  │     │  ├─ despachadores.py
   │  │     │  ├─ dto.py
   │  │     │  ├─ excepciones.py
   │  │     │  ├─ fabricas.py
   │  │     │  ├─ mapeadores.py
   │  │     │  ├─ repositorios.py
   │  │     │  ├─ schema
   │  │     │  │  ├─ v1
   │  │     │  │  │  ├─ comandos.py
   │  │     │  │  │  ├─ eventos.py
   │  │     │  │  │  └─ __init__.py
   │  │     │  │  └─ __init__.py
   │  │     │  └─ __init__.py
   │  │     └─ __init__.py
   │  └─ seedwork
   │     ├─ aplicacion
   │     │  ├─ comandos.py
   │     │  ├─ dto.py
   │     │  ├─ handlers.py
   │     │  ├─ queries.py
   │     │  ├─ servicios.py
   │     │  └─ __init__.py
   │     ├─ dominio
   │     │  ├─ entidades.py
   │     │  ├─ eventos.py
   │     │  ├─ excepciones.py
   │     │  ├─ fabricas.py
   │     │  ├─ mixins.py
   │     │  ├─ objetos_valor.py
   │     │  ├─ reglas.py
   │     │  ├─ repositorios.py
   │     │  ├─ servicios.py
   │     │  └─ __init__.py
   │     ├─ infraestructura
   │     │  ├─ schema
   │     │  │  ├─ v1
   │     │  │  │  ├─ comandos.py
   │     │  │  │  ├─ eventos.py
   │     │  │  │  ├─ mensajes.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ uow.py
   │     │  ├─ utils.py
   │     │  ├─ vistas.py
   │     │  └─ __init__.py
   │     ├─ presentacion
   │     │  ├─ api.py
   │     │  └─ __init__.py
   │     └─ __init__.py
   └─ propiedades
      ├─ api
      │  ├─ recursos.py
      │  └─ __init__.py
      ├─ config
      │  ├─ config.py
      │  ├─ db.py
      │  ├─ uow.py
      │  └─ __init__.py
      ├─ modulos
      │  └─ propiedades
      │     ├─ aplicacion
      │     │  ├─ comandos
      │     │  │  ├─ base.py
      │     │  │  └─ crear_propiedad.py
      │     │  ├─ dto.py
      │     │  ├─ handlers.py
      │     │  ├─ mapeadores.py
      │     │  ├─ queries
      │     │  │  ├─ base.py
      │     │  │  └─ obtener_todas_propiedades.py
      │     │  ├─ servicios.py
      │     │  └─ __init__.py
      │     ├─ dominio
      │     │  ├─ entidades.py
      │     │  ├─ eventos.py
      │     │  ├─ excepciones.py
      │     │  ├─ fabricas.py
      │     │  ├─ objetos_valor.py
      │     │  ├─ repositorios.py
      │     │  └─ __init__.py
      │     ├─ infraestructura
      │     │  ├─ consumidores.py
      │     │  ├─ despachadores.py
      │     │  ├─ dto.py
      │     │  ├─ excepciones.py
      │     │  ├─ fabricas.py
      │     │  ├─ mapeadores.py
      │     │  ├─ repositorios.py
      │     │  ├─ schema
      │     │  │  ├─ v1
      │     │  │  │  ├─ comandos.py
      │     │  │  │  ├─ eventos.py
      │     │  │  │  └─ __init__.py
      │     │  │  └─ __init__.py
      │     │  └─ __init__.py
      │     └─ __init__.py
      └─ seedwork
         ├─ aplicacion
         │  ├─ comandos.py
         │  ├─ dto.py
         │  ├─ handlers.py
         │  ├─ queries.py
         │  ├─ servicios.py
         │  └─ __init__.py
         ├─ dominio
         │  ├─ entidades.py
         │  ├─ eventos.py
         │  ├─ excepciones.py
         │  ├─ fabricas.py
         │  ├─ mixins.py
         │  ├─ objetos_valor.py
         │  ├─ reglas.py
         │  ├─ repositorios.py
         │  ├─ servicios.py
         │  └─ __init__.py
         ├─ infraestructura
         │  ├─ schema
         │  │  ├─ v1
         │  │  │  ├─ comandos.py
         │  │  │  ├─ eventos.py
         │  │  │  ├─ mensajes.py
         │  │  │  └─ __init__.py
         │  │  └─ __init__.py
         │  ├─ uow.py
         │  ├─ utils.py
         │  ├─ vistas.py
         │  └─ __init__.py
         ├─ presentacion
         │  ├─ api.py
         │  └─ __init__.py
         └─ __init__.py
```

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

### Entregables
Los entregables se movieron a Wiki para tener mejor control de los mismos:
#### Entrega Semana 3
https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3-4-5/wiki/Entrega3
#### Entrega Semana 4
https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3-4-5/wiki/Entrega4
#### Entrega Semana 5
https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3-4-5/wiki/Entrega5
