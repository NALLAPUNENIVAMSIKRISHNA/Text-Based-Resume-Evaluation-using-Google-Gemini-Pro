# ATS Resume Evaluation Tool
# pdf to image to get bytes we used pdf2image dependencies are poppler then info going to api then response
# pdf with pypdf2 -> text with text -> api -> response

import google.generativeai as genai
import PyPDF2 as pdf
import os
import streamlit as st
import json
import re
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract response from Gemini
def gemini_pro_response(prompt):
    model = genai.GenerativeModel("gemini-2.0-pro-exp")
    response = model.generate_content(prompt)
    return response.text

# Function to extract text from PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey act like a skilled or very experienced ATS (Application Tracking System) with a deep understanding of tech field, software engineering,
data analyst, big data, and generative AI engineering. Your task is to evaluate the resume based on the given job description. 
You must consider the job market is very competitive and you should provide the best assistance for improving the resume.
Assign the percentage matching based on the JD and the missing keywords with high accuracy.

resume : {text}
description : {jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

# ------------------- Streamlit UI -------------------

st.set_page_config(page_title="ATS Resume Checker", layout="centered")

st.title("🤖 ATS Resume Evaluation Tool")
st.markdown("""
📄 Upload your Resume & 📋 Paste the Job Description below  
🚀 Get instant insights on how your resume matches the job description!

### ℹ️ Instructions
1. Upload your **PDF Resume**  
2. Paste the **Job Description**  
3. Click **Submit** to get:
   - ✅ JD Match Percentage  
   - 🔍 Missing Keywords  
   - 🧠 AI-generated Profile Summary
""")

# Inputs
jd = st.text_area("📝 Paste the Job Description here:")
uploaded_file = st.file_uploader("📎 Upload your Resume (PDF only)", type=["pdf"])
submit = st.button("🚀 Submit")

# Handle Submit
if submit:
    if uploaded_file is not None and jd.strip() != "":
        with st.spinner("🔍 Analyzing your resume..."):
            extracted_text = input_pdf_text(uploaded_file)
            final_prompt = input_prompt.format(text=extracted_text, jd=jd)
            raw_response = gemini_pro_response(final_prompt)

            try:
                # Extract JSON string from the response
                json_match = re.search(r"\{.*\}", raw_response, re.DOTALL)
                if json_match:
                    response_dict = json.loads(json_match.group())

                    # Display results
                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric("📊 JD Match", response_dict["JD Match"])

                    with col2:
                        st.markdown("🧩 **Missing Keywords**")
                        st.write(", ".join(response_dict["MissingKeywords"]))

                    st.markdown("### 📌 Profile Summary")
                    st.info(response_dict["Profile Summary"])
                else:
                    st.error("❌ Couldn't find a valid JSON structure in the response.")
                    st.code(raw_response)
            except Exception as e:
                st.error("❌ Error parsing response. Please try again or check formatting.")
                st.code(raw_response)
    else:
        st.warning("⚠️ Please upload a resume and paste the job description before submitting.")
