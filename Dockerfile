FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz && \
    tar xzf dockerize-linux-amd64-v0.6.1.tar.gz && \
    mv dockerize /usr/local/bin/

COPY . .

EXPOSE 8000

CMD ["dockerize", "-wait", "tcp://mysql-db:3306", "-timeout", "60s", "sh", "-c", ". venv/bin/activate && python main.py"]
