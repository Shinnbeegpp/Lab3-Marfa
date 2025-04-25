from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        title = request.form['Name']
        message = request.form['message']
        return render_template('message_sent.html', title=title)  
    return render_template('contacts.html')  

if __name__ == '__main__':  
    app.run(debug=True)
