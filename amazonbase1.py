from flask import Flask, request, jsonify
import subprocess
import sys

app = Flask(__name__)

def check_user_existence(phone_number):
    # Run the Selenium script as a separate process
    result = subprocess.run([sys.executable, "selenium_script.py", phone_number], capture_output=True, text=True)
    return result.stdout.strip() == "True"

@app.route('/check_user', methods=['POST'])
def check_user():
    data = request.json
    phone_number = data.get('phone_number')
    
    if not phone_number:
        return jsonify({"error": "Phone number is required"}), 400
    
    user_exists = check_user_existence(phone_number)
    return jsonify({"user_exists": user_exists})

if __name__ == '__main__':
    app.run(debug=True)
