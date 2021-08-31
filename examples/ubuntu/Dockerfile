# образ 
FROM ubuntu:latest

# установка директории приложения
WORKDIR /usr/src/app

# устанавливаем python  и pip
RUN apt-get update && apt-get install -y  python3  && apt-get install python3-pip -y 

# копируем файлы  в директорию

COPY . .

# установим flask

RUN pip install flask

# порт контейнера который он будет "слушать"
EXPOSE 5000

# запуск приложения
CMD ["python3", "./app.py"]
