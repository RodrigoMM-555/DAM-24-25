sudo apt install ollama

ollama pull [modelo]

ollama list
josevicente@josevicenteportatil:~$ ollama list
NAME                   ID              SIZE      MODIFIED     
phi3:mini              4f2222927938    2.2 GB    2 weeks ago     
gemma:2b               b50d6c999e59    1.7 GB    2 weeks ago     
qwen2.5-coder:7b       dae161e27b0e    4.7 GB    2 weeks ago     
qwen2.5:3b-instruct    357c53fb659c    1.9 GB    2 months ago    


ollama run [modelo] "[pregunta]"