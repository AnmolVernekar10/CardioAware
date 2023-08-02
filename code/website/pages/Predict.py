import streamlit as st
import pandas as pd
import requests
import pickle
from streamlit_lottie import st_lottie
import base64
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components


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
# This code is used for the styling of the header statement
def header(url):
    st.markdown(f'<p style="background-color:transparent;color:white;font-size:32px;font-weight:bolder;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

header("Predict your Heart Health!!")
# ********************************************************************************





# ********************************************************************************
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)
# ********************************************************************************

# This code is used for the removal of the Header of the streamlit page
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header{visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ********************************************************************************
#                                Background Image code

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
set_background('code/website/heart illustration.jpg')

# ********************************************************************************
                            # Styled Text
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    color: white;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)
# ********************************************************************************
# This code is for the Predict button styling

st.markdown("""
    <style>
    .stButton button {
        background-color:white;
        color: black;
        border: 2px solid black; /* Deep Pink color */
        border-radius: 10px;
        padding: 10px 20px;
        width: 30%;
        height:30%;
    }
    .stButton button:hover {
        background-color:rgb(100, 242, 90);
        color: black;
        border: 2px solid black; /* Deep Pink color */
        border-radius: 10px;
        padding: 10px 20px;
        width: 30%;
        height:30%;
    }
    </style>
""", unsafe_allow_html=True)

# ********************************************************************************


# ********************************************************************************
# This code is for the styling of the sidebar

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color:transparent;
        font-size:18px;
        color:white;
    }
</style>
""", unsafe_allow_html=True)
# ********************************************************************************


def main():
    col1,col2,col3,col4,col5=st.columns([0.7,1,1,1,1.1])
    with col1:
        st.markdown('<p class="big-font">Age </p>', unsafe_allow_html=True)
        age=st.number_input("", 0,100)
        st.markdown('<p class="big-font">Thalassemia</p>', unsafe_allow_html=True)
        thal=st.selectbox("", [0,1,2,3])

    with col2:
        st.markdown('<p class="big-font">Gender </p>', unsafe_allow_html=True)
        gender=st.selectbox("empty",['Male','Female'],label_visibility="hidden")
        if gender=='Male':
            sex=0
        else:
            sex=1
        st.markdown('<p class="big-font">Resting BP mm/Hg</p>', unsafe_allow_html=True)
        trestbps=st.number_input("",90,200)

    with col3:
        st.markdown('<p class="big-font">Chestpain </p>', unsafe_allow_html=True)
        val=st.selectbox("",['None','Mild','Moderate','Severe'],label_visibility="hidden")
        if val=='None':
            cp=0
        elif val=='Mild':
            cp=1
        if val=='Moderate':
            cp=2
        if val=='Severe':
            cp=3

        st.markdown('<p class="big-font">Fasting BloodSugar</p>', unsafe_allow_html=True)
        ans=st.number_input("",0,200)
        if ans>120:
            fbs=1
        else:
            fbs=0

    with col4:
        st.markdown('<p class="big-font">Cholesterol </p>', unsafe_allow_html=True)
        chol=st.number_input("",100,600,label_visibility='hidden')

        st.markdown('<p class="big-font">Resting ECG Result</p>', unsafe_allow_html=True)
        restecg=st.selectbox("",[0,1,2],label_visibility="hidden")

    with col5:
        st.markdown('<p class="big-font">Max Heart Rate</p>', unsafe_allow_html=True)
        thalach=st.number_input("", 70, 220)

        st.markdown('<p class="big-font">Chestpain on excercise</p>', unsafe_allow_html=True)
        vale =st.selectbox("",['Yes','No'])
        if vale=='Yes':
            exang=1
        elif vale=='No':
            exang=0


    
    # oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.2, 1.0)
    # slope = st.slider('Slope of the Peak Exercise ST Segment', 0, 2, 1)
    # ca = st.slider('Number of Major Vessels Colored by Fluoroscopy', 0, 4, 1)
    # thal = st.slider('Thalassemia', 0, 3, 1)
    st.write("##")

    if st.button('Predict'):
        user_input = pd.DataFrame(data={
            'age': [age],
            'sex': [sex],
            'cp': [cp],
            'trestbps': [trestbps],
            'chol': [chol],
            'fbs': [fbs],
            'restecg': [restecg],
            'thalach': [thalach],
            'exang': [exang],
            'thal': [thal]
            # 'oldpeak': [oldpeak],
            # 'slope': [slope],
            # 'ca': [ca],
        })
        prediction = model.predict(user_input)
        if prediction[0]==1:
             st.markdown('<p class="big-font">Heart Disease Prediction: Positive</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="big-font">Heart Disease Prediction: Positive</p>', unsafe_allow_html=True)
        # st.write(f"Heart Disease Prediction: {'Positive' if prediction[0] == 1 else 'Negative'}")

if __name__ == '__main__':
    main()

