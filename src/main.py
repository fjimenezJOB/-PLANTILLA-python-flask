# inicializando
from flask import Flask, redirect, render_template, request

app=Flask(__name__)

# rutas
@app.route('/')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run('0.0.0.0',5000,debug=True)