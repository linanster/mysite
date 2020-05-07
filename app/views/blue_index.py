from flask import Blueprint, request, render_template, flash, redirect, url_for, send_from_directory
import os

from app.views.blue_filezilla import blue_filezilla

blue_index = Blueprint('blue_index', __name__)



@blue_index.route('/')
@blue_index.route('/index')
def vf_index():
    # return "Hello, MySite!"
    return redirect(url_for('blue_filezilla.vf_index')) 
