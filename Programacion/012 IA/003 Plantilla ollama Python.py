import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b-instruct"   #Nombre exacto del modelo instalado

prompt = "Explica qué es PHP."  #Prompt a enviar al modelo

data = {
    "model": MODEL,
    "prompt": prompt,
    "stream": False     #False para respuesta completa, True para respuesta en stream
}

req = urllib.request.Request(
    OLLAMA_URL,
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read().decode("utf-8"))
    print(result["response"])
