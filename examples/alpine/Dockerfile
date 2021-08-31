# На основе  Alpine Linux image https://hub.docker.com/r/frolvlad/alpine-python3/
FROM frolvlad/alpine-python3

# Устанвливаем рабочую директорию
WORKDIR /usr/src/app

# копируем файлы в контейнер
COPY . .

#  Устанавливаем flask через  pip
RUN pip install flask

# номер порта который контейнер будет слушать
EXPOSE 5000

# запускаем
CMD ["python", "./app.py"]
