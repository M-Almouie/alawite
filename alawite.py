#!/usr/bin/python3

import os
from flask import Flask, render_template, session, request,redirect
import re, os
from datetime import datetime
import random

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
