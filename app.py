import gradio as gr
import cv2

def gray(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale
    
iface = gr.Interface(fn=gray, inputs="image", outputs="image")
iface.launch()

