# PDF to Markdown

Web application for converting PDF files into Markdown directly from your browser.

## What it does

- Lets you upload a PDF file.
- Converts the content to Markdown.
- Shows a preview of the converted text.
- Lets you download the result as a `.md` file.

## Requirements

- Python 3.11 or later
- Docker, if you prefer to run the app in a container

## Run locally

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Start the application:

```bash
streamlit run pdf2md.py --server.address=0.0.0.0 --server.port=8502
```

3. Open the app in your browser:

```text
http://localhost:8502
```

## Run with Docker

If you prefer Docker, you can either pull a published image from Docker Hub or build it locally.

### Use the Docker Hub image

Pull the image:

```bash
docker pull alejandroromeroa/pdf2markdown:latest
```

Run the container:

```bash
docker run -d --name pdf2markdown -p 8502:8502 alejandroromeroa/pdf2markdown:latest
```

Then open:

```text
http://localhost:8502
```

### Build the image locally

If you prefer to build it on your machine, use:

```bash
docker build -t pdf2markdown .
docker run -d --name pdf2markdown -p 8502:8502 pdf2markdown
```

## How to use the app

1. Open the main page.
2. Upload a PDF file.
3. Wait for the conversion to finish.
4. Review the preview.
5. Download the Markdown output if you want to keep it.

## Main files

- `pdf2md.py`: main application.
- `Dockerfile`: Docker image definition.
- `requirements.txt`: project dependencies.

## Dependency license

This project uses `markitdown`, a Microsoft library distributed under the MIT License.

Requirements and notes:

- `markitdown` requires Python 3.10 or later.
- PDF conversion uses the `markitdown[pdf]` extra.
- The library performs input and output operations with the privileges of the running process, so it is best to use trusted files or validate untrusted inputs before converting them.

## Notes

- The application runs on port `8502`.
- Conversion time depends on the size of the PDF.
- Results may vary for PDFs with complex layouts, images, or tables.
