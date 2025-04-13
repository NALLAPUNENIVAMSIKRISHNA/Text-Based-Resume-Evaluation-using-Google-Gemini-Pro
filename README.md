# Text-Based Resume Evaluation using Google Gemini Pro

This project is a Streamlit-based application that evaluates a candidate's resume by comparing its text content to a job description using Google’s Gemini Pro. Unlike image-based models, this app directly reads and analyzes the plain text extracted from the uploaded PDF file for fast and accurate results.

---

##  Features

- Paste a **Job Description**.
- Upload your **Resume (PDF format)**.
- Choose one of the following:
  -  Get a resume review.
  -  Suggestions to improve your skills.
  -  Get a match percentage.
- Uses **Gemini Pro** to analyze the text.
- Direct **text-based evaluation** — faster and more efficient.

---

## 🧰 Technologies Used

- **Python**
- **Streamlit** – web app framework
- **Google Generative AI SDK** – for interacting with Gemini Pro
- **PyPDF2 ** – for extracting text from PDF
- **python-dotenv** – for securely managing API keys

---

##  Project Structure

```
 text_resume_evaluator/
├── app.py                # Streamlit app logic
├── .env                   # Contains Gemini API key
├── requirements.txt       # Python dependencies
```

---

##  Setup Instructions

### 1. Clone the Repository

### 2. Install Dependencies

Ensure you have Python 3.8 or above.

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add the Gemini API key:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4. (Optional) Add `.env` to `.gitignore`

To avoid leaking secrets, ensure `.env` is not tracked by Git.

---

##  How to Run the Application

```bash
streamlit run main.py
```

The application will open in your default web browser.

---

##  How It Works

1. **User Inputs**:
   - Paste a **Job Description** in the input area.
   - Upload a **PDF resume**.

2. **Text Extraction**:
   - The PDF file is read using `PyMuPDF`.
   - Full text content is extracted from the resume.

3. **Prompt Generation**:
   - Based on user selection, a specific prompt is generated for Gemini Pro:
     - Resume review
     - Skill gap analysis
     - Match percentage

4. **Gemini Pro Analysis**:
   - Gemini Pro receives the text-based resume and job description.
   - The model returns detailed, natural language feedback.

5. **Output**:
   - The AI's response is displayed clearly in the app window.

---

##  Sample Prompt Templates Used

- “Act like an ATS and evaluate this resume text based on the job description...”
- “What skills are missing in this resume when compared to the job description?”
- “Provide a percentage match based on the resume and the job requirements.”

---

##  Limitations

- Only supports **PDF resumes**.
- Assumes resumes are **text-based PDFs** (scanned image-based resumes will not work).
- Gemini Pro's API usage limits apply.

---

##  Requirements File (`requirements.txt`)

```
streamlit
python-dotenv
google-generativeai
PyPDF2
```

##  Future Improvements

- Add support for `.docx` and `.txt` resume formats.
- Include keyword highlighting from job description in the resume.
- Save results in a downloadable format (PDF or DOC).
- Add user authentication and resume storage history.
