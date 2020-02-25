from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap 
from flask_uploads import UploadSet,configure_uploads,IMAGES,DATA,ALL
from werkzeug import secure_filename
import os 
import datetime
import time 
import pandas as pd 
import numpy as np 



#from flask_uploads import



#from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
Bootstrap(app) 


files = UploadSet('files',ALL)
app.config['UPLOADED_FILES_DEST'] = 'static/uploadsDB'
configure_uploads(app,files) 






@app.route('/')  
def index():
    return render_template('index.html')

@app.route('/datauploads' ,methods =['GET','POST'])  
def datauploads():
  if request.method == 'POST' and 'csv_data' in request.files:
    file = request.files['csv_data']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/uploadstorage' , filename))



    df = pd.read_csv(os.path.join('static/uploadstorage' , filename))
    df_table = df


  return render_template('details.html', filename=filename , df_table=df)




if __name__=="__main__":
    app.run(debug=True)




    #@app.route('/upload', methods=['POST'])
    #def upload():
    #file=request.files['ifile']

    #return file.filename




      #config the db 

#app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///dfiles.db'
#db = SQLAlchemy(app)

#define db columns 


#class FileContent(db.Model):
 #    tweet = db.Column(db.String(200) , primary_key = True)
  #   label = db.Column(db.Integer)


#@app.route('/analyse' , methods=['POST'])  
#def analyse():
    #if request.method=="POST":
     #   rawtext = request.form['rawtext']
        #nlp
      #  blob = TextBlob(rawtext)
       # received_text = blob
   # return render_template('index.html' , received_text = received_text )

        #return render_template('index.html')