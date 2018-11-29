from flask import Flask, render_template

app = Flask(__name__)
@app.route('/<val>/<text>')
def checker(val, text):
    return render_template('index.html', times=int(val), color=(text))

if __name__=="__main__":
    app.run(debug=True)
