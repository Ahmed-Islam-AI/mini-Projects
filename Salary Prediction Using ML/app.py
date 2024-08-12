import streamlit as st
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
from plotly import graph_objs as go

# Load the data
data = pd.read_csv('Data/Salary_Data.csv')
x = np.array(data['YearsExperience']).reshape(-1, 1)
model = LinearRegression()
model.fit(x, np.array(data['Salary']))

# Streamlit app title
st.title('Salary Prediction App')

# Sidebar navigation
nav = st.sidebar.radio('Navigation', ['Home', 'Prediction', 'Contribute'])

# Home page
if nav == 'Home':
    st.image('Data/dataset-card.jpg', width=400)

# Show CSV file data
if st.checkbox('Show CSV File Data'):
    st.table(data)

# Filter the data based on years of experience
val = st.slider("Filter data using years of Experience", 0, 20)
filtered_data = data[data['YearsExperience'] <= val]

# Choose the type of graph
graph = st.selectbox('What kind of graph?', ['Non-Interactive', 'Interactive'])

# Plot the graph
if graph == 'Non-Interactive':
    # Use a new figure object for thread safety and to avoid the warning
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(filtered_data['YearsExperience'], filtered_data["Salary"])
    ax.set_ylim(0)
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Salary")
    plt.tight_layout()
    st.pyplot(fig)

if graph == 'Interactive':
    layout = go.Layout(
        xaxis=dict(range=[0, 15]),
        yaxis=dict(range=[0, 2300000])
    )
    
    fig = go.Figure(data=go.Scatter(x=filtered_data["YearsExperience"], y=filtered_data['Salary'], mode='markers'), layout=layout)
    st.plotly_chart(fig)

# Salary prediction page
if nav == 'Prediction':
    st.header('Predict Salary by Using Machine Learning')
    val = st.number_input('Enter Your Experience', 0.00, 20.00, step=0.25)
    val = np.array(val).reshape(-1, 1)
    pred = model.predict(val)[0]
    
    if st.button('Predict'):
        st.success(f"Your Predicted Salary is {round(pred)}")

# Data contribution page
if nav == 'Contribute':
    st.header("Contribute Your Data")
    ex = st.number_input("Enter Your Years of Experience", 0.00, 20.00)
    sal = st.number_input("Enter Your Salary", 0.00, 800000.00, step=1000.00)
    
    if st.button("Submit Data"):
        # Append the new data to the CSV
        to_add = pd.DataFrame({'YearsExperience': [ex], 'Salary': [sal]})
        to_add.to_csv('Data/Salary_Data.csv', mode='a', header=False, index=False)
        st.success("Data Added Successfully!")
