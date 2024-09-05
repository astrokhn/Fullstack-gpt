import streamlit as st
from datetime import datetime
# from langchain.prompts import PromptTemplate

today = datetime.today().strftime("%H:%M:%S")
st.title(today)

model = st.selectbox("Choose your model",("GPT-3", "GPT-4"))
st.write(model)

if model == "GPT-3":
    st.write("cheap")
else:
    st.write("not cheap")
    
    name = st.text_input("What is your name?")
    st.write(name)

    value = st.slider("temperature", min_value=0.1, max_value=1.0,)
    st.write(value)

# st.write("hello")
# st.write([1,2,3,4])
# st.write({"x": 1})
# st.write(PromptTemplate)
# st.title("hello world!")
# st.subheader("welcome to streamlit")
# st.markdown("""
#     #### i love it!
# """)
# p = PromptTemplate.from_template("xxxx")
# st.write(p)

# a = [1,2,3,4]
# d = {"x": 1}

# a
# d
# p
# PromptTemplate
