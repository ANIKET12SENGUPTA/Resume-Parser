import streamlit as st
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from extractor import extract_text
from parser import parse_resume

st.title("🎯 Resume Parser")
st.markdown("**Upload resumes → Parse name/email/skills → Match to job using TF-IDF!**")

job_desc = st.text_area(
    "Job Description",
    "Example: Applying for a Machine Learning Engineer with Python, TensorFlow, PyTorch, Git."
)

uploaded_files = st.file_uploader(
    "Upload PDF resumes",
    accept_multiple_files=True,
    type="pdf"
)


if st.button("🚀 PARSE & MATCH") and uploaded_files:
    results = []
    os.makedirs("temp", exist_ok=True)

    resume_texts = []
    filenames = []

    # Save resumes + extract text using extractor.py
    for file in uploaded_files:
        path = f"temp/{file.name}"

        with open(path, "wb") as f:
            f.write(file.getbuffer())

        text = extract_text(path)
        resume_texts.append(text)
        filenames.append(file.name)

    # TF-IDF similarity calculation
    docs = [job_desc] + resume_texts
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(docs)

    job_vec = tfidf[0:1]
    resume_vecs = tfidf[1:]
    sims = cosine_similarity(job_vec, resume_vecs)[0]

    # Parse + score
    for i, text in enumerate(resume_texts):
        data = parse_resume(text)

        raw_sim = sims[i]
        score = min(max(raw_sim * 200, 0), 100)

        data["score"] = round(score, 1)
        data["file"] = filenames[i]

        results.append(data)

    df = pd.DataFrame([
        {
            "File": r["file"],
            "Score": r["score"],
            "Name": r["name"],
            "Skills": ", ".join(r["skills"])
        }
        for r in results
    ])

    st.subheader("📊 Ranking")
    st.dataframe(df.sort_values("Score", ascending=False), use_container_width=True)

    st.subheader("📈 Match Scores")
    st.bar_chart(df.set_index("File")["Score"])

    st.subheader("📄 Parsed Details")
    for r in results:
        with st.expander(f"{r['file']}  —  {r['score']}%"):
            st.json(r)


st.info("CV Tip: MENTION YOUR SKILLS AND ADD YOUR CERTIFICATES")