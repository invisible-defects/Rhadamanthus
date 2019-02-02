# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return "Ну здравствуй."

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', title='Ваша лодка уже готова', form=form)