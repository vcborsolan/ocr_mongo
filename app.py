import os
from flask import Flask, render_template, request
from ocr_core import ocr_core
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# define a folder to store and later serve the images
app.config["IMAGE_UPLOADS"] = "static/pdf/"

client = MongoClient('localhost',27017)
db = client.ocr_pdf
ocr = db.ocr

# allow files of a specific type
ALLOWED_IMAGE_EXTENSIONS = set(['pdf'])

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS

# route and function to handle the home page
@app.route('/')
def home_page():
    select_all = []
    for obj in ocr.find( ):
        select_all.append(obj)

    return render_template('index.html' , select_all=select_all)

# route and function to handle the upload page
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

            # call the OCR function on it
            extracted_text = ocr_core(file)
            extracted_text = extracted_text[0].splitlines()

            for x in range(0 , extracted_text.count("")):
                extracted_text.remove("")

            for x in range(0 , extracted_text.count(" ")):
                extracted_text.remove(" ")

            json = {}
            for str in extracted_text:
                json[f'linha {extracted_text.index(str)+1}'] = str

            ocr.insert_one(json)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Upload concluido com sucesso!',
                                   extracted_text=extracted_text,
                                   img_src=app.config["IMAGE_UPLOADS"] + filename)
    elif request.method == 'GET':
        return render_template('upload.html')

@app.route('/view/<id>', methods=['GET'])
def view(id):
    # pdf = []
    pdf = ocr.find_one( {"_id": ObjectId(id)} )
    return render_template('view.html' , pdf=pdf )

@app.route('/delete/<id>', methods=['GET'])
def delete(id):
    deleted = ocr.find_one_and_delete( {'_id': ObjectId(id)} ) != None
    select_all = []
    for obj in ocr.find( ):
        select_all.append(obj)
    return render_template('index.html' , deleted = deleted , select_all=select_all )

@app.route('/update', methods=["POST"])
def update():
    valor = request.form['valor']
    object_id = request.form['id']
    linha = request.form['linha']
    update = ocr.update_one( {'_id': ObjectId(object_id)} , {"$set": {f"{linha}": f"{valor}"}}) != None
    pdf = ocr.find_one( {"_id": ObjectId(object_id)} )
    return render_template('view.html' , pdf=pdf , update = update )

if __name__ == '__main__':
    app.run(debug=True)