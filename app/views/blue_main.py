from flask import Blueprint, request, render_template, flash, redirect, url_for, send_from_directory
import os

from app.views.blue_filezilla import blue_filezilla

blue_main = Blueprint('blue_main', __name__)



@blue_main.route('/')
@blue_main.route('/index')
def vf_index():
    return render_template('main_index.html')
