#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///store.db"
db = SQLAlchemy(app)

class InputData(db.Model):
  id = db.Column(db.Integer, primary_key=True , autoincrement=True)
  date = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
  Cost = db.Column(db.Integer, nullable=True)
  Paytm = db.Column(db.Integer, nullable=True)
  Total = db.Column(db.Integer, nullable=True)

@app.route("/", methods=["GET", "POST"])
def hello_world():
  if request.method=="POST":
    Cost = int(request.form['Cost'])
    Paytm = int(request.form['Paytm'])
    Total = Cost + Paytm

    with app.app_context():
            data = InputData(Cost=Cost, Paytm=Paytm, Total=Total)
            db.session.add(data)
            db.session.commit()

  with app.app_context():
        data = InputData.query.all()
        print(len(data))
        print(data)

  return render_template("index.html", data=data)

@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    # Find the data record to delete by its ID
    data_item = InputData.query.get(item_id)

    if data_item:
        # Delete the data record from the database
        db.session.delete(data_item)
        db.session.commit()

    # Redirect back to the homepage after deletion
    return redirect(("/"))

if __name__ == "__main__":
  with app.app_context():
        db.create_all()
  app.run(debug=True)  # host='127.0.0.1', port=5000)
