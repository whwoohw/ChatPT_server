FROM python:3.10.8

RUN apt-get update && apt-get install -y tesseract-ocr

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN which tesseract

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
