import time
import streamlit as st

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="📑",
)

st.title("DocumentGPT")

def send_message(message, role):
    with st.chat_message(role):
        st.write(message)

message = st.chat_input("send a message to the ai")

if message:
    send_message(message, "human")
    time.sleep(2)
    send_message(f"You said: {message}", "ai")



# with st.chat_message("human"):
#     st.write("Helloo")

# with st.chat_message("ai"):
#     st.write("how are you")

# with st.status("Embedding file...", expanded=True) as status:
#     time.sleep(2)
#     st.write("Getting the file")
#     time.sleep(2)
#     st.write("Embedding the file")
#     time.sleep(2)
#     st.write("Caching the file")
#     status.update(label="Error", state="error")

