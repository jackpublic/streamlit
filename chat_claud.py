import streamlit as st
import anthropic

with st.sidebar:
    anthropic_api_key = st.text_input("Anthropic API Key", key="file_qa_api_key", type="password")


question = st.text_input(
    "Ask something",
    placeholder="Can you tell me joke?",
)

if not anthropic_api_key:
    st.info("Please add your Anthropic API key to continue.")

if question and anthropic_api_key:
    prompt = f"""{anthropic.HUMAN_PROMPT} {question}{anthropic.AI_PROMPT}"""

    client = anthropic.Anthropic(api_key=anthropic_api_key)
    #response = client.completions.create(
    #    prompt=prompt,
    #    stop_sequences=[anthropic.HUMAN_PROMPT],
    #    model="claude-3-opus-20240229", 
    #    max_tokens_to_sample=1000,
    #)
    #st.write("### Answer")
    #st.write(response.completion)
    message = client.messages.create(
      model="claude-3-opus-20240229",
      max_tokens=1000,
      system="chat bot",
      messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "how to use claude in .net environment\n"
                }
            ]
        }
    )
    st.write(message.content)
    
    
