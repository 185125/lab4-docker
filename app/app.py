from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def index():
    sid = os.environ.get("STUDENT_ID", "Brak")
    db = os.environ.get("DATABASE_URL", "Brak")
    return f"Student: {sid} | DB: {db.split('@')[-1]}\n"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
