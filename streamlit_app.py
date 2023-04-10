import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

def get_api_key():
    input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-2twmA8tfCb8un4...", key="openai_api_key_input")
    return input_text


openai_api_key = get_api_key()


st.set_page_config(page_title="Analize growth", page_icon=":robot:")
st.header("Analize growth")

st.image(image='data.png', width=500)



 
st.markdown("Analize data for growth (GDP per capita) for countries in the world [LangChain](https://langchain.com/) and [OpenAI](https://openai.com) and made by \
                [@GregKamradt](https://twitter.com/GregKamradt). \n\n View Source Code on [Github](https://github.com/gkamradt/globalize-text-streamlit/blob/main/main.py)")

st.markdown("## Enter Your Question")



def get_text():
    input_text = st.text_area(label="Email Input", label_visibility='collapsed', placeholder="Your Email...", key="email_input")
    return input_text

question = get_text()

if len(question.split(" ")) > 700:
    st.write("Please enter a shorter question. The maximum length is 700 words.")
    st.stop()


def update_text_with_example():
    print ("in updated")
    st.session_state.email_input = "Sally I am starts work at yours monday from dave"

st.markdown("### Your Converted Email:")

if question:
    if not openai_api_key:
        st.warning('Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.stop()

    agent = create_csv_agent(OpenAI(temperature=0, openai_api_key=openai_api_key), 'gdp-per-capita-growth.csv', verbose=True)
    answer = agent.run(question)
    st.write(answer)


