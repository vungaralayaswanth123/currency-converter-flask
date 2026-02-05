from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url).json()
        rate = response['rates'][to_currency]
        result = amount * rate

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
