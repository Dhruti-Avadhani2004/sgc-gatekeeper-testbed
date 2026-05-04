import os
import sqlite3
import pickle
import base64
from flask import Flask, request

app = Flask(__name__)

@app.route("/vulnerable-demo")
def index():
    user_id = request.args.get("id")
    file_name = request.args.get("file")

    # 1. SQL Injection (Direct string formatting)
    # Semgrep Rule: python.lang.security.audit.sqli.sqlite-string-format
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = '%s'" % user_id) 

    # 2. Command Injection (Using os.system with user input)
    # Semgrep Rule: python.lang.security.audit.system-command-execution-os-system
    os.system("ls -l " + file_name)

    # 3. Insecure Deserialization (Unpickling user-controlled data)
    # Semgrep Rule: python.lang.security.audit.pickle.insecure-pickle-deserialization
    data = request.args.get("data")
    decoded_data = base64.b64decode(data)
    obj = pickle.loads(decoded_data) 

    # 4. Hardcoded Secret (Generic secret detection)
    # Semgrep Rule: generic.secrets.security.detected-hardcoded-secret
    API_KEY = "1a2b3c4d5e6f7g8h9i0j" 

    return "Processing complete!"

if __name__ == "__main__":
    # 5. Insecure App Configuration (Running with debug=True)
    # Semgrep Rule: python.flask.security.audit.debug-enabled
    app.run(debug=True, port=5000)
