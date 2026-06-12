# AI Resume Analyzer

A Flask-based web application that analyzes resumes in PDF format, extracts skills, and calculates an ATS (Applicant Tracking System) score.

## Features

- Upload resume in PDF format
- Extract text from resumes using PDF processing
- Detect technical skills from resume content
- Calculate ATS score based on identified skills
- Display extracted resume content
- Simple and user-friendly web interface

## Tech Stack

- Python
- Flask
- HTML
- CSS
- PDFPlumber

## Project Structure

```text
AI_RESUME_ANALYZER/
│
├── app.py
├── ats.py
├── resume_parser.py
├── skill_extractor.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── uploads/
```

## Installation

### Clone the repository

```bash
git clone https://github.com/khyathi15hue/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## How It Works

1. User uploads a PDF resume.
2. The application extracts text from the PDF.
3. Skills are identified from the extracted content.
4. ATS score is calculated.
5. Results are displayed on the analysis page.

## Example Skills Detected

- Python
- Java
- SQL
- Machine Learning
- Flask
- Git
- Data Science
- Pandas
- NumPy
- Scikit-learn

## Future Enhancements

- Job Description Matching
- AI-powered Resume Feedback
- Interview Question Generation
- Resume Improvement Suggestions
- Advanced ATS Scoring

## Author

**Khyathi Sri Dharmavarapu**

- GitHub: https://github.com/khyathi15hue
- LinkedIn: Add your LinkedIn profile link here
