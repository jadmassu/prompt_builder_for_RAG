from flask import Flask,request,jsonify
from controller import controller

app = Flask(__name__)

@app.route("/generatePrompt",methods=[ 'POST',"GET"])
def generate_prompt():
    try:
        if request.method == 'POST':
            prompt = request.get_json()
            if 'question' not in prompt:
                return jsonify({"error": "Question not found in the request."}), 400
            
            # Check if the question is empty
            if not prompt['question']:
                return jsonify({"error": "Question cannot be empty."}), 400

            # Send the non-empty prompt to the controller
            response = controller(prompt['question'])
            
            return jsonify(response), 200
        else:
            return 'Hello, World!'
    except Exception as e:
        return jsonify({"error": str(e)}), 500