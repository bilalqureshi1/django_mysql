# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:42:25 2021

@author: bqure
"""


from flask import Flask

app = Flask(__name__)
app.secret_key = "secret key"