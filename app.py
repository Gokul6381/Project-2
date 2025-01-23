from flask import Flask,render_template,request,redirect,session,flash,url_for
from controller import jsonData,insert_data,insert,redrive_1,redrive_all
import os
from datetime import datetime


app=Flask(__name__)
app.secret_key= os.urandom(24)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/',methods=['GET','POST'])
def index():
    try:
        return render_template('Home.html')
    except Exception as err:
        print(str(err))
        return redirect('/error')


@app.route('/register',methods=['GET','POST'])
def register():
    try:

        if request.method=='POST':

            
            form={
                "name":request.form.get('name'),
                "phone":request.form.get('phone'),
                "email":request.form.get('email'),
                "user":request.form.get('user'),
                "password":request.form.get('userPass'),
                "reg_date":str(datetime.now())
            }
            try:
                query=f"insert into users(user_id,password,name,phone,email) values('{form['user']}','{form['password']}','{form['name']}','{form['phone']}','{form['email']}');"
                insert(query=query)
                file=r"user_details.json"
                insert_data(form=form,file=file)
            except Exception as err:
                print(str(err))

            return redirect('/login')
        return render_template('Register.html')

    except Exception as err:
        print(str(err))
        return redirect('/error')


@app.route('/login',methods=['GET','POST'])
def login():
    try:
        if request.method=='POST':
            form={
                "user":request.form.get('user'),
                "password":request.form.get('userPass')
            }

            query=f"select *from users where user_id='{form['user']}' and password='{form['password']}';"
            user=redrive_1(query=query)
            session['users']=user


            if user:
                session['loggedin'] = True
                session['user'] = form['user']
                session['name']=user[2]
                return redirect(url_for('profile') )
            else:
                flash('Incorrect username or password!','danger')
                
        return render_template('login.html')

    except Exception as err:
        print(str(err))
        return redirect('/error')

@app.route('/profile',methods=['GET','POST'])
def profile():
    try:
        if request.method=='POST':
            form={
                    "name":request.form.get('name'),
                    "phone":request.form.get('phone'),
                    "email":request.form.get('email'),
                    "user":request.form.get('user'),
                    "password":request.form.get('userPass'),
                    "reg_date":str(datetime.now())
                }
            query=f"""UPDATE users set name="{form['name']}",phone="{form['phone']}",email="{form['email']}",password="{form['password']}" WHERE user_id="{session['user']}";"""
            insert(query=query)
            print("Update Successfully")
            

        profile=session['users']    
        query=f"select b.booking_id,b.name,b.age,b.gender,b.class,f.* FROM flight_data as f INNER JOIN booking as b on f.flight_id=b.flight_id INNER JOIN users as u ON b.user_id=u.user_id WHERE u.user_id='{session['user']}';"
        history=redrive_all(query=query)
        print(history)
        if history:        
            return render_template('profile.html', profile=profile, history=history)
        else:
            return render_template('profile.html', profile=profile)

       
    
    except Exception as err:
        print(str(err))
        return redirect('/error')


@app.route('/available',methods=['GET','POST'])
def available():
    try:
        # data=jsonData()
        query=f"select *from flight_data;"
        data=redrive_all(query=query)

        if request.method == 'POST':
            flight_id = request.form.get('flight_id')

            session['flight_id']=flight_id
            return redirect('/passenger')

        return render_template('FlightList.html',data=data)

    except Exception as err:
        print(str(err))
        return redirect('/error')




@app.route('/passenger',methods=['GET','POST'])
def book():
    try:
        if request.method=='POST':
            form={
            "flight_id":session['flight_id'],
            "user":session['user'],    
            "name":request.form.get('name'),
            "age":request.form.get('age'),
            "gender":request.form.get('gender'),
            "class":request.form.get('class'),
            "book_date":str(datetime.now())
            }
            try:
                query=f"insert into booking(flight_id,user_id,name,age,gender,class) values('{form['flight_id']}','{form['user']}','{form['name']}','{form['age']}','{form['gender']}','{form['class']}');"
                insert(query=query)
                file=r"Book_data.json"
                insert_data(form=form,file=file)
                return redirect('/success')
            except Exception as err:
                print(str(err))
                return redirect('/error')

            
            
        return render_template('Passanger.html')
    except Exception as err:
        print(str(err))
        return redirect('/error')
 


@app.route('/success',methods=['GET'])
def success():
    try:
        return render_template('success.html')
    except Exception as err:
        print(str(err))
        return redirect('/error')


@app.route('/error',methods=['GET'])
def error():
    return render_template('404.html')



if __name__=='__main__':
    # app.run(debug=True,host='0.0.0.0',port=5000)
    app.run(debug=True)