import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Example data
data = np.random.randn(100)

def plot_with_matplotlib():
    plt.figure(figsize=(10, 4))
    plt.hist(data, bins=20, alpha=0.5, label='Data')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.legend()
    return plt

# Plotting with Matplotlib
st.write("### Plotting with Matplotlib")
fig = plot_with_matplotlib()
st.pyplot(fig)