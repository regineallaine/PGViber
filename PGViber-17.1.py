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
        empnum = empid
        # # print ("Connection Established")
        sql="UPDATE employees SET email='cj was here' WHERE employee_number = %s;"
        # # try:
        conn = pymysql.connect(host="localhost", user="root", passwd="1234", database="db_info")
        B_cur=conn.cursor()
        B_cur.execute(sql, empnum)
        B_cur.close()
        conn.commit()
        return "Success"
    # def getvaluenew():    
#     empnum = [(request.form['empnum'])]
#     conn = pymysql.connect(host="localhost", user="root", passwd="1234", database="db_info")
#     B_cur=conn.cursor()
#     sql="UPDATE employees SET password=%s last_name='%s', first_name=%s, birthdate='%s' gender='%s', mobile_number=%s WHERE employee_number = %s ",
#     (password.get(), lastname.get(), firstname.get(), gender.get(), birthday.get(), phonenumber.get())
#     B_cur.execute(sql)
        
#     conn.commit()    
#     return render_template('PGViber-17.2.html', a1=employeenumber, a2=emailaddress, a3=pas, a4=lname, a5=fname, a6=gend, a7=phone, a8=bday)
def update_employees():
    # read database configuration
    db_info = read_db_info()

    sql = """ UPDATE employees
                SET email = %s, password = %s, last_name = %s, first_name = %s, birthdate = %s, gender = %s, mobile_number = %s
                WHERE employee_number = %s """
 
    data = (email, password, last_name, first_name, birthdate, gender, mobile_number)
 
    try:
        conn = MySQLConnection(**db_info)
 
        # update book title
        cursor = conn.cursor()
        cursor.execute(sql, data)
 
        # accept the changes
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()

if __name__ =='__main__':
    app.run(debug=True)



# def clear():
#         empnum.set('')
#         name.set('')
#         age.set('')
#         e1.configure(state='normal')


# def add():
#     try:
#         conn = pymysql.connect(host="localhost", user="root", passwd="1234", database="db_details")
#         cur=conn.cursor()
#         sql="insert into employees values=('%s','%s','%s')"\
#             %(empnum.get(), name.get(), age.get())
#         cur.execute(sql)
#         conn.commit()
#         conn.close()
#         messagebox.showinfo('Success','Record saved...')
#     except: 
#         messagebox.showinfo('Error', 'Error in data entry...')
#     finally:
#         clear()

#     def cancel():
#         empnum.set('')
#         name.set('')
#         empid.set('')
#         e1.configure(state='normal')



# def delete():
#     try:
#         conn = pymysql.connect(host="localhost", user="root", passwd="1234", database="db_details")
#         cur=conn.cursor()
#         sql="delete from employees where empnum='%s'"\
#             %(empnum.get())
#         cur.execute(sql)
#         conn.commit()
#         conn.close()
#         messagebox.showinfo('Success','Record deleted...')
#     except: 
#         messagebox.showinfo('Error', 'Error in data entry...')
#     finally:
#         clear()


# w1=Tk()
# w1.title('My App')
# w1.geometry('500x200')
# ptitle=Label(w1, text='''Program to add, delete and modify the 
#                             records from the student student table''')
# ptitle.grid(row=0, column=0, columnspan=2)

# empnum=StringVar()
# name=StringVar()
# age=StringVar()

# l1=Label(w1, text='Empnum')
# e1=Entry(w1, textvariable=empnum)
# l2=Label(w1, text='Name')
# e2=Entry(w1, textvariable=name)
# l3=Label(w1, text='Age')
# e3=Entry(w1, textvariable=age)

# @app.route('/retrieve', methods=['GET', 'POST'])
# def getvalue():
#  empnum = [(request.form['empnum'])]
 
#  print(request.method)
 
#  myCursor.execute("SELECT * FROM employees WHERE empnum=(%s)",empnum)
#  row = myCursor.fetchone()
#  # print(row)
 
#  empnum = row[0]
#  name = row[1]
#  age = row[2]
# #  ln = row[3]
# #  fn = row[4]
# #  gend = row[5]
# #  phone = row[6]
# #  bday = row[7]
 
#  conn.commit()
 
#  return render_template('showdetails.html', a1=empnum, a2=name, a3=age)

# l1.grid(row=1, column=0)
# e1.grid(row=1, column=1)
# b1.grid(row=1, column=2)

# l2.grid(row=2, column=0)
# e2.grid(row=2, column=1)
# l3.grid(row=3, column=0)
# e3.grid(row=3, column=1)
# b2.grid(row=4, column=0)
# b3.grid(row=4, column=1)
# b4.grid(row=5, column=0)
# b5.grid(row=5, column=1)
# w1.mainloop()

