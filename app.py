import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Heart Disease App",
    page_icon="💖",
    layout="wide"
)

# ==============================
# SIDEBAR WITH LOGO + NAVIGATION
# ==============================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/833/833472.png", width=100)
st.sidebar.title("💖 Green Haven Health AI")

page = st.sidebar.radio(
    "📂 Navigation",
    ["🏠 Home", "📊 Visualization", "💡 About", "🔍 Prediction Result"],
)

# ==============================
# HOME PAGE
# ==============================
if page == "🏠 Home":
    st.title("💖 Heart Disease Prediction App")
    st.write("Predict your heart disease risk using Machine Learning!")

    # Two-column layout for inputs
    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Select Age", 18, 100, 25)
        chol = st.number_input("Enter Cholesterol Level", 100, 400, 200)
        bp = st.number_input("Blood Pressure (mm Hg)", 80, 200, 120)

    with col2:
        sex = st.selectbox("Gender", ["Male", "Female"])
        sugar = st.number_input("Blood Sugar Level (mg/dL)", 50, 300, 120)
        chest_pain = st.selectbox(
            "Chest Pain Type",
            ["Typical", "Atypical", "Non-anginal", "Asymptomatic"]
        )

    # Predict button
    predict_btn = st.button("🔮 Predict Risk")

    if predict_btn:
        # Store user inputs in session state and redirect to results page
        st.session_state["page"] = "🔍 Prediction Result"
        st.session_state["inputs"] = {
            "Age": age,
            "Cholesterol": chol,
            "BP": bp,
            "Gender": sex,
            "Sugar": sugar,
            "Chest Pain": chest_pain
        }
        st.rerun()

# ==============================
# VISUALIZATION PAGE
# ==============================
elif page == "📊 Visualization":
    st.title("📊 Heart Data Visualization Dashboard")

    st.write("Explore sample health data insights below 👇")

    # Generate sample dataset
    df = pd.DataFrame({
        "Age": np.random.randint(25, 70, 50),
        "Cholesterol": np.random.randint(150, 300, 50),
        "BP": np.random.randint(90, 180, 50)
    })

    # Create interactive scatter plot
    fig = px.scatter(
        df,
        x="Age",
        y="Cholesterol",
        size="BP",
        color="BP",
        title="Age vs Cholesterol vs Blood Pressure",
        template="plotly_dark"
    )
    st.plotly_chart(fig, use_container_width=True)

# ==============================
# ABOUT PAGE
# ==============================
elif page == "💡 About":
    st.title("💡 About This Project")
    st.markdown("""
    ### ❤️ Heart Disease Prediction App  
    This AI-powered web app helps users understand their potential **heart disease risk**  
    using basic health indicators like age, blood pressure, and cholesterol.  

    #### 🧠 Built With:
    - 🖥️ **Streamlit** – for the interactive user interface  
    - 📊 **Plotly** – for advanced visualizations  
    - 🤖 **Machine Learning** – for smart risk prediction  

    #### 👩‍⚕️ Mission:
    Empower early detection and promote healthy living through data-driven insights.  
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966482.png", width=150)

# ==============================
# PREDICTION RESULT PAGE
# ==============================
elif page == "🔍 Prediction Result":
    st.title("🔍 Prediction Result")

    if "inputs" in st.session_state:
        inputs = st.session_state["inputs"]

        st.write("### Your Input Data:")
        st.json(inputs)

        # Simple example prediction logic
        if inputs["Cholesterol"] < 200 and inputs["BP"] < 130:
            result = "Low Risk 💚"
        else:
            result = "High Risk 💔"

        st.success(f"**Prediction Result:** {result}")

        # Personalized advice
        st.markdown("### 🩺 Health Tips:")
        if result == "Low Risk 💚":
            st.info("Keep maintaining a healthy lifestyle! 🥗💪")
        else:
            st.warning("Please consult a doctor and maintain a balanced diet & regular exercise.")
    else:
        st.error("⚠️ No prediction data found! Please go back to the Home page.")

# ==============================
# FOOTER
# ==============================
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("© 2025 Green Haven Health AI | Made with ❤️ using Streamlit")
