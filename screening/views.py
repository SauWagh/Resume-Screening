from django.shortcuts import render
import pdfplumber
import docx
import re

SKILLS = [
    "python",
    "django",
    "fastapi",
    "flask",
    "react",
    "javascript",
    "postgresql",
    "mysql",
    "docker",
    "aws",
    "langchain",
    "langgraph",
    "chromadb",
    "faiss",
    "rag",
    "git"
]


def extract_pdf(file):
    text = ""

    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
    except Exception:
        pass

    return text


def extract_docx(file):
    text = ""

    try:
        document = docx.Document(file)

        for para in document.paragraphs:
            text += para.text + " "
    except Exception:
        pass

    return text


def extract_experience(text):
    matches = re.findall(r'(\d+)\+?\s*(?:years|yrs)', text.lower())

    if matches:
        return max([int(x) for x in matches])

    return 0


def home(request):

    results = []

    if request.method == "POST":

        jd = request.POST.get("job_description", "").lower()

        resumes = request.FILES.getlist("resumes")

        jd_skills = []

        for skill in SKILLS:
            if skill in jd:
                jd_skills.append(skill)

        required_exp = extract_experience(jd)

        for resume in resumes:

            resume_text = ""

            if resume.name.lower().endswith(".pdf"):
                resume_text = extract_pdf(resume)

            elif resume.name.lower().endswith((".doc", ".docx")):
                resume_text = extract_docx(resume)

            resume_text = resume_text.lower()

            matched = []
            missing = []

            for skill in jd_skills:

                if skill in resume_text:
                    matched.append(skill)
                else:
                    missing.append(skill)

            skill_score = 0

            if len(jd_skills) > 0:
                skill_score = (
                    len(matched) / len(jd_skills)
                ) * 100

            candidate_exp = extract_experience(
                resume_text
            )

            if required_exp > 0:
                exp_score = min(
                    (candidate_exp / required_exp) * 100,
                    100
                )
            else:
                exp_score = 100

            final_score = round(
                (skill_score * 0.8) +
                (exp_score * 0.2)
            )

            if final_score >= 80:
                recommendation = "Strong Match"
            elif final_score >= 60:
                recommendation = "Consider"
            else:
                recommendation = "Reject"

            results.append({
                "resume": resume.name,
                "score": final_score,
                "experience": candidate_exp,
                "matched": matched,
                "missing": missing,
                "recommendation": recommendation
            })

        results = sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )

    return render(
        request,
        "screening/home.html",
        {"results": results}
    )