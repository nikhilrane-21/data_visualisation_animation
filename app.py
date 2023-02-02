import streamlit as st              # `pip install streamlit`
import pandas as pd                 # `pip install pandas`
import plotly.express as px         # `pip install plotly`

st.set_page_config(
    page_title='DataVisualisation',
    page_icon=':robot:',
)

hide_st_style = """
                <style>
                    header {visibility: hidden;}
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Visualizing Data with Animated Insights: Enhancing Understanding through Dynamic Visualizations.")
st.header("Project 1: Life expectancy vs GDP data visualisation")
df = px.data.gapminder()
st.subheader("Dataframe used:")
st.write(df)

fig = px.scatter(df, x='gdpPercap', y='lifeExp',
            size="pop", color='continent', hover_name='country',
            log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90],
            animation_frame='year', animation_group='country')

fig.update_xaxes(gridcolor='#333333')
fig.update_yaxes(gridcolor='#333333')

fig.update_layout(width=800)
st.subheader("Life expectancy vs GDP Scatter Plot:")
st.write(fig)
st.write("Press ▶️   from above  👆 to visualise data change by year.")


st.header("Project 2: Covid Confirmed Cases across countries Data Visualisation")
covid = pd.read_csv('https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
covid.columns = ['Country', 'Country_code', 'Date', 'Confirmed', 'Days_since_confirmed']


covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')
country_options = covid['Country'].unique().tolist()
st.subheader("Dataframe used:")
st.write(covid)

date_options = covid['Date'].unique().tolist()

country = st.multiselect('Which country would you like to see?', country_options, ['India', 'United States', 'Brazil', 'United Kingdom', 'Russia'])

covid = covid[covid['Country'].isin(country)]
covid = covid[covid['Date']>='2020-03-01']


fig2 = px.bar(covid, x='Country', y='Confirmed', color='Country', range_y=[0,35000],
            animation_frame="Date", animation_group='Country')
fig2.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 30
fig2.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5


fig2.update_layout(width=800)
st.subheader("Covid Cases Bar Plot:")
st.write(fig2)
st.write("Press ▶️   from above  👆 to visualise data change by year.")


