# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, MainForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = MainForm()
    if form.validate_on_submit():
        print("Gotcha")
        return redirect(url_for('index'))
    return render_template('index.html', title='Логово Радаманта', form=form, karma=0)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', title='Ваша лодка уже готова', form=form)