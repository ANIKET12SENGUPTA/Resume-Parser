# 🎯 Resume Parser

A smart Resume Parser and Job Matching web app built with **Python**, **Streamlit**, **PyMuPDF**, and **scikit-learn**.  
This project allows users to upload PDF resumes, extract important candidate details, and rank resumes against a job description using TF-IDF similarity scoring.

## 📌 Overview

Recruiters and hiring teams often receive many resumes for a single role. Manually screening them takes time and effort. This project helps automate the early screening process by:

- Extracting text from uploaded PDF resumes
- Parsing basic candidate details like name, email, phone number, and skills
- Comparing resumes with a job description
- Ranking resumes based on similarity score
- Displaying parsed data in an interactive web interface

This project is beginner-friendly and also useful as a portfolio project for students and aspiring machine learning engineers.

---

## 🚀 Features

- Upload multiple PDF resumes
- Extract resume text from PDF files
- Parse:
  - Candidate name
  - Email address
  - Phone number
  - Skills
- Match resumes with a given job description
- Generate a similarity score using TF-IDF + cosine similarity
- Rank candidates based on job relevance
- View parsed details in an easy-to-use Streamlit interface
- Display score visualization with charts

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – for the web interface
- **PyMuPDF** – for PDF text extraction
- **pandas** – for tabular result display
- **scikit-learn** – for TF-IDF vectorization and cosine similarity

---

## 📂 Project Structure

```bash
Resume-Parser/
│── app.py
│── parser.py
│── extractor.py
│── requirements.txt

⚙️ How It Works
1. Resume Upload
Users upload one or more PDF resumes through the Streamlit interface.

2. Text Extraction
Each uploaded resume is processed using PyMuPDF to extract text content.

3. Resume Parsing
The extracted text is analyzed to identify:
> Name
> Email
> Phone number
> Skills

4. Job Description Matching
The entered job description and each resume are converted into TF-IDF vectors.

5. Similarity Scoring
Cosine similarity is used to measure how closely each resume matches the job description.

6. Ranking and Display
The application ranks resumes by score and displays:
> A results table
> Match score bar chart
> Parsed resume details

📥 Installation
1. Clone the repository
> git clone https://github.com/ANIKET12SENGUPTA/Resume-Parser.git
> cd Resume-Parser

2. Install dependencies
> pip install -r requirements.txt

▶️ Run the Application
> streamlit run app.py

📝 Example Usage
1. Open the app
2. Enter a job description, for example:
  > Looking for a Machine Learning Engineer with Python, TensorFlow, PyTorch, Git, NLP, and data analysis skills.
    Upload one or more PDF resumes
4. Click PARSE & MATCH
5. View:
    > Resume ranking table
    > Match score chart
    > Parsed candidate information

📊 Sample Output
The app generates:
  > A ranked table of resumes with:
      > File name
      > Match score
      > Candidate name
      > Skills
  > A bar chart showing resume scores
  > Expandable parsed details for each uploaded resume

🙌 Acknowledgment
This project was built as a practical machine learning and NLP-based application to learn resume parsing, document processing, and job-resume matching.
