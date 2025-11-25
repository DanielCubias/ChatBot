import os
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7, api_key=os.getenv("GOOGLE_API_KEY"))
pregunta = input("Haga su pregunta para gemini: ")

while pregunta != "salir":
    respuesta = llm.invoke(pregunta)
    print(respuesta.content)
    pregunta = input("Haga su pregunta para gemini: ")