from flask import Flask, render_template, request
from truth_table_generator import TruthTable

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    values = request.form.get('values', '')
    data = []
    for char in values:
        if char.isalpha():
            if char not in data and len(data) < 10:
                data.append(char.upper())
    data.sort()
    table = TruthTable(data)
    nums = []
    for i in range(2 ** len(data)):
        nums.append(i)
    return render_template('homepage.html', table=table.create_table(),
                           data=data, nums=nums)

if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1')
