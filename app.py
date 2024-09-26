from flask import Flask,render_template,request,redirect
from controller import jsonData,insert_data
import json


app=Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/select',methods=['GET'])
def select():
  
    data=jsonData()

    return render_template('select.html',data=data)

@app.route('/book',methods=['GET','POST'])
def book():

    if request.method=='POST':
        form={
        "name":request.form.get('name'),
        " age":request.form.get('age'),
        "gender":request.form.get('gender'),
        "class":request.form.get('class')
        }
        
        insert_data(form=form)

        return redirect('/instruction')
        
    return render_template('book.html')

@app.route('/instruction',methods=['GET'])
def instruct():
    return render_template('instruction.html')




if __name__=='__main__':
    app.run(debug=True,port=5000)