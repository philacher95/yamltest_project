from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Email


app = Flask(__name__)

app.config["SECRET_KEY"] = "thisisasecret"

class contact(FlaskForm):
    name = StringField("Full Name", validators=[InputRequired("Input required.")])
    email = StringField("Email", validators=[InputRequired("Input required."), Email(message="This Email is Invalid.")])
    phone = IntegerField("Phone Number", validators=[InputRequired("Input required.")])
    comment = TextAreaField("Message", validators=[InputRequired("Input required.")])


@app.route("/", methods=["GET", "POST"])
def index():
    form = contact()
    if form.validate_on_submit():
        pass
    return render_template("index.html", form=form)

@app.route("/<pages>")
def scroll(pages):
    pass


if __name__ == "__main__":
    app.run(debug=True)