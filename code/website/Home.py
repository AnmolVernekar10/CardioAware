import streamlit as st
import pandas as pd
import requests
import pickle
import base64
from streamlit_lottie import st_lottie
import streamlit as st
from PIL import Image

# ************************************************ Pickling of Model ************************************************
# In Pickling of Model : rb--> Load the model from pickle
#                        lb--> Saving the model with pickle

model_name='model/Model.pkl'
with open(model_name,'rb') as file:
    model=pickle.load(file)

# *******************************************************************************************************************



# Here we are setting the page configuration: page icon, page title, layout type
st.set_page_config(page_title="CardioAware", page_icon="🫀" , layout="wide")



# *******************************************************************************************************************
# Here we are Styling the sidebar of the website
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background:transparent;
        font-size:18px;
        color:white;
    }
</style>
""", unsafe_allow_html=True)

# *******************************************************************************************************************



# *******************************************************************************************************************

# We are using this section, to add background-image to the website
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# set_background('E:/Heart_Disease_Project/Code/Website/2923472.webp')
set_background('code/website/heart illustration.jpg')
# *******************************************************************************************************************





# *******************************************************************************************************************
# This code can be used for a Lottie animation
# lottie = """
# <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
# <lottie-player src="https://lottie.host/0ec1f945-d5c7-4242-acb8-aed934124f09/yoeQjUP5a8.json"  background="transparent"  speed="0"  style="width: 500px; height: 500px;"  loop  autoplay></lottie-player>
# """s

            # right: 60px;

# st.components.v1.html(lottie, width=300, height=300)
# *******************************************************************************************************************



# *******************************************************************************************************************
# Used for importing the Css file ( style.css)
def local_css():
    with open("code/website/style/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# *******************************************************************************************************************




def webcode():    
    local_css()
    with st.container():
        original_title = '<p style="position:relative;top:-120px;color:White;font-weight:500; font-size: 32px;"><b><u>Heart Disease Prediction</u></b></p>'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style=" position:relative;color:white;font-weight:bold; font-size: 20px;top:-130px;padding-left:50px;padding-right:50px;">At CardioAware, we are dedicated to promoting heart health and helping individuals assess their risk of heart-disease accurately and conveniently. Our state-of-the-art platform employs artificial intelligence and machine learning algorithms to provide you with personalized and reliable predictions.</p>'
        st.markdown(original_title, unsafe_allow_html=True)

    with st.container():
        original_title = '<p style=" position:relative;top:-140px;color:White; font-size: 32px;"><b><u>Key Features: </u></b></p>'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style=" position:relative;color:white;font-weight:bold; font-size: 20px;top:-133px;padding-left:50px;padding-right:50px;">Comprehensive Risk Assessment, User-Friendly Interface<br> ,Instant Results, Educational Resources..</p>'
        st.markdown(original_title, unsafe_allow_html=True)

    with st.container():
        original_title = '<p style=" position:relative;top:-140px;color:White; font-size: 32px;"><b><u>Contact Us: </u></b></p>'
        st.markdown(original_title, unsafe_allow_html=True)

        contact_form="""
        <form action="https://formsubmit.co/comderboi@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required><input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Query" required></textarea>
        <button type="submit">Send</button></form>"""

        left_column ,right_column =st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()


       
        
# *******************************************************************************************************************
# Model copy
# def main():
#     age=st.slider("Age: ", 18, 100, 50)
#     sex=st.selectbox("Sex-> (Male :- 0), (Female :- 1): ", [0,1])
#     cp=st.slider("Chestpain: ",0,3,1)
#     trestbps=st.slider("Resting Blood pressure: ",90,200,120)
#     chol=st.slider("Cholesterol: ",100,600,250)
#     fbs=st.selectbox("Fasting Blood Sugar > 120mg/dl ", [0,1])
#     restecg=st.selectbox("Resting Electrocardiographic Results ",[0,1,2])
#     thalach = st.slider('Maximum Heart Rate Achieved', 70, 220, 150)
#     exang = st.selectbox('Exercise Induced Angina', [0, 1])
#     # oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.2, 1.0)
#     # slope = st.slider('Slope of the Peak Exercise ST Segment', 0, 2, 1)
#     # ca = st.slider('Number of Major Vessels Colored by Fluoroscopy', 0, 4, 1)
#     # thal = st.slider('Thalassemia', 0, 3, 1)

#     if st.button('Predict'):
#         user_input = pd.DataFrame(data={
#             'age': [age],
#             'sex': [sex],
#             'cp': [cp],
#             'trestbps': [trestbps],
#             'chol': [chol],
#             'fbs': [fbs],
#             'restecg': [restecg],
#             'thalach': [thalach],
#             'exang': [exang],
#             # 'oldpeak': [oldpeak],
#             # 'slope': [slope],
#             # 'ca': [ca],
#             # 'thal': [thal]
#         })
#         prediction = model.predict(user_input)
#         st.write(f"Prediction: {'Positive' if prediction[0] == 1 else 'Negative'}")
# *******************************************************************************************************************


if __name__ == '__main__':
    webcode()

