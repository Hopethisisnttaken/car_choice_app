import pandas as pd
import streamlit as st
import plotly.express as px

# I used the fixed csv here. the one that doesn't have null values.
data_s = pd.read_csv('data_s.csv')

st.header('Welcome to CRAPP')
st.header('The app to help you find a car within you price range based on model and condition')

price_range = st.slider('What is your price range?', value = (0,380000))
actual_range=list(range(price_range[0],price_range[1]+1))
filtered_data=data_s[data_s.price.isin(actual_range)]

st.write('This histogram gives a general look at the number of options available within your pricerange,'
         ' colored by condition')
fig = px.histogram(filtered_data, x = "price", color = "condition")
st.plotly_chart(fig)

car_cond = st.radio('What car condition are you interested in?',
         ['new','like new','excellent','good','fair','salvage'])

if car_cond is 'new':
    filtered_data = data_s[data_s.price.isin(actual_range)]
    filtered_data = filtered_data[data_s['condition']=='new']
elif car_cond is 'like_new':
    filtered_data = data_s[data_s.price.isin(actual_range)]
    filtered_data = filtered_data[data_s['condition'] == 'like new']
elif car_cond is 'excellent':
    filtered_data = data_s[data_s.price.isin(actual_range)]
    filtered_data = filtered_data[data_s['condition'] == 'excellent']
elif car_cond is 'good':
    filtered_data = data_s[data_s.price.isin(actual_range)]
    filtered_data = filtered_data[data_s['condition'] == 'good']
elif car_cond is 'fair':
    filtered_data = data_s[data_s.price.isin(actual_range)]
    filtered_data = filtered_data[data_s['condition'] == 'fair']
elif car_cond is 'salvage':
    filtered_data = data_s[data_s.price.isin(actual_range)]
    filtered_data = filtered_data[data_s['condition'] == 'salvage']
else:
    filtered_data = data_s[data_s.price.isin(actual_range)]

st.write('This is the price range of each vehicle type in your condition and price range')
type_vs_price = px.scatter(filtered_data,y='price',x='type')
st.plotly_chart(type_vs_price)

posted = st.checkbox('Show me only 4wd cars')

if posted:
    filtered_data = filtered_data[filtered_data['is_4wd']==1]

st.write("Here's the list of cars recommended for you: ")
st.dataframe(filtered_data)
