import boto3
import ai_calls
import streamlit as st



bedrock_runtime =  boto3.client(
                                service_name = 'bedrock-runtime',
                                region_name='us-east-1',
                            )   

st.title("SGD - Buscador de documentos")
st.write("Este es un buscador de documentos que utiliza inteligencia artificial para responder preguntas")


user = st.text_area("Chat")
ai_calls.claude_call(bedrock_runtime, user, user, model=1, max_tokens=4000, images=None)



