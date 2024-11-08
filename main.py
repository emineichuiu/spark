# spark Dockerfile

FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main"]

# Code Update 1760617529-7983

# Additional Implementation 1760617529
