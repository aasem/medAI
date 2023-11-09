import streamlit as st
from scenarios import scenarios
from health_risk_assessment import health_risk_assessment_app

# Place the scenario details in the sidebar
def display_scenario_info(selected_scenario):
    st.sidebar.markdown(f"**Use Case**: {scenarios[selected_scenario]['Use Case']}")
    st.sidebar.markdown(f"**Input**: {scenarios[selected_scenario]['Input']}")
    st.sidebar.markdown(f"**Output**: {scenarios[selected_scenario]['Output']}")
    st.sidebar.markdown(f"**Design**: {scenarios[selected_scenario]['Design']}")
    st.sidebar.markdown(f"**Complexity**: {scenarios[selected_scenario]['Complexity']}")

# Function for the Health Risk Assessment demo
def health_risk_assessment_demo():{}
    # ... (Insert the health_risk_assessment_form function code here)


def main():
    st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
    st.sidebar.title("Use Cases")
    selected_scenario = st.sidebar.selectbox("Choose a scenario", list(scenarios.keys()))

    # Display the selected scenario information in the sidebar
    if selected_scenario:
        display_scenario_info(selected_scenario)
        
        # Depending on the scenario, display the corresponding demo in the main frame
        if selected_scenario == "Health Risk Assessment":
            health_risk_assessment_app()

if __name__ == "__main__":
    main()