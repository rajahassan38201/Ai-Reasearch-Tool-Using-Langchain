from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.7)

st.header('Reasearch Tool Using Langchain')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "GPT-3: Language Models are Few-Shot Learners",
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "Diffusion Models Beat GANs on Image Synthesis",
        "AlexNet: ImageNet Classification with Deep Convolutional Neural Networks",
        "ResNet: Deep Residual Learning for Image Recognition",
        "YOLO: You Only Look Once - Real-Time Object Detection",
        "VGGNet: Very Deep Convolutional Networks for Large-Scale Image Recognition",
        "U-Net: Convolutional Networks for Biomedical Image Segmentation",
        "Swin Transformer: Hierarchical Vision Transformer using Shifted Windows",
        "DALL·E: Creating Images from Text",
        "CLIP: Connecting Text and Images",
        "SAM: Segment Anything Model",
        "ViT: An Image is Worth 16x16 Words"
    ]
)


style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')



if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)