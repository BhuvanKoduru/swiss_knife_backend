from flask import Flask, jsonify, request, send_file

from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("codeparrot/unixcoder-java-complexity-prediction")
model = AutoModelForSequenceClassification.from_pretrained("codeparrot/unixcoder-java-complexity-prediction")

import os
import string

def predict_complexity(code):
  inputs = tokenizer(code, return_tensors="pt")

  op = model(**inputs)

  values = []
  names=['constant', 'cubic', 'linear', 'logn', 'nlogn', 'np', 'quadratic']
  for val in op.logits[0]:
    values.append(val.item())

  return names[(values.index(max(values)))]
