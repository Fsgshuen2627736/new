#cgpa
from flask import Flask, request, render_template

app = Flask(__name__)

# Function to convert grades to points
def default_grade(grade):
    if grade == 'O':
        return 10
    elif grade == 'A+':
        return 9
    elif grade == 'A':
        return 8
    elif grade == 'B+':
        return 7
    elif grade == 'B':
        return 6
    elif grade == 'C':
        return 5
    elif grade == 'U' or grade == 'SA' or grade == 'W' or grade == 'WH':
        return 0
    else:
        return None

# Route for home page
@app.route('/')
def welcome():
    return render_template('index.html')

# Route for SGPA calculation
@app.route('/calculate_sgpa', methods=['POST'])
def calculate_sgpa():
    maths = default_grade(request.form['maths'].upper())
    ids = default_grade(request.form['ids'].upper())
    dbms = default_grade(request.form['dbms'].upper())
    cn = default_grade(request.form['cn'].upper())
    jp = default_grade(request.form['jp'].upper())
    asd = default_grade(request.form['asd'].upper())
    jp_lab = default_grade(request.form['jp_lab'].upper())
    dbms_lab = default_grade(request.form['dbms_lab'].upper())
    ss2 = default_grade(request.form['ss2'].upper())

    # SGPA Calculation
    gpa = (4 * maths) + (3 * ids) + (3 * dbms) + (3 * cn) + (3 * jp) + (4 * asd) + (2 * jp_lab) + (2 * dbms_lab) + (1 * ss2)
    sgpa = gpa / 25

    return f'SGPA: {sgpa:.2f}'

# Route for CGPA calculation
@app.route('/calculate_cgpa', methods=['POST'])
def calculate_cgpa():
    sem1 = float(request.form['sem1'])
    sem2 = float(request.form['sem2'])
    sem3 = float(request.form['sem3'])
    sem4 = float(request.form['sem4'])

    # CGPA Calculation
    cgpa = (sem1 + sem2 + sem3 + sem4) / 4

    return f'CGPA: {cgpa:.2f}'

if __name__ == '__main__':
    app.run(debug=True)
