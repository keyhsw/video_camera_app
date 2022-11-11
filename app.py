import gradio as gr
import numpy as np

def greet(name):
    array = np.array([1, 2, 3])
    return "Hello " + name + str(array) +  "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()

