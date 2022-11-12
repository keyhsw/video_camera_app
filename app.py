import gradio as gr
import cv2

def gray(video):
    vidcap = cv2.VideoCapture(video)
    success, image = vidcap.read()
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale

iface = gr.Interface(
    fn=gray,
    inputs=gr.Video(source="webcam", format="mp4", streaming="True"),
    outputs="image"
)
iface.launch()

