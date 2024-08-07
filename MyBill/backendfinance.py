
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) #instance of the flask class
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app) #db is instance of sqlalchemy class

class myspending(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    category = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self) -> str:
        return f"expense {self.id}"


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method =="POST":
        amount = request.form.get('amount')
        category = request.form.get('category') 
        expense = myspending(amount= amount, category= category)
        try:
            db.session.add(expense)
            db.session.commit()
            return redirect ('/')
        except Exception as e:
            print(f"ERROR:{e}")
            return f"ERROR:{e}"

    
    expenses = myspending.query.order_by(myspending.created).all()    
    return render_template('index.html', expenses= expenses)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id:int):
    updatedexpense = myspending.query.get_or_404(id)
    if request.method == "POST":
           amount = request.form.get('amount')
           category = request.form.get('category')
           try:
               updatedexpense.amount = amount
               updatedexpense.category = category
               db.session.commit()
               return redirect('/')
           except Exception as e:
               return f"Error(e)"
    else: 
      return render_template('update.html', amount=updatedexpense.amount, category=updatedexpense.category, expense=updatedexpense )

@app.route('/delete/<int:id>', methods=['POST'])    
def delete(id:int):
    delete_expense =myspending.query.get_or_404(id)
    try:
        db.session.delete(delete_expense)
        db.session.commit()
        return redirect('/')

    except Exception as e:
        return f"ERROR:{e}" 









if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

