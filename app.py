from flask import Flask, jsonify, request, send_file
from PIL import Image
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("codeparrot/unixcoder-java-complexity-prediction")
model = AutoModelForSequenceClassification.from_pretrained("codeparrot/unixcoder-java-complexity-prediction")

import smtplib
import imghdr
from email.message import EmailMessage
from pydriller import Repository
import os
import string
import re

def predict_complexity(code):
  inputs = tokenizer(code, return_tensors="pt")

  op = model(**inputs)

  values = []
  names=['constant', 'cubic', 'linear', 'logn', 'nlogn', 'np', 'quadratic']
  for val in op.logits[0]:
    values.append(val.item())

  return names[(values.index(max(values)))]

def get_code_maintainability(filepath):
    def get_maintainability_index(report):
        symbols = set()

        alphanum = (list(string.ascii_lowercase + string.ascii_uppercase + string.digits +  '()+-.─' + '\n' + ' '))

        for i in report:
            if i not in alphanum:
                symbols.add(i)

        for sym in symbols:
            report = report.replace(sym, " ")

        return float(report.split()[19])
    
    filename = filepath.split('/')[-1]
    # folder = '/'.join(filepath.split('/')[:-1]).strip()
    folder = '/'.join(filepath.split('/')[:-1]).strip()
    folder = folder.replace(r"\ ", " ")
    
    os.chdir(folder)
    os.system("ls")
    os.system("wily build")
    os.system("wily report " + filename + " > report.txt")

    f = open("report.txt", "r")
    text = (f.readlines())
    text = ''.join(text) 

    return get_maintainability_index(text)
  
# creating a Flask app
app = Flask(_name_)
  
# From React, send GET request to localhost:5000/some_code
@app.route('/complexity', methods = ['GET','POST'])
def pred():
    input=request.args.get('code')
    output = predict_complexity(input)
    return jsonify({'output': output})
#dont use this
# @app.route('/maintainability', methods = ['POST'])
# def maintain():
#     urlPath = request.args.get('code')
#     output = get_code_maintainability(urlPath)
#     return jsonify({'output': output})

@app.route('/functioncallflowchart', methods = ['POST'])
def flowchart_generator():
    filepath = request.args.get('code')
    # filename = filepath.split('/')[-1]
    # folder = '/'.join(filepath.split('/')[:-1]).strip()
    # folder = folder.replace(r"\ ", " ")
    # os.chdir(folder)
    os.system("code2flow "+filepath)
    file_send="out.png"
    # {'output' :  'linear'}
    #return jsonify({'image': output})
    return send_file(file_send, mimetype='image/gif')

@app.route('/malicious_commit', methods=['GET','POST'])
def check_malicious_commits():
    repo=request.args.get('code')
    for commit in Repository(repo).traverse_commits():
        scary_list=['xml','json']
        if(commit.committer_date.time().hour in [9,10,11,12]):
            mesg=f"Commit at odd time detected at commit with message {commit.msg}"
            return jsonify({'output':mesg})
        if(commit.insertions>100 or commit.deletions>100):
            mesg=f"Many insertions or deletions detected at commit with message {commit.msg}"
            return jsonify({'output':mesg})
        filetypes=set()
        for file in commit.modified_files:
            hehe=file.filename.split(".")
            if(hehe[1] in scary_list):
                return jsonify({'output':"malicious commit possibile due to change in sensitive files"})
    return jsonify({'output':"No malicious commits found!"})

@app.route('/function_call_flowchart',methods=['GET','POST'])
def fn():
    filepath = request.args.get('code')
    os.system("code2flow "+filepath)
   

    Sender_Email = "example@gmail.com"
    #Reciever_Email = "bckoduru@gmail.com"
    Reciever_Email = request.args.get('receiver_mail')
    Password = "lzmpkercxb"

    newMessage = EmailMessage()                         
    newMessage['Subject'] = "View your function call flow chart" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content('Hope this clears any confusion!') 

    with open('out.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
    return jsonify({'message':'mail sent!'})

#use this instead
@app.route('/maintainability',methods=['GET','POST'])
def micalcfunction():
    path=request.args.get('code')
    os.system("radon mi "+ path + " > mi.txt")
    f = open("mi.txt", "r")
    text = (f.readlines())
    text = ''.join(text)
    return jsonify({'output':text[-2]})

if _name_ == '_main_':
    app.run(debug = True)
