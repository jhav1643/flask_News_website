from flask import Flask, render_template, request
import requests
app = Flask(__name__);

@app.route('/')
def home():
    url = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=848dabf0a04f4aeca99cd3b15474993b");
    r = url.json(); 

    cases = {
        'articles' : r['articles']
    }

    return render_template('index.html', case = cases);

if __name__ == '__main__':
    app.run(debug=True, port=5000);