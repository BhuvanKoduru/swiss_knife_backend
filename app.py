# Flask API dummy code

# Run python app.py
# Server in localhost:5000

# Using flask to make an api
# import necessary libraries and functions

from flask import Flask, jsonify, request, send_file

from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("codeparrot/unixcoder-java-complexity-prediction")
model = AutoModelForSequenceClassification.from_pretrained("codeparrot/unixcoder-java-complexity-prediction")


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
    
    #filename = filepath.split('/')[-1]
    filename = filepath.split('\')[-1]
    # folder = '/'.join(filepath.split('/')[:-1]).strip()
    folder = '\'.join(filepath.split('\')[:-1]).strip()
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
app = Flask(__name__)
  
# From React, send GET request to localhost:5000/some_code
@app.route('/complexity', methods = ['GET','POST'])
def pred():
    input=request.args.get('code')
    output = predict_complexity(input)
    return jsonify({'output': output})

@app.route('/maintainability', methods = ['POST'])
def maintain():
    urlPath = request.args.get('path')
    output = get_code_maintainability(urlPath)
    return jsonify({'output': output})

@app.route('/functioncallflowchart', methods = ['POST'])
def flowchart_generator():
    filepath = request.args.get('path')
    # filename = filepath.split('/')[-1]
    # folder = '/'.join(filepath.split('/')[:-1]).strip()
    # folder = folder.replace(r"\ ", " ")
    # os.chdir(folder)
    os.system("code2flow "+filepath)
    file_send="out.png"
    # {'output' :  'linear'}
    #return jsonify({'image': output})
    return send_file(file_send, mimetype='image/gif')


# driver function
if __name__ == '__main__':
    app.run(debug = True)
