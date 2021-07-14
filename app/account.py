from app import app
from .models import db
from flask.helpers import url_for
from flask import Flask, redirect, render_template, request, session, flash


@app.route('/wallet', methods=['GET', 'POST'])
def wallet():
  return 'top up the wallet'