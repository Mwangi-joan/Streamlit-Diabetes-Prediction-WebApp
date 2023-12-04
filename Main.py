import streamlit as st
from streamlit.logger import get_logger
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler


LOGGER = get_logger(__name__)

def main():
        st.set_page_config(page_title="DiaBeatIt", page_icon="👋")
        st.subheader("Welcome to the Diabetes Prediction App!")
        st.image('logo.png', use_column_width=True)

        # Introduction Message
        st.markdown(
                """
                # Welcome to DiaBeatIt Predict!

                🌟 Predict the likelihood of diabetes with DiaBeatIt Predict, your trusted companion for health insights. 🌟

                Are you curious about your risk of developing diabetes? This user-friendly web app provides a quick and easy way to assess your likelihood based on key health factors. Simply navigate to the prediction page, enter your details, and get instant results.

                ✨ Stay proactive about your health. Explore DiaBeatIt Predict today! ✨
                """
        )

        st.sidebar.success("Select a page above")



if __name__ == "__main__":
        main()