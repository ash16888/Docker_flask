# забираем из образа 
FROM python:slim

# устанавливаем директорию для приложения
WORKDIR /usr/src/app

# копируем файлы в контейнер
COPY . .

# устанавливаем flask

RUN pip install flask

# какой порт будет слушать контейнер
EXPOSE 5000

# запускаем приложение

CMD ["python", "./app.py"]
