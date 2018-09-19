# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:03:44 2018

@author: C252059
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('button_page.html')

@app.route('/alabama')
def alabama():
    import Alabama
    Alabama.main()
    render_template('button_page.html')

@app.route('/california_one')
def cali_one():
    import CaliforniaStepOne
    from selenium.common.exceptions import WebDriverException
    try:
        CaliforniaStepOne.main()
    except WebDriverException as ex:
    return render_template('button_page.html')

@app.route('/california_two')
def cali_two():
    import CaliforniaSteptwo
        from selenium.common.exceptions import WebDriverException
    try:
        CaliforniaStepTwo.main()
    except WebDriverException as ex:
    return render_template('button_page.html')





@app.route('/prims_request')
def prims_request():
    import PrimsRequest
    from selenium.common.exceptions import WebDriverException
    try:
        PrimsRequest.main()
    except WebDriverException as ex:
        pass
    return render_template('button_page.html')


    