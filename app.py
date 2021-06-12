from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/bokeh')
def bokeh():
    return render_template('bokeh.html')


if __name__ == '__main__':
    app.run(port=33507)
