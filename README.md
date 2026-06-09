# AI-Powered Resume Screening & Candidate Ranking System (RAG-Based)
  * This project follows a Retrieval-Augmented Generation architecture.
<hr>

AI Resume Screening System using RAG
Hosted on Render<br>
Live Demo :-  https://resume-screening-21fd.onrender.com

## Overview<br>
AI Resume Screening System is a Retrieval-Augmented Generation (RAG) based recruitment platform designed to automate the candidate screening process.
The system allows recruiters to upload multiple resumes, provide a job description, and automatically rank candidates based on their relevance to the job requirements.
Instead of manually reviewing hundreds of resumes, recruiters receive a sorted list of candidates with match scores, skill gap analysis, and hiring recommendations.

<hr>

## Problem Statement
Recruiters often spend significant time reviewing large volumes of resumes.

### Challenges include:<br>
Manual resume screening is time-consuming<br>
Important candidates may be overlooked<br>
Human bias can affect selection<br>
Skill matching is inconsistent<br>
Large applicant pools are difficult to managenr<br>
<hr>

#### This project addresses these challenges by leveraging Artificial Intelligence and RAG architecture to automate resume evaluation.
<hr>

## Solution
<br>

###  The system performs the following operations:
  1. Upload multiple resumes<br>
  2. Extract text from PDF and DOCX files<br>
  3. Process the job description<br>
  4. Extract skills and experience information<br>
  5. Generate embeddings<br>
  6. Compare resumes against job requirements<br>
  7. Calculate candidate match scores<br>
  8. Rank candidates automatically<br>
  8. Display matched and missing skills<br>
  9. Generate hiring recommendations

<hr> 

### Key Features
  1. Resume Upload
       * Upload multiple resumes simultaneously
       * Supports PDF files
       * Supports DOCX files
       * Bulk candidate processing
  2. Intelligent Resume Parsing
       * Extracts resume content automatically
       * Identifies technical skills
       * Identifies work experience
       * Processes education details
  3. Job Description Analysis
       * Accepts custom job descriptions
       * Extracts required skills
       * Detects experience requirements
       * Creates job requirement profiles
  4. AI Candidate Matching
       * Semantic similarity matching
       * Skill gap analysis
       * Experience comparison
       * Candidate ranking
  5. Candidate Ranking Dashboard
       * Match percentage
       * Skill match visualization
       * Missing skills identification
       * Hiring recommendations
       * Export Results
  6. CSV export
       * Recruiter-friendly reporting
       * RAG Architecture
    
<hr>

## RAG Architecture

```text
Job Description
        │
        ▼
Skill Extraction
        │
        ▼
Embedding Generation
        │
        ▼
Vector Search
        │
        ▼
Resume Retrieval
        │
        ▼
Similarity Matching
        │
        ▼
Candidate Ranking
        │
        ▼
Recruiter Dashboard
```

---

## System Workflow

```text
Recruiter
      │
      ▼
Upload Resumes
      │
      ▼
Paste Job Description
      │
      ▼
Resume Parsing
      │
      ▼
Embedding Generation
      │
      ▼
Vector Database Search
      │
      ▼
Similarity Scoring
      │
      ▼
Candidate Ranking
      │
      ▼
Results Dashboard
```


##  Technologies Used

### Frontend
The user interface is built using modern web technologies to provide an intuitive and responsive experience for recruiters.

- HTML5
- CSS3
- JavaScript

---

### Backend
The backend handles resume processing, candidate scoring, business logic, and application workflows.

- Python
- Django

---

### Artificial Intelligence & NLP
AI-powered techniques are used to analyze resumes and match candidates against job requirements.

- Retrieval-Augmented Generation (RAG)
- Embedding-Based Retrieval
- Semantic Similarity Search
- Intelligent Candidate Ranking
- Resume-to-Job Description Matching

---

### Resume Processing
The system extracts and processes content from uploaded resumes for analysis.

- pdfplumber (PDF text extraction)
- python-docx (DOCX text extraction)

---

### Database
Used for storing application data, candidate information, and screening results.

