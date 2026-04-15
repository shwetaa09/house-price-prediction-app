import streamlit as st
import pickle
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>

.stApp {
background: linear-gradient(to right,#eef2f3,#8e9eab);
}

h1 {
text-align:center;
color:#0a2540;
font-size:45px;
}

.stButton>button {
background-color:#2563eb;
color:white;
border-radius:10px;
height:3em;
width:200px;
font-size:18px;
}

.stButton>button:hover {
background-color:#1d4ed8;
}

.result-box{
background:white;
padding:25px;
border-radius:10px;
text-align:center;
box-shadow:0px 4px 10px rgba(0,0,0,0.2);
margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# Load trained model
model = pickle.load(open("model.pkl","rb"))

# Title
st.markdown("<h1>🏠 House Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("### Predict the estimated house price using Machine Learning")

st.write("Enter house details below 👇")

# Input layout
col1,col2,col3 = st.columns(3)

with col1:
    area = st.number_input("Area (sq ft)",500,5000,step=100)

with col2:
    bedrooms = st.number_input("Bedrooms",1,10)

with col3:
    age = st.number_input("Age of House",0,50)

# Predict button
predict = st.button("🔍 Predict Price")

# Prediction
if predict:
    features = np.array([[area,bedrooms,age]])
    price = model.predict(features)

    st.markdown(f"""
    <div class="result-box">
    <h2>💰 Estimated House Price</h2>
    <h1 style="color:#2563eb;">₹ {int(price[0]):,}</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("Made with ❤️ by **Shweta Chaubey**")