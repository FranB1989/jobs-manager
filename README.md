# Gestor de Jobs en Control-M

Este repositorio contiene una aplicación desarrollada en Python y Django que se encarga de gestionar los jobs ejecutados en un planificador tipo Control-M.

## Descripción

La aplicación proporciona una interfaz web para administrar y monitorear los jobs programados en Control-M. Permite a los usuarios realizar diversas acciones como crear, editar, eliminar y programar jobs, así como también visualizar el estado y el historial de ejecución de los mismos.

## Características

- Interfaz web intuitiva para la gestión de jobs en Control-M.
- Funcionalidades de CRUD (Crear, Leer, Actualizar y Eliminar) para jobs.
- Programación de jobs con parámetros personalizados.
- Visualización del estado actual y el historial de ejecución de los jobs.
- Integración con el sistema de autenticación de Django para la gestión de usuarios y permisos.

## Requisitos

- Python >= 3.x
- Django >= 3.x
- Control-M API (Se requiere configuración adecuada para la comunicación con el planificador Control-M)

## Instalación

1. Clona este repositorio en tu máquina local:

    ```
    git clone https://github.com/FranB1989/jobs-manager.git
    ```

2. Instala las dependencias del proyecto utilizando pip:

    ```
    pip install -r requirements.txt
    ```

3. Configura las variables de entorno necesarias, como la conexión a la API de Control-M.

4. Ejecuta las migraciones de la base de datos:

    ```
    python manage.py migrate
    ```

5. Inicia el servidor de desarrollo:

    ```
    python manage.py runserver
    ```

6. Accede a la aplicación desde tu navegador web utilizando la URL proporcionada por Django.

## Uso

Una vez que la aplicación esté en funcionamiento, puedes iniciar sesión con tus credenciales de usuario y comenzar a gestionar los jobs en Control-M a través de la interfaz web proporcionada.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit de ellos (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request en el repositorio original.

## Licencia

Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT).
