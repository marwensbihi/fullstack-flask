from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)
app.run(host='0.0.0.0', port=3000)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-scala', methods=['POST'])
def run_scala():
    # Get the Scala code from the form data
    scala_code = request.form['scala_code']

    # Write the Scala code to a file
    with open('scala_script.scala', 'w') as f:
        f.write(scala_code)

    # Run the Scala script and capture its output
    result = subprocess.run(['scala', 'scala_script.scala'], capture_output=True, text=True)

    # Return the result to the user
    return render_template('index.html', result=result.stdout)

if __name__ == '__main__':
    app.run(debug=True)
