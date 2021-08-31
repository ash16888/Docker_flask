from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://cdn.trinixy.ru/uploads/posts/2021-06/1623078510_demotivatory_06.jpg",
    "https://cdn.trinixy.ru/uploads/posts/2021-08/1630338534_demotivatory_19.jpg",
    "https://cdn.trinixy.ru/uploads/posts/2021-06/1622813435_demotivatory_20.jpg",
    "https://cdn.trinixy.ru/uploads/posts/2021-04/1618328142_demotivatory_16.jpg",
    "https://cdn.trinixy.ru/pics6/20210331/210185_13_trinixy_ru.jpg",
    "https://cdn.trinixy.ru/pics6/20210205/207764_3_trinixy_ru.jpg",
    "https://cdn.trinixy.ru/uploads/posts/2020-10/1603120423_demotivatory_14.jpg",
    "https://cdn.trinixy.ru/uploads/posts/2020-07/1595338156_demotivatory_15.jpg",

    ]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
