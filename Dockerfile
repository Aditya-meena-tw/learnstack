FROM python:3-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /learnstack

COPY requirements.txt /learnstack/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && \
    unzip ngrok-stable-linux-amd64.zip && \
    mv ngrok /usr/local/bin/

EXPOSE 4040

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
