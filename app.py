from flask import Flask, request, jsonify
import tiktoken

app = Flask(__name__)


@app.post("/tokenizer")
def tokenizer():
    if not request.json.get('model') or not request.json.get('content'):
        response = jsonify({
            'message': 'both model and content are required'
        })
        response.status_code = 422
        return response

    if request.json['model'] not in ['gpt-4', 'gpt-3.5-turbo']:
        response = jsonify({
            'message': 'the model is not supported'
        })
        return response

    encoding = tiktoken.encoding_for_model(request.json['model'])
    tokens = encoding.encode(request.json['content'])

    response = jsonify({
        'tokens': tokens
    })

    return response
