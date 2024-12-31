import streamlit as st
import PyPDF2
import google.generativeai as genai


genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

def extract_text(uploaded_file):
    
    pdf_text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    
    for page in pdf_reader.pages:
        pdf_text += page.extract_text() + "\n"  

    
    return pdf_text


st.title("ATS Compatibility Checker")


uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")


if uploaded_file is not None:
    st.success("PDF has been uploaded successfully!")

    
    option = st.selectbox(
        "Select an option:",
        ["Select an option", "Extract Text", "Run ATS"]
    )

    if option == "Extract Text":
        
        extracted_text = extract_text(uploaded_file)

        
        st.write("Extracted Text:")
        st.text_area("PDF Text", extracted_text, height=500)

    elif option == "Run ATS":
        jdesc = st.text_area("Enter Job Description:", height=150)
        if st.button("Calculate ATS"):
            
            extracted_text = extract_text(uploaded_file)

            
            input_prompt = f"""
            Act as a highly skilled and experienced Application Tracking System (ATS). Your role is to evaluate resumes based on the provided job description (JD). Keep in mind that the job market is highly competitive, and your goal is to offer the best possible assistance for improving resumes. Accurately assign a percentage match to the JD and identify missing keywords with precision.
            resume: {extracted_text}
            description: {jdesc}
            I want the response in a proper manner: JD Match %, Missing Keywords, and Profile Summary. Also provide if the user should apply for the job. 
            """

            
            ats_response = model.generate_content(input_prompt)
            st.write(f"ATS Score: {ats_response.text}")
