from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('data_2024.csv')

def rank(df, category):
    boorda = df[['votes', category]]
    result = boorda.groupby(category).sum().sort_values(by='votes',ascending=False)
    if category == 'college' or category == 'pfr_player_name':
        return result.head(20)
    else:
        return result

@app.route('/', methods=['GET', 'POST'])
def index():
    selection = None
    error = None
    output = None
    if request.method == 'POST':
        selection = request.form.get('query_choice')
        if selection:
            try:
                output = rank(df, selection)
            except Exception as e:
                error = f"Error: {str(e)}"
    return render_template("index.html", selection=selection, output=output, error=error)

if __name__ == '__main__':
    app.run(debug=True)