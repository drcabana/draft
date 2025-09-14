from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    selection = None
    output = None
    error = None
    if request.method == 'POST':
        selection = request.form.get('query_choice')
        if selection:
            try:
                result = subprocess.run(
                    ['python', 'boorda.py', f'{selection}'],
                    capture_output=True,
                    text=True,
                    timeout=5  # Prevent long-running scripts
                )
                output = result.stdout
                error = result.stderr if result.stderr else None
            except subprocess.TimeoutExpired:
                error = "Error: Program took too long to execute."
            except FileNotFoundError:
                error = f"Error: {selection}.py not found."
            except Exception as e:
                error = f"Error: {str(e)}"
    return render_template("index.html", selection=selection, output=output, error=error)

if __name__ == '__main__':
    app.run(debug=True)