from flask import Flask,request,jsonify
import os, sys
rpath = os.path.abspath('/home/user/Documents/10/w7/PromptBuilder for RAG')
from controller import controller
from werkzeug.exceptions import InternalServerError
app = Flask(__name__)

@app.route("/generatePrompt",methods=[ 'POST',"GET"])
def generate_prompt():
    try:
        if request.method == 'POST':
            prompt = request.get_json()
            if 'question' not in prompt:
                return jsonify({"error": "Question not found in the request."}), 400
            question = prompt['question']
            # Check if the question is empty
            if not question:
                return jsonify({"error": "Question cannot be empty."}), 400
            
            # Send the non-empty prompt to the controller
            response = controller.controller(question)
            return jsonify({"data": response}), 200
        else:
            return 'Hello, World!'
    except Exception as e:
         print(f"An error: {e}")
         raise InternalServerError(description="An internal server error occurred")