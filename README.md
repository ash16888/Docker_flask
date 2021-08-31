Пример  Docker контейнера с веб приложением на фреймворке  flask языка Python. 

Создаем образ

`docker build -t .`

Запускаем контейнер

`docker run -p 8888:5000 flask_app`

Для примера в папке examples три варианта Dockerfile
сравним размеры полчившихся образов  Docker 

* Alpine/Python 67.3 Мб
* Python slim 133 МБ
* Ubuntu  415 МБ
