from flask import Flask, render_template, request
import os

from resume_parser import extract_text
from skill_extractor import extract_skills
from ats import calculate_ats

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=["POST"])
def upload():

    file = request.files["resume"]

    path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(path)

    # This line is here
    text = extract_text(path)

    skills = extract_skills(text)
    ats_score = calculate_ats(skills)
    return render_template(
        "result.html",
        text=text,
        skills=skills,
        ats_score=ats_score
    )

if __name__ == "__main__":
    app.run(debug=True)