#### Development
- SQLite

#### Production Ready
- PostgreSQL

---

### Deployment & Hosting
The application is deployed and hosted on a cloud platform for public accessibility.

- Render
- Gunicorn
- WhiteNoise

---

### 🔧 Development Tools
Additional tools used during development and deployment.

- Git
- GitHub
- Virtual Environment (venv)
- VS Code

---

## Technical Highlights

- Multi-Resume Upload Support
- Automated Candidate Ranking
- AI-Powered Resume Screening
- Job Description Analysis
- Skill Gap Detection
- Recruiter-Friendly Dashboard
- CSV Export Functionality
- Scalable RAG-Based Architecture
- Cloud Deployment on Render

<br>
<hr>

## Project Structure


## How Match Score Is Calculated

The system evaluates each candidate using multiple scoring factors to determine how closely the resume aligns with the job requirements.

### Skill Matching

The system extracts required skills from the Job Description and compares them against the skills found in the candidate's resume.

```text
Required Skills
        VS
Resume Skills
```

Examples:

- Python
- Django
- FastAPI
- React
- PostgreSQL
- Docker

A higher percentage of matched skills results in a higher score.

---

### Experience Matching

The system compares the experience required in the Job Description with the candidate's experience extracted from the resume.

```text
Required Experience
        VS
Candidate Experience
```

Examples:

```text
Job Requirement: 3+ Years

Candidate A: 5 Years   ✓
Candidate B: 3 Years   ✓
Candidate C: 1 Year    ✗
```

Candidates closer to or exceeding the required experience receive higher scores.

---

### Semantic Similarity

The system uses AI-powered semantic matching to compare the overall meaning and context of the Job Description against the Resume content.

```text
Job Description
        VS
Resume Content
```

This helps identify relevant candidates even when different wording is used.

Example:

```text
Job Description:
"Experience with Retrieval-Augmented Generation"

Resume:
"Built AI applications using LangChain and vector databases"
```

Even though the exact phrase is different, the semantic similarity score will be high.

---

###  Final Score Formula

The final candidate score is calculated using a weighted combination of multiple factors.

```text
Final Score

=
(Skill Match × Weight)

+

(Experience Match × Weight)

+

(Semantic Similarity × Weight)
```

Example:

```text
Skill Match          = 90%
Experience Match     = 80%
Semantic Similarity  = 85%

Final Score = 86%
```

---

##  Example Candidate Ranking Output

```text
Rank    Candidate            Score
---------------------------------------
1       John Smith           94%
2       Priya Sharma         89%
3       Saurabh Waghmare     85%
4       Rahul Kumar          72%
5       Candidate X          51%
```

---

##  Recommendation Categories

```text
90% - 100%    Exceptional Match
80% - 89%     Strong Match
70% - 79%     Good Match
60% - 69%     Consider
Below 60%     Low Match
```

---

##  Benefits

<br>
✔ Faster resume screening
<br>
✔ Automated candidate ranking
<br>
✔ Reduced recruiter workload
<br>
✔ Consistent evaluation process
<br>
✔ Better hiring decisions
<br>
✔ Scalable for large applicant pools
<br>
✔ AI-powered semantic understanding
<br>
✔ Improved candidate shortlisting accuracy

<hr> 

##  Future Enhancements
###  Planned improvements:

1.   ChromaDB integration
2.   FAISS vector search
3.   LangChain pipelines
4.   LangGraph workflows
5.   OpenAI embeddings
6.   Gemini integration
7.   PostgreSQL support
8.   Resume summarization
9.   AI-generated interview questions
10.  Candidate recommendation engine
11.  HR analytics dashboard
12.  Email notifications

<br>
<hr>

###  Deployment
####  The application is deployed on Render.
###  Production Environment
* Hosting Platform: Render
* Backend: Django
* WSGI Server: Gunicorn
* Static Files: WhiteNoise
<hr>

<img width="1920" height="952" alt="Image" src="https://github.com/user-attachments/assets/c58d2d64-36fd-467d-9e06-b0286d3d08f5" />
