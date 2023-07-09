import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forcast for the next day')

place = st.text_input('Place: ')

days = st.slider('Forcast days ', min_value=1,
                 max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select what to view', ('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {place}")


d, t = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)
