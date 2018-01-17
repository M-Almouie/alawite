#!/usr/bin/python3

import os
from flask import Flask, render_template, session, request,redirect
import re, os
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/base', methods=['GET','POST'])
def begin():
    return render_template('base.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
