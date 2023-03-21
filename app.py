from flask import Flask, jsonify, request, send_file

from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("codeparrot/unixcoder-java-complexity-prediction")
model = AutoModelForSequenceClassification.from_pretrained("codeparrot/unixcoder-java-complexity-prediction")

def predict_complexity(code):
  inputs = tokenizer(code, return_tensors="pt")

  op = model(**inputs)

  values = []
  names=['constant', 'cubic', 'linear', 'logn', 'nlogn', 'np', 'quadratic']
  for val in op.logits[0]:
    values.append(val.item())

  return names[(values.index(max(values)))]

app = Flask(__name__)
  
# From React, send GET request to localhost:5000/some_code
@app.route('/complexity', methods = ['GET','POST'])
def pred():
    #input = code
    input=request.args.get('code')
    output = predict_complexity(input)
    # {'output' :  'linear'}
    return jsonify({'output': output})
  
 __name__ == '__main__':
    app.run(debug = True)
