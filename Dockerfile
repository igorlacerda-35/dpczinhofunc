FROM rasa/rasa:3.5.2

WORKDIR /app

COPY . /app

USER root

RUN pip install --no-cache-dir -r requirements.txt

CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug"]
