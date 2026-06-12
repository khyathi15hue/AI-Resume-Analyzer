skills_db = [

    "Python",
    "Java",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Machine Learning",
    "Deep Learning",
    "Flask",
    "Git",
    "Data Science"

]

def extract_skills(text):

    found_skills = []

    for skill in skills_db:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return found_skills