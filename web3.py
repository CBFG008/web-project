from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)

@app.route('/' )
def index():
    return render_template('index.html')

def write_to_csv(data):
    with open ('web3.CSV', mode='a') as Database:
        email = data ["email"]
        name = data ["name"]
        subject = data ["subject"]
        message = data ["message"]
        csv_writer = csv.writer(Database , delimiter= ',' , quotechar='"' , quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,name,subject,message])

@app.route('/web3.py', methods=['POST', 'GET'])
def html_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)    
        return "form submitted"
    else:
        return "went wrong"

if __name__ == '__main__':
    app.run(debug=True)