# PDF to Markdown

Aplicación web para convertir archivos PDF a Markdown de forma sencilla desde el navegador.

## Qué hace

- Permite subir un archivo PDF.
- Convierte el contenido a Markdown.
- Muestra una vista previa del resultado.
- Permite descargar el texto convertido como archivo `.md`.

## Requisitos

- Python 3.11 o superior
- Docker, si prefieres ejecutar la aplicación en contenedor

## Ejecutar en local

1. Instala las dependencias:

```bash
pip install -r requirements.txt
```

2. Inicia la aplicación:

```bash
streamlit run pdf2md.py --server.address=0.0.0.0 --server.port=8502
```

3. Abre la aplicación en tu navegador:

```text
http://localhost:8502
```

## Ejecutar con Docker

Si prefieres usar Docker, puedes ejecutar una imagen publicada en Docker Hub o construirla localmente.

### Usar una imagen de Docker Hub

Descarga la imagen:

```bash
docker pull alejandroromeroa/pdf2markdown:latest
```

Ejecuta el contenedor:

```bash
docker run -d --name pdf2markdown -p 8502:8502 alejandroromeroa/pdf2markdown:latest
```

Luego abre:

```text
http://localhost:8502
```

### Construir la imagen localmente

Si prefieres construirla en tu equipo, usa estos comandos:

```bash
docker build -t pdf2markdown .
docker run -d --name pdf2markdown -p 8502:8502 pdf2markdown
```

## Cómo usar la aplicación

1. Abre la página principal.
2. Sube un archivo PDF.
3. Espera a que termine la conversión.
4. Revisa la vista previa.
5. Descarga el resultado en Markdown si lo deseas.

## Archivos principales

- `pdf2md.py`: aplicación principal.
- `Dockerfile`: definición de la imagen Docker.
- `requirements.txt`: dependencias del proyecto.

## Licencia de dependencias

Este proyecto utiliza `markitdown`, una librería de Microsoft distribuida bajo licencia MIT.

Requisitos y notas importantes:

- `markitdown` requiere Python 3.10 o superior.
- Para la conversión de PDF se usa el extra `markitdown[pdf]`.
- La librería realiza operaciones de entrada y salida con los privilegios del proceso, por lo que conviene usar archivos confiables o validar entradas antes de convertirlas.

## Notas

- El puerto de la aplicación es `8502`.
- La conversión puede tardar más o menos según el tamaño del PDF.
- Si el PDF contiene imágenes o tablas complejas, el resultado puede variar según el contenido original.
