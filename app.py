import streamlit as st
import numpy as np
import joblib

model = joblib.load(r"C:\Users\bindu\OneDrive\Desktop\Fitness-Lifestyle-Prediction-20250224T053449Z-001\Fitness-Lifestyle-Prediction\data\exercise_dataset.csv")

st.title("Fitness Level Predictor")

st.header("Enter Your Details:")

calories_burn = st.number_input("Calories Burned", min_value=0.0, step=0.1)
dream_weight = st.number_input("Dream Weight (kg)", min_value=0.0, step=0.1)
actual_weight = st.number_input("Actual Weight (kg)", min_value=0.0, step=0.1)
age = st.number_input("Age (years)", min_value=1, step=1)
gender = st.selectbox("Gender", options=["Male", "Female"], index=0)
duration = st.number_input("Duration (minutes)", min_value=1, step=1)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, step=1)
bmi = st.number_input("BMI", min_value=0.0, step=0.1)
weather_conditions = st.selectbox("Weather Conditions", options=["Rainy", "Cloudy", "Sunny"], index=0)

gender_map = {"Male": 1, "Female": 0}
weather_map = {"Rainy": 0, "Cloudy": 1, "Sunny": 2}

mapped_gender = gender_map[gender]
mapped_weather = weather_map[weather_conditions]

test_data = np.array([calories_burn, dream_weight, actual_weight, age, mapped_gender, duration, heart_rate, bmi, mapped_weather]).reshape(1, -1)

levels = ["Average", "Bad", "Good"]
if st.button("Check Fitness"):
    prediction = model.predict(test_data)

    if prediction[0] == 0:  
        st.info(f"Based on your input, your fitness level is **Average**.")
        st.subheader("Suggestions to Improve Your Fitness Level:")
        st.write("- **Increase Exercise Duration**: Aim for at least 45 minutes per session to transition to a 'Good' fitness level.")
        st.write("- **Focus on Moderate-Intensity Workouts**: Engage in activities like brisk walking, cycling, or light jogging.")
        st.write("- **Monitor Your Diet**: Ensure you have a balanced diet with proteins, carbs, and healthy fats.")
        st.write("- **Stay Consistent**: Commit to regular physical activities 4-5 times per week.")

    elif prediction[0] == 1:
        st.error(f"Based on your input, your fitness level is **Bad**.")
        st.subheader("General Suggestions to Achieve Better Fitness:")
        st.write("- **Increase Exercise Duration**: Aim for at least 30-60 minutes per session.")
        st.write("- **Improve Exercise Intensity**: Include jogging, cycling, or interval training to increase heart rate.")
        st.write("- **Track Calories Burned**: Choose exercises like running or aerobics to burn more calories.")
        st.write("- **Maintain a Healthy BMI**: Combine a balanced diet with exercise to improve BMI.")
        st.write("- **Gradual Progress**: Start with small steps to build stamina and fitness over time.")

    elif prediction[0] == 2:
        st.success(f"Based on your input, your fitness level is **Good**.")
        st.subheader("Keep Up the Great Work!")
        st.write("- Continue with your current routine and maintain consistency.")
        st.write("- Set new goals to further enhance your fitness (e.g., improved strength, endurance).")
        st.write("- Focus on a balanced lifestyle, including proper hydration and rest.")

        