import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


# Set up pages name
st.sidebar.title("Sidebar")
st.sidebar.markdown('---')
st.sidebar.page_link(page="app.py", label="Home", icon="🏠")
st.sidebar.page_link(page="pages/predict.py", label="Oracle", icon="🔮")
# st.sidebar.markdown("---")

# Set the title
st.title("Funfact about penguins🐧")

# Add an image and description
st.image('penguins.png')
st.markdown("This is the [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/) dataset that describes measurements on penguins")
st.markdown("---")

# Load the penguins dataset
df = pd.read_csv("./data/penguins_pimped.csv")

# Display a sample of 5 random observations in the dataset
df_sample = df.sample(n=5)
st.header("Penguins 🐧 data")
st.dataframe(df_sample)
st.markdown("**-->Here you can describe your data<--**")

st.subheader("Let's play with the data")

# Create a dropdown menu for selecting an island
island = df['island'].unique()
user_island = st.selectbox(label="Select an Island", options=island)

# Add a checkbox to filter data based on the selected island
if st.checkbox("Do you really want to see the filtered data according to your island?"):
    st.dataframe(df[df['island'] == user_island])
st.markdown("---")

st.header("Showing 🐧 cases with Matplotlib, Seaborn, and Plotly")
st.subheader("🐧 Matplotlib + Seaborn")
fig, ax = plt.subplots()
ax = sns.scatterplot(
    data=df,
    x='bill_length_mm',
    y='bill_depth_mm',
    hue='species'
)
st.pyplot(fig)

st.subheader("🐧 Plotly")
plotly_fig = px.scatter(
    data_frame=df,
    x='bill_length_mm',
    y='bill_depth_mm',
    color='species',
    animation_frame='sex',
)
st.plotly_chart(plotly_fig)

st.subheader("🐧 Bar Chart")
bill_length_mean = df.groupby(by='species')['bill_length_mm'].mean()
st.bar_chart(bill_length_mean)

st.subheader("🐧 Maps 🗺️📍")
st.map(df)