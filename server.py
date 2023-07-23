import csv
from flask import Flask, render_template,url_for, request, redirect

app = Flask(__name__) #creating an instance of this class in the main file, because __name__ = __main__

@app.route("/")
def home_page():
    return render_template('index.html') #To run this we will need to put our html file in templates folder

@app.route("/<string:page_name>")
def go_to_page(page_name):
    return render_template(page_name) 


def write_to_file(data):
    with open('database.txt', mode='a') as database: #to read and write to a file
        email = data["email"] #taking info from dictionary(key:value pairs)
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email};{subject};{message}')


def write_to_csv(data):
    with open('database.csv', mode='a',newline='') as database2:
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',',quotechar='"' ,quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])   #GET means the browser wants us to get information, POST means the browser wants us to save information
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict() #will get data from form and store into a dictionary
        write_to_csv(data)
        return redirect('/thankyou.html') #will redirect us to thankyou.html after we submit the form
    else:
        return 'something went wrong'
