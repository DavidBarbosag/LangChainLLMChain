import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

prompt = ChatPromptTemplate.from_template("Explica en dos frases el concepto de {tema}.")
chain = prompt | llm | StrOutputParser()

resultado = chain.invoke({"tema": "aprendizaje automático"})
print("Resultado:")
print(resultado)
