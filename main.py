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


if place:
    filtered_content = get_data(place, days)

    if option == 'Temperature':
        temperature = [dict['main']['temp'] for dict in filtered_content]
        dates = [dict['dt_txt'] for dict in filtered_content]
        figure = px.line(x=dates, y=temperature, labels={'x': 'Date', 'y': 'Temperature (C)'})
        st.plotly_chart(figure)
    if option == 'Sky':
        filtered_content = [dict['weather'][0]['main'] for dict in filtered_content]
        images = {'Clear': 'images/clear.png',
                       'Clouds': 'images/cloud.png',
                       'Rain': 'images/rain.png',
                       'Snow': 'images/snow.png'
                       }
        image_path = [images[x] for x in filtered_content]
        st.image(image_path, width=115)
