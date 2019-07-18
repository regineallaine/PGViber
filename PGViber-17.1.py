from flask import Flask, render_template, request, redirect, url_for
import pymysql



app = Flask(__name__)


@app.route('/retrieve', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        empnum = request.form['employeenumber']
        return redirect(url_for('edit',empid=empnum))
    

@app.route('/employee/<int:empid>', methods=['GET', 'POST'])
def edit(empid):
    if request.method == 'GET':
        empnum = empid
        # # print ("Connection Established")
        sql="select * from employees where employee_number=%s"
        # # try:
        conn = pymysql.connect(host="localhost", user="root", passwd="1234", database="db_info")
        B_cur=conn.cursor()
        B_cur.execute(sql, empnum)
        row = B_cur.fetchone()
        #     # for B in B_cur:
        print(row)
        employeenumber = row[0]
        emailaddress = row[1]
        pas = row[2]
        lname = row[3]
        fname = row[4]
        gend = row[5]
        phone = row[6]
        bday = row[7]

        conn.commit()
        return render_template('PGViber-17.2.html', a1=employeenumber, a2=emailaddress, a3=pas, a4=lname, a5=fname, a6=gend, a7=phone, a8=bday)
    else:

# @app.route('/update', methods=["POST"])
# def update():
        empnum = empid
        # # print ("Connection Established")
        phonenumber = request.form['phonenumber']
        gender = request.form['gender']
        lastname = request.form['lastname']
        firstname = request.form['firstname']
        # employeenumber = request.form['employeenumber']
        emailaddress = request.form['emailaddress']
        password = request.form['password']
        # sql="UPDATE employees SET last_name = '" + lastname +"' WHERE employee_number = %s;"
        conn = pymysql.connect(host="localhost", user="root", passwd="1234", database="db_info")
        B_cur=conn.cursor()
        B_cur.execute("UPDATE employees SET email_address=%s, password=%s, last_name=%s, first_name=%s, gender=%s, mobile_number=%s WHERE employee_number=%s", (emailaddress,password,lastname,firstname,gender,phonenumber,empnum))
        
        # B_cur.close()
        
        # return "Success"

        # print(row)
        # employeenumber = row[0]
        # emailaddress = row[1]
        # pas = row[2]
        # lname = row[3]
        # fname = row[4]
        # gend = row[5]
        # phone = row[6]
        # bday = row[7]
        conn.commit()
        return redirect(url_for('edit',empid=empnum))
        # return render_template('PGViber-17.2.html', a1=employeenumber, a2=emailaddress, a3=pas, a4=lname, a5=fname, a6=gend, a7=phone, a8=bday)


if __name__ =='__main__':
    app.run(debug=True)
