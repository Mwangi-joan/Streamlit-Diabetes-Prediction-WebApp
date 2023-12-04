import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def main():
    st.title("DiaBeatIt Dashboard")
    st.image('images/diabetes-prevalence.png', use_column_width=True)
    st.image('images/statistics.jpeg', use_column_width=True)
    st.image('images/statistics2.png', use_column_width=True)


if __name__ == "__main__":
    main()
