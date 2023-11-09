import streamlit as st
from transformers import pipeline, set_seed

# Initialize the model and set a seed for reproducibility if needed
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
set_seed(42)

def generate_health_advice_with_llm(smoking_status, exercise_frequency, alcohol_consumption, dietary_habits, known_conditions, family_history, current_medications, height, weight, age):
    # Construct a prompt from the user's input
    prompt = (
        f"Provide health advice based on the following patient information:\n"
        f"Smoking Status: {smoking_status}\n"
        f"Exercise Frequency: {exercise_frequency}\n"
        f"Alcohol Consumption: {alcohol_consumption}\n"
        f"Dietary Habits: {', '.join(dietary_habits)}\n"
        f"Known Medical Conditions: {known_conditions}\n"
        f"Family Medical History: {family_history}\n"
        f"Current Medications: {current_medications}\n"
        f"Height: {height} cm\n"
        f"Weight: {weight} kg\n"
        f"Age: {age} years\n"
        f"Advice:"
    )
    
    # Generate health advice using the LLM
    generated_responses = generator(prompt, max_length=500, num_return_sequences=1)
    advice = generated_responses[0]['generated_text'].split('Advice:')[1].strip()
    
    return advice

def health_risk_assessment_app():
    st.header('Health Risk Assessment Form')

    with st.form("health_risk_form"):
        st.subheader('Patient Lifestyle Information')
        # Lifestyle-related questions
        smoking_status = st.selectbox('Smoking Status', ['Never', 'Former', 'Current'])
        exercise_frequency = st.selectbox('Exercise Frequency', ['Never', 'Rarely', 'Regularly', 'Daily'])
        alcohol_consumption = st.selectbox('Alcohol Consumption', ['None', 'Moderate', 'Frequent'])
        dietary_habits = st.multiselect('Dietary Habits', ['Balanced', 'High-fat', 'High-sugar', 'Vegetarian', 'Vegan'])

        st.subheader('Medical History')
        # Medical history-related questions
        known_conditions = st.text_input('Known Medical Conditions (comma separated)')
        family_history = st.text_input('Family Medical History (comma separated)')
        current_medications = st.text_input('Current Medications (comma separated)')

        st.subheader('Biometric Information')
        # Biometric information questions
        height = st.number_input('Height (in centimeters)', min_value=100, max_value=250)
        weight = st.number_input('Weight (in kilograms)', min_value=30, max_value=200)
        age = st.number_input('Age', min_value=0, max_value=130)

        # Submit button for the form
        submit_button = st.form_submit_button('Submit')

    if submit_button:
        st.write('Submitted!')
         # Call the health advice generator function
        advice = generate_health_advice_with_llm(
            smoking_status, 
            exercise_frequency, 
            alcohol_consumption, 
            dietary_habits, 
            known_conditions, 
            family_history, 
            current_medications, 
            height, 
            weight, 
            age
        )
        st.subheader('Health Advice')
        st.write(advice)