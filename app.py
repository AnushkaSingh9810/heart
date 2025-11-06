import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Heart Disease App", page_icon="💖", layout="wide")

# Sidebar with logo
st.sidebar.image("logo.png", use_column_width=True)
st.sidebar.header("🔍 User Input")

# Main title with emoji
st.title("💖 Heart Disease Prediction App")
st.write("Predict your heart disease risk using Machine Learning!")

# Example UI
age = st.slider("Age", 18, 100, 25)
chol = st.number_input("Cholesterol Level", 100, 400, 200)

if st.button("Predict ❤️"):
    st.success("Prediction: Low Risk 💚")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("© 2025 Green Haven Health AI | Made with ❤️ in Streamlit")
