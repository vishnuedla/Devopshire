from flask import Flask, render_template , request
from database import connect_to_database , verify_employee

app = Flask(__name__)   


@app.route('/login')
def employee_login(): 
   return render_template('login.html')

@app.route('/employee', methods=['POST'])
def employee_login_post():
    username = request.form['username']
    password = request.form['password']

    if verify_employee(username, password):
        return render_template('admin.html', username=username)
    else:
        return "Invalid credentials. Please try again."


     


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)