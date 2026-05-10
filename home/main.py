from flask import Flask, render_template , request
from database import connect_to_database


app = Flask(__name__)   

@app.route('/')
def home(): 
    return render_template('home.html')


@app.route('/home.html')
def homepage(): 
    return render_template('home.html')


@app.route('/enquire', methods=['POST'])
def add_enquiry():
    email = request.form['email']
    description = request.form['description']

    conn = connect_to_database()
    if conn is None:
        return "Database connection failed"

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO enquire (email, description) VALUES (%s, %s)",
        (email, description)
    )
    conn.commit()
    cur.close()
    conn.close()
    return f"Thanks {email}, your enquiry has been submitted!"



@app.route('/current-openings.html')
def current_openings():
    return render_template('current-openings.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
