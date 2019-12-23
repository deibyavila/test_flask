# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
#from contact_model import Contact
app = Flask(__name__)


@app.route(r'/', methods=['GET'])
def contact_book():
    return render_template('agenda.html')


@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():

    if request.form:
        print(request.form.get('name'))
        print(request.form.get('phone'))
        print(request.form.get('email'))

    return render_template('add_contact.html')



if __name__ == '__main__':
    app.run()