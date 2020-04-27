from flask import Blueprint, request, render_template, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

from app.myglobals import filemgrfolder

blue_filemgr = Blueprint('blue_filemgr', __name__, url_prefix='/filemgr')



@blue_filemgr.route('/')
@blue_filemgr.route('/index')
def vf_index():
    invisibles = ['.keep', '.gitkeep']
    filelist = os.listdir(filemgrfolder)
    for filename in invisibles:
        if filename in filelist:
            filelist.remove(filename)
        else:
            continue
    return render_template('filemgr_index.html', filelist=filelist)

@blue_filemgr.route('/download', methods=['GET'])
def cmd_download():
    filename = request.args.get('filename')
    return send_from_directory(filemgrfolder, filename, as_attachment=True)


@blue_filemgr.route('/view', methods=['GET'])
def cmd_view():
    filename = request.args.get('filename')
    return send_from_directory(filemgrfolder, filename, as_attachment=False)

@blue_filemgr.route('/delete', methods=['GET'])
def cmd_delete():
    filename = request.args.get('filename')
    sourcefile = os.path.join(filemgrfolder, filename)
    os.remove(sourcefile)
    return redirect(url_for('blue_filemgr.vf_index'))

@blue_filemgr.route('/upload', methods=['POST'])
def cmd_upload():
    file = request.files['file']
    if file.filename == '':
        flash('请选择文件!')
    if file:
        filename = secure_filename(file.filename)
        destfile = os.path.join(filemgrfolder, filename)
        file.save(destfile)
        # os.chmod(destfile, stat.S_IROTH)
        # os.chmod(destfile, 0o777)
        flash('文件导入成功!')
    return redirect(url_for('blue_filemgr.vf_index'))

