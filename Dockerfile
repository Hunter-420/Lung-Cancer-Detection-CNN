FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY . .

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

EXPOSE 12000

CMD ["python", "api.py"]

