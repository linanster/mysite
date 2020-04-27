from flask import Blueprint, request, render_template, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

from app.myglobals import filezillafolder

blue_filezilla = Blueprint('blue_filezilla', __name__, url_prefix='/filezilla')



@blue_filezilla.route('/')
@blue_filezilla.route('/index')
def vf_index():
    invisibles = ['.keep', '.gitkeep']
    filelist = os.listdir(filezillafolder)
    for filename in invisibles:
        if filename in filelist:
            filelist.remove(filename)
        else:
            continue
    return render_template('filezilla_index.html', filelist=filelist)

@blue_filezilla.route('/<string:filename>', methods=['GET'])
def vf_view(filename):
    return send_from_directory(filezillafolder, filename, as_attachment=False)

@blue_filezilla.route('/download', methods=['GET'])
def cmd_download():
    filename = request.args.get('filename')
    return send_from_directory(filezillafolder, filename, as_attachment=True)


@blue_filezilla.route('/view', methods=['GET'])
def cmd_view():
    filename = request.args.get('filename')
    return send_from_directory(filezillafolder, filename, as_attachment=False)

@blue_filezilla.route('/delete', methods=['GET'])
def cmd_delete():
    filename = request.args.get('filename')
    sourcefile = os.path.join(filezillafolder, filename)
    os.remove(sourcefile)
    return redirect(url_for('blue_filezilla.vf_index'))

@blue_filezilla.route('/upload', methods=['POST'])
def cmd_upload():
    file = request.files['file']
    if file.filename == '':
        flash('no file selected!')
    if file:
        filename = secure_filename(file.filename)
        destfile = os.path.join(filezillafolder, filename)
        file.save(destfile)
        # os.chmod(destfile, stat.S_IROTH)
        # os.chmod(destfile, 0o777)
        flash('file upload success!')
    return redirect(url_for('blue_filezilla.vf_index'))

