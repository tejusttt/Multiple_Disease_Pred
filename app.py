import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu
from sklearn.exceptions import NotFittedError
import time
import warnings

warnings.filterwarnings("ignore", category=UserWarning, message="X does not have valid feature names")

# Set page configuration
st.set_page_config(page_title="Multiple Disease Prediction", layout="centered", page_icon="💉")

# Define paths and load models
working_dir = os.path.dirname(os.path.abspath(__file__))

try:
    diabetes_model = pickle.load(open(r'e:\New folder\Multiple_Disease_Prediction-main\diabetes.pkl', 'rb'))
    heart_disease_model = pickle.load(open(r'e:\New folder\Multiple_Disease_Prediction-main\heart.pkl', 'rb'))
    kidney_disease_model = pickle.load(open(r'e:\New folder\Multiple_Disease_Prediction-main\kidney.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"Model file not found: {e}")
except Exception as e:
    st.error(f"Error loading models: {e}")

# Enhanced CSS for sidebar and animations
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
            color: #333;
        }
        .nav-link-selected, .nav-link:hover {
            color: #1f77b4 !important;
            transition: color 0.5s ease;
        }
        .stButton>button {
            color: white;
            background: linear-gradient(135deg, #11998e, #38ef7d);
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            transition: all 0.4s ease;
            font-size: 16px;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #11998e, #11998e);
            transform: translateY(-5px);
        }
        .title {
            color: #007acc;
            font-weight: bold;
            text-align: center;
            font-size: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation with icons
with st.sidebar:
    selected = option_menu(
        "🔍 Disease Prediction Menu",
        ['🏥 Diabetes Prediction', '❤️ Heart Disease Prediction', '🩺 Kidney Disease Prediction'],
        icons=['droplet', 'heart', 'stethoscope'],
        menu_icon="capsule",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#1a0e0e", "border-radius": "10px"},
            "icon": {"color": "#f39c12", "font-size": "30px"},
            "nav-link": {"font-size": "20px", "margin": "10px 0", "padding": "10px 15px", "border-radius": "8px"},
            "nav-link-selected": {"background-color": "#16a085", "color": "white", "border-radius": "10px", "font-weight": "bold"},
        }
    )

# Helper function for validated input
def get_float_input(prompt, min_value=None, max_value=None):
    step = 1 if isinstance(min_value, int) else 1.0
    value = st.number_input(f"{prompt}:", min_value=min_value, max_value=max_value, step=step, key=prompt)
    return value

# Dynamic header
st.markdown(f"<h1 class='title'>👨‍⚕️ Welcome to Multiple Disease Prediction System</h1>", unsafe_allow_html=True)

# Function to simulate progress and prediction tasks
def simulate_progress(task_name, total_steps=100):
    progress_bar = st.progress(0)
    for i in range(total_steps):
        time.sleep(0.03)
        progress_bar.progress(i + 1)
    st.success(f"{task_name} Completed!")

# Diabetes Prediction Page
if selected == '🏥 Diabetes Prediction':
    st.subheader("Diabetes Prediction")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = get_float_input("Number of Pregnancies", min_value=0)
    with col2:
        Glucose = get_float_input("Glucose Level", min_value=0)
    with col3:
        BloodPressure = get_float_input("Blood Pressure Level", min_value=0)
    with col1:
        SkinThickness = get_float_input("Skin Thickness", min_value=0)
    with col2:
        Insulin = get_float_input("Insulin Level", min_value=0)
    with col3:
        BMI = get_float_input("BMI", min_value=0.0)
    with col1:
        DiabetesPedigreeFunction = get_float_input("Diabetes Pedigree Function", min_value=0.0)
    with col2:
        Age = get_float_input("Age", min_value=0)

    if st.button("Predict Diabetes"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        try:
            simulate_progress("Diabetes Prediction")
            prediction = diabetes_model.predict([user_input])
            result = "The person has diabetes" if prediction[0] == 1 else "The person does not have diabetes"
            st.success(result)
        except NotFittedError:
            st.error("Model is not fitted yet. Please check the model file.")

# Heart Disease Prediction Page
elif selected == '❤️ Heart Disease Prediction':
    st.subheader("Heart Disease Prediction")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = get_float_input("Age", min_value=0)
    with col2:
        sex = get_float_input("Sex (1=Male, 0=Female)")
    with col3:
        cp = get_float_input("Chest Pain Type (0-3)")
    with col1:
        trestbps = get_float_input("Resting Blood Pressure", min_value=0)
    with col2:
        chol = get_float_input("Serum Cholesterol in mg/dl", min_value=0)
    with col3:
        fbs = get_float_input("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)")
    with col1:
        restecg = get_float_input("Resting ECG (0-2)")
    with col2:
        thalach = get_float_input("Max Heart Rate Achieved", min_value=0)
    with col3:
        exang = get_float_input("Exercise Induced Angina (1=Yes, 0=No)")
    with col1:
        oldpeak = get_float_input("ST Depression Induced by Exercise", min_value=0.0)
    with col2:
        slope = get_float_input("Slope of the Peak Exercise ST Segment (0-2)")
    with col3:
        ca = get_float_input("Number of Major Vessels Colored by Fluoroscopy (0-3)")
    with col1:
        thal = get_float_input("Thal (3=Normal, 6=Fixed Defect, 7=Reversible Defect)")

    if st.button("Predict Heart Disease"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        try:
            simulate_progress("Heart Disease Prediction")
            prediction = heart_disease_model.predict([user_input])
            result = "The person has heart disease" if prediction[0] == 1 else "The person does not have heart disease"
            st.success(result)
        except NotFittedError:
            st.error("Model is not fitted yet. Please check the model file.")
            
# Kidney Disease Prediction Page
# Kidney Disease Prediction Page
elif selected == '🩺 Kidney Disease Prediction':
    st.subheader("Kidney Disease Prediction")
    
    # Collecting user inputs for kidney disease prediction
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        age = get_float_input("Age", min_value=0)
    with col2:
        bp = get_float_input("Blood Pressure", min_value=0)
    with col3:
        sg = get_float_input("Specific Gravity", min_value=1.0, max_value=1.025)
    with col4:
        al = get_float_input("Albumin", min_value=0)
    with col5:
        su = get_float_input("Sugar", min_value=0)

    # Collecting additional inputs
    with col1:
        rbc = get_float_input("Red Blood Cells (0=Normal, 1=Abnormal)", min_value=0, max_value=1)
    with col2:
        pc = get_float_input("Pus Cells (0=Normal, 1=Abnormal)", min_value=0, max_value=1)
    with col3:
        pcc = get_float_input("Pus Cell Clumps (0=No, 1=Yes)", min_value=0, max_value=1)
    with col4:
        ba = get_float_input("Bacteria (0=No, 1=Yes)", min_value=0, max_value=1)
    with col5:
        bgr = get_float_input("Blood Glucose Random", min_value=0)

    with col1:
        bu = get_float_input("Blood Urea", min_value=0)
    with col2:
        sc = get_float_input("Serum Creatinine", min_value=0)
    with col3:
        sod = get_float_input("Sodium", min_value=0)
    with col4:
        pot = get_float_input("Potassium", min_value=0)
    with col5:
        hemo = get_float_input("Hemoglobin", min_value=0)

    with col1:
        pcv = get_float_input("Packed Cell Volume", min_value=0)
    with col2:
        wc = get_float_input("White Blood Cell Count", min_value=0)
    with col3:
        rc = get_float_input("Red Blood Cell Count", min_value=0)
    with col4:
        htn = get_float_input("Hypertension (1=Yes, 0=No)", min_value=0, max_value=1)
    with col5:
        dm = get_float_input("Diabetes Mellitus (1=Yes, 0=No)", min_value=0, max_value=1)

    # Adding the missing features
    with col1:
        cad = get_float_input("Coronary Artery Disease (1=Yes, 0=No)", min_value=0, max_value=1)
    with col2:
        appet = get_float_input("Appetite (0=Poor, 1=Good)", min_value=0, max_value=1)
    with col3:
        pe = get_float_input("Pedal Edema (1=Yes, 0=No)", min_value=0, max_value=1)
    with col4:
        ane = get_float_input("Anemia (1=Yes, 0=No)", min_value=0, max_value=1)

    # Ensure 25 features are included in user_input
    if st.button("Predict Kidney Disease"):
        user_input = [
            age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo,
            pcv, wc, rc, htn, dm, cad, appet, pe, ane
        ]
        
        try:
            simulate_progress("Kidney Disease Prediction")
            prediction = kidney_disease_model.predict([user_input])
            result = "The person has kidney disease" if prediction[0] == 1 else "The person does not have kidney disease"
            st.success(result)
        except NotFittedError:
            st.error("Model is not fitted yet. Please check the model file.")
