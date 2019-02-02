# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, MainForm
from app.rad_db import User
from flask_login import current_user, login_user, logout_user
from app.rad_db import User

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = MainForm()
    if form.validate_on_submit():
        print("Gotcha")
        return redirect(url_for('index'))
    return render_template('index.html', title='Логово Радаманта', form=form, karma=0)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data, surname=form.surname.data).first()
        if user is None:
            flash("Ты не из Поведников, уходи!")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Ваша лодка уже готова', form=form)