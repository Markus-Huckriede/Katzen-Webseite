from flask import Flask, render_template, redirect, url_for
import requests
import random

app = Flask(__name__)

def get_cat_image():
    try:
        res = requests.get("https://api.thecatapi.com/v1/images/search")
        res.raise_for_status()
        return res.json()[0]['url']
    except:
        return "/static/fallback-cat.jpg"

@app.route('/')
def home():
    cat_url = get_cat_image()
    return render_template("index.html", cat_url=cat_url)

@app.route('/mehr-katzen')
def more_cats():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
