import gradio as gr
import sambanova_gradio

gr.load(
    name='Meta-Llama-3.1-405B-Instruct',
    src=sambanova_gradio.registry,
).launch()