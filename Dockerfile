FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1   
ENV PYTHONUNBUFFERED=1  

WORKDIR /app


COPY requirements.txt /app/  

RUN pip3 install --upgrade pip  
RUN pip3 install -r requirements.txt  

COPY ./core /app/  

# sudo docker run -p 8000:8000 django