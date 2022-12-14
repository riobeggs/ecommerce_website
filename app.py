from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import models

engine = create_engine("sqlite:///test.sqlite", echo=True, future=True)

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def create_address():
    if request.method == "POST":

        with Session(engine) as session:

            user = models.Address(
                street=request.form["street"],
                suburb=request.form["suburb"],
                city=request.form["city"],
                postal_code=request.form["postal_code"],
                country=request.form["country"],
            )

            session.add(user)

            session.commit()

            return "Success"

    return render_template("create_address.html")


if __name__ == "__main__":
    app.run(debug=True)
