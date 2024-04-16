import streamlit as st
from openai import OpenAI

# Update the API key
OPENAI_API_KEY = "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"

client = OpenAI(api_key=OPENAI_API_KEY)

# Set colored page title
st.markdown("<h1 style='color:purple;'>GenAI App - AI Code Reviewer</h1>", unsafe_allow_html=True)

# User input section
st.markdown("<h2 style='color:purple;'>Enter Your Python Code</h2>", unsafe_allow_html=True)
prompt = st.text_area("Enter your Python code here:", height=200)

# Button to trigger code review
if st.button("Review the Code"):
    st.markdown("<h2 style='color:green;'>Review Result</h2>", unsafe_allow_html=True)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "user", "content": "Please review the given Python code. Identify any mistakes and provide corrections."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    # Display the generated text
    generated_text = response.choices[0].message.content
    
    # Check if the generated text indicates the code is fine
    if "fine" in generated_text or "perfect" in generated_text or "alright" in generated_text:
        st.write("The code seems fine.")
    else:
        # If the code needs correction, provide the corrected code
        st.write("Review Result:")
        st.write(generated_text)
