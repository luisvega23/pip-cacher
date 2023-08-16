FROM python:3.11.4

LABEL org.opencontainers.image.authors="Luis Vega <vvegem@gmail.com>"

RUN pip install python-pypi-mirror

WORKDIR /pythonCacher

RUN mkdir simple

COPY files/server.py .

EXPOSE 8000

CMD ["python", "/pythonCacher/server.py"]
