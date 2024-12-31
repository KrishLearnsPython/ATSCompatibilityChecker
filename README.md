# ATSCompatibilityChecker

**Overview**

The ATS Compatibility Checker is a web application built using Streamlit that allows users to upload a PDF resume and evaluate its compatibility with a given job description. The application extracts text from the uploaded PDF and uses a generative AI model to assess the resume against the job description, providing a match percentage, missing keywords, and a profile summary.

**Features**

1) PDF Upload: Users can upload their resumes in PDF format.
2) Text Extraction: The application extracts text from the uploaded PDF for further analysis.
3) ATS Evaluation: Users can input a job description and receive an evaluation of their resume, including:

    a) JD Match Percentage
    b) Missing Keywords
    c) Profile Summary
    d) Recommendation on whether to apply for the job

   
**Requirements**

To run this application, you need the following:

1) Python 3.7 or higher
2) Streamlit
3) PyPDF2
4) Google Generative AI SDK
   
You can install the required packages using pip: pip install streamlit PyPDF2 google-generativeai



**Setup**

1) API Key: Obtain your API key from Google Generative AI and replace "YOUR_API_KEY" in the code with your actual API key. 
(line 6 in code)
link: https://ai.google.dev/gemini-api/docs/api-key

3) Run the Application: Start the Streamlit application by running the following command in your terminal: streamlit run app.py



**Usage**

1) Upload a PDF Resume: Click on the "Upload a PDF file" button to upload your resume.
2) Select an Option: Choose between "Extract Text" to view the extracted text from your resume or "Run ATS" to evaluate your resume against a job description.
3) Extract Text: If you select "Extract Text," the application will display the text extracted from your PDF.
4) Run ATS: If you select "Run ATS," enter the job description in the provided text area and click the "Calculate ATS" button. The application will analyze your resume and provide feedback.
