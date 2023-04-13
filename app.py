from flask import Flask, request, jsonify
import tiktoken

app = Flask(__name__)


@app.post("/tokenizer")
def tokenizer():
    if 'model' not in request.json or 'content' not in request.json:
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

    if not isinstance(request.json['content'], str):
        response = jsonify({
            'message': 'the content must be a string'
        })
        return response

    encoding = tiktoken.encoding_for_model(request.json['model'])
    tokens = encoding.encode(request.json['content'])

    response = jsonify({
        'tokens': tokens
    })

    return response
