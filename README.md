# RAG
## Explanation:
This is just a simple projext to learn how RAG works. I am building the simplest verison so that it runs.

---

## Prerequisites
- **Python** 3.10+  
- **Git**
- **Ollama** running locally (default URL `http://127.0.0.1:11434`)  
    - Pull the model used in the code (default): `ollama pull deepseek-r1:1.5b`
    - you can switch this if you want to just install the ollama you wannt and change it in the code

---

## Guide for windows
1. run the requirements
   `pip install -r requirements.txt`
2. add any context you want as txt files in data folder
3. make sure its running the ollama you want, if not change it in the code and install the correctone 
4. run:
   `python rag_ejercicio.py`
