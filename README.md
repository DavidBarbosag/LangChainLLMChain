# LangChain LLM Chain Tutorial

Este proyecto implementa un ejemplo básico del uso de **LangChain** con **OpenAI**, mostrando cómo crear una **cadena simple de prompts (LLM Chain)** para generar texto de manera estructurada.

---

## Objetivo del Proyecto

El propósito de este ejercicio es familiarizarse con los conceptos fundamentales de **LangChain**, comprendiendo cómo:
- Conectar un **modelo de lenguaje (LLM)** de OpenAI.
- Crear **prompts dinámicos** con variables.
- Encadenar pasos de procesamiento usando la **LangChain Expression Language (LCEL)**.
- Ejecutar consultas básicas para generar texto.

---

## Estructura del Proyecto

langchain-llm-chain/

├── main.py # Script principal

├── .env # Archivo con la clave de API de OpenAI

├── requirements.txt # Dependencias del entorno

└── README.md # Documentación del proyecto

---

## Descripción del Script (`main.py`)

El archivo `main.py` contiene todos los pasos necesarios para construir y ejecutar una cadena simple en LangChain:

### 1. **Importación y configuración**
```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
```

* Se importan las clases necesarias para:

  * Cargar variables de entorno (load_dotenv).

  * Inicializar el modelo de lenguaje de OpenAI (ChatOpenAI).

  * Crear plantillas de prompts (ChatPromptTemplate).

  * Procesar y formatear la salida (StrOutputParser).

### 2. **Inicialización del modelo**

   ```
   llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
   ```


### 3. **Creación del prompt dinámico**

   ```
   prompt = ChatPromptTemplate.from_template("Explica en dos frases el concepto de {tema}.")
   ```
### 4. **Construcción de la cadena**

   ```
   chain = prompt | llm | StrOutputParser()
   ```
### 5. **Ejecución de la cadena**

   ```
   resultado = chain.invoke({"tema": "aprendizaje automático"})
   print(resultado)
   ```

## Instalación y Ejecución

1. Clona este repositorio:

    ```
    git clone https://github.com/tu_usuario/langchain-llm-chain.git
    cd langchain-llm-chain
    ```
   
2. Instala las dependencias:

    ```
    pip install -r requirements.txt
    ```

3. Crea el archivo .env con tu clave de OpenAI

4. Ejecuta el script:

    ```
    python main.py
    ```
