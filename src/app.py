from flask import Flask, flash, request, redirect, render_template, url_for
 

 
app = Flask(__name__)



  

users = {}
book = {}
liblary = {}
 

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/register')
def register_template():       
    return render_template("register.html")


@app.route('/login')
def login_template():
    return render_template("login.html")

@app.route('/boroow')
def boroow():
    return render_template("boroow.html")
 

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        


        for user in users:
            if users[user]['name'] == name and users[user]['password'] == password:
                return redirect(url_for('viewbooks'))
        
                error = 'invalid credentials.Please try again.'
        
    return render_template('viewbooks.html', error=error)

 
@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        passwordagain = request.form['passwordagain']

        id = len(users) + 1
        
    

        users[id] = { 'name': name, 'password': password, 'email': email, 'passwordagain': passwordagain}
         


    return render_template('login.html')
 

@app.route('/viewbooks', methods=['GET'])
def books_template():
    if book == True:
        return redirect(url_for('boroow'))
    
        
    return render_template('viewbooks.html', liblary=liblary)

@app.route('/addbook', methods=['POST'])
def addbook():
    author = request.form['author']
    description = request.form['description']
    title = request.form['title']

    id = len(liblary) + 1
    
    liblary[id] = {'author': author, 'description': description, 'title': title}
    return redirect(url_for('books_template'))
      

 
 
if __name__ == '__main__':
    app.run(debug = True)