from flask import Flask, render_template, request
from truth_table_generator import TruthTable

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    values = request.form.get('values', '')
    data = []
    for char in str(values):
        if char.isalpha():
            if char not in data and len(data) < 4:
                data.append(char.upper())
    nums = [x for x in range(2 ** len(data))]
    table = TruthTable(data)
    data = table.sort_columns()
    return render_template('homepage.html', table=table.logic_table(),
                           data=data, nums=nums)

if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1')
