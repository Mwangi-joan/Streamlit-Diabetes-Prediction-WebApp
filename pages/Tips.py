import streamlit as st
import pandas as pd
import random
import time

# Dummy data for tips
tips_data = {
    'Tip': [
        "Maintain a healthy weight. Being overweight increases the risk of diabetes.",
        "Regular exercise helps control weight and reduces the risk of diabetes.",
        "Eat a balanced diet with plenty of fruits, vegetables, and whole grains.",
        "Limit sugary and processed foods to prevent blood sugar spikes.",
        "Monitor your blood glucose levels regularly, especially if you have risk factors.",
        "Quit smoking to reduce the risk of diabetes and other health issues.",
        "Manage stress through relaxation techniques like meditation and yoga.",
        "Stay hydrated. Drinking enough water is important for overall health.",
    ],
    'Image': [
        "images/picture4.jpeg",
        "images/picture5.jpeg",
        "images/picture2.jpeg",
        "images/picture3.jpeg",
        "images/picture4.jpeg",
        "images/picture2.jpeg",
        "images/picture3.jpeg",
        "images/picture4.jpeg",
    ]

}

tips_df = pd.DataFrame(tips_data)

def get_random_tip():
    return random.choice(tips_df['Tip'])

def get_random_image():
    return random.choice(tips_df['Image'])

# Streamlit app
def main():
    st.title("Diabetes Prediction Tips")
    st.subheader("Useful tips for diabetes prevention and management")

    # Create a placeholder for tips section
    tips_placeholder = st.empty()

    while True:
        # Get a random tip and image
        random_tip = get_random_tip()
        random_image = get_random_image()

        # Display the image
        st.image(random_image, use_column_width=True)

        # Display the tip
        st.info(f"💡 **Tip:** {random_tip}")

        # Update tips every 10 seconds
        time.sleep(10)

if __name__ == "__main__":
    main()
