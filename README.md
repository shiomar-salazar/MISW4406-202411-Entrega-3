# Entrega 3: 

Repositorio del equipo Optimizers de la Materia MISW4406-2024-11

## Integrantes:

|   Nombre                         |   Correo                      | Codigo    | 
|----------------------------------|-------------------------------|-----------|
| Jhon Fredy Guzmán Caicedo        | jf.guzmanc1@uniandes.edu.co   | 202216872 |
| Haiber Humberto Galindo Sanchez  | h.galindos@uniandes.edu.co    | 202216850 |
| Jorge M. Carrillo                | jm.carrillo@uniandes.edu.co   | 200426097 |
| Shiomar Alberto Salazar Castillo | s.salazarc@uniandes.edu.co    | 202213359 |

## Lanzar Gitpod

<a href="https://shiomarsala-misw4406202-41tvrrfj7bl.ws-us108.gitpod.io/" style="padding: 10px;">
    <img src="https://gitpod.io/button/open-in-gitpod.svg" width="150" alt="Push" align="center">
</a>
<br/><br/>


### Estructura del proyecto

1. Este proyecto fue creado usando un fork del tutorial #5 de clase obtenido del siguiente [enlace](https://github.com/MISW4406/tutorial-5-cqrs-eventos)
2. El codigo fuente del servicio implementado puede verse en la siguiente estructura:

```
├── .gitignore
├── .gitpod.yml
├── adaptador.Dockerfile
├── docker-compose.Dockerfile
├── notificacion.Dockerfile
├── notificacion-requirements.txt
├── propiedadesalpes.Dockerfile
├── pyproject.toml
├── README.md
├── requirements.txt
├── sidecar-requirements.yml
├── ui-requirements.yml
├── ui.Dockerfile
└── src
    ├── ui
    ├── sidecar
    ├── propiedadesalpes
        ├── __init__.py
        ├── api
            ├── __init__.py
            └── companias.py
        ├── config
            ├── __init__.py
            ├── db.py
            └── uow.py
        ├── modulos
            ├── __init__.py
            └── companias
                ├── __init__.py
                ├── aplicacion
                    ├── __init__.py
                    ├── dto.py
                    ├── handlers.py
                    ├── mapeadores.py
                    ├── servicios.py
                    ├── comandos
                        ├── __init__.py
                        ├── base.py
                        └── registrar_comapnias.py
                    └── queries
                        ├── __init__.py
                        ├── base.py
                        └── obtener_companias.py
                ├── dominio
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
                            └── eventos.py          
        └── seedwork
            ├── __init__.py
            ├── aplicacion
                ├── __init__.py
                ├── comandos.py
                ├── dto.py
                ├── hablder.py
                ├── queries.py
                ├── comandos.py
                └── servicios.py
            ├── dominio
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
            ├── infraestructura
                ├── __init__.py
                ├── uow.py
                ├── utils.py
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
    └── notificaciones
        ├── __init__.py
        └── main.py
```

### Escenarios de Calidad Seleccionados

#### Esceneario de Calidad #1: Desempeño
![image](https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3/assets/111320185/52eff4a1-20c8-40da-85b9-d627c5c3b4f9)

#### Esceneario de Calidad #2: Disponibilidad
![image](https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3/assets/111320185/c6d25f10-3638-4dbf-9768-8f69655add90)

#### Esceneario de Calidad #2: Seguridad
![image](https://github.com/shiomar-salazar/MISW4406-202411-Entrega-3/assets/111320185/42f7a336-0f69-44de-a43c-f2adaed72240)

### Pasos para la Ejecucion de la Aplicación

Para desplegar toda la arquitectura en un solo comando, usamos `docker-compose`. Para ello, desde el directorio principal, ejecute el siguiente comando:

```bash
docker-compose up
```

Si desea detener el ambiente ejecute:

```bash
docker-compose stop
```

En caso de querer desplegar dicha topología en el background puede usar el parametro `-d`.

```bash
docker-compose up -d
```

### Video de la Entrega 3
