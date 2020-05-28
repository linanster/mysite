from flask import Blueprint, request, render_template, flash, redirect, url_for, send_from_directory
import os
from app.ext.mysocketio import socketio

blue_chat = Blueprint('blue_chat', __name__, url_prefix='/chat')

@blue_chat.route('/')
@blue_chat.route('/index')
def vf_index():
    return render_template('chat_index.html', async_mode=socketio.async_mode)
