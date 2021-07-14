from app import app
from .models import db
from flask.helpers import url_for
from flask import Flask, redirect, render_template, request, session, flash

@app.route('/wallet', methods=['GET', 'POST'])
def wallet():
  return 'top up the wallet'


@app.route('/password', methods=['GET', 'POST'])
def password():
  return 'change password'


@app.route('/delete', methods=['GET', 'POST'])
def delete():
  return 'Delete account'