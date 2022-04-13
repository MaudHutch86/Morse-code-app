from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'potequetu21cq134'
#  data setting
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cypher.db'
# db = SQLAlchemy(app)
Bootstrap(app)


#  input form setting

class MessageForm(FlaskForm):
    message = TextAreaField('Enter your code', validators=[DataRequired()])
    submit = SubmitField('Encode')


class ResultForm(FlaskForm):
    message = TextAreaField('Enter your Morse code', validators=[DataRequired()])
    submit = SubmitField('Decode')


# class cyphered_message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     original_message = db.Column(db.Text, unique=True, nullable=False)
#     encrypted_message = db.Column(db.Text, unique=True, nullable=False)
#

# db.create_all()

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

CODE_REVERSED = {value: key for key, value in CODE.items()}


@app.route("/", methods=["GET", "POST"])
def encrypt():
    form = MessageForm()
    if form.validate_on_submit():
        return ''.join(CODE.get(i.upper()) for i in form.message.data)
    return render_template("index.html", form=form)


@app.route("/decipher", methods=["GET", "POST"])
def decrypt():
    form_r = ResultForm()
    if form_r.validate_on_submit():
        return ''.join(CODE_REVERSED.get(i) for i in form_r.message.data.split())
    return render_template("result.html", form=form_r)


if __name__ == "__main__":
    app.run(debug=True)
