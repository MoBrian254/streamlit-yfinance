import pandas as pd
import streamlit as st
import plotly.express as px
from numerize.numerize import numerize

st.set_page_config(page_title='MoBrian254 Global Emmission Data Visualization',
                    layout='wide',
                    initial_sidebar_state='expanded')


@st.cache_data
def get_data():
    df = pd.read_csv('data/emmisondata.csv')
    return df


df = get_data()

header_mid, header_right = st.columns([3, 1], gap='large')

with header_mid:
    st.title('Emmission Visualization Dashboard')

with st.sidebar:
    st.sidebar.header("MoBrian254 Demo")
    st.sidebar.header('Dashboard')

    Country_filter = st.multiselect(label='Select Country', options=df['Country'].unique(), default=df['Country'].unique())

    Year_filter = st.multiselect(label='Select Year', options=df['Year'].unique(), default=df['Year'].unique())

    git = 'https://github.com/MoBrian254'
    linkdin = 'https://www.linkedin.com/in/brian-owana-web-developer/'
    portfolio = 'https://mobrian-portfolio-01.vercel.app/'
    st.markdown(
        f"<span>Follow me: <a href={git} target='_blank'>@Github</a> | <a href='{linkdin}' target='_blank'>@LinkedIn</a> | <a href='{portfolio}' target='_blank'>@Portfolio</a></span>",
        unsafe_allow_html=True)

df1 = df.query('Country == @Country_filter & Year == @Year_filter')

totals = float(df1['Total'].sum())
total_coal = float(df1['Coal'].sum())
total_oil = float(df1['Oil'].sum())
total_gas = float(df1['Gas'].sum())
total_cement = float(df1['Cement'].sum())
total_flaring = float(df1['Flaring'].sum())
total_other = float(df1['Other'].sum())

# Row A Metrics
st.markdown('### Metrics')
t1, t2, t3, t4, t5, t6, t7 = st.columns(7, gap='large')

with t1:
    st.image('images/totals.png', use_column_width='Auto')
    st.metric(label='Totals', value=numerize(totals, 2))
with t2:
    st.image('images/coal.png', use_column_width='Auto')
    st.metric(label='Total Coal', value=numerize(total_coal, 2))
with t3:
    st.image('images/oil.png', use_column_width='Auto')
    st.metric(label='Total Oil', value=numerize(total_oil, 2))
with t4:
    st.image('images/gas.png', use_column_width='Auto')
    st.metric(label='Total Gas', value=numerize(total_gas, 2))
with t5:
    st.image('images/cement.png', use_column_width='Auto')
    st.metric(label='Total Cement', value=numerize(total_cement, 2))
with t6:
    st.image('images/flaring.png', use_column_width='Auto')
    st.metric(label='Totals Flaring', value=numerize(total_flaring, 2))
with t7:
    st.image('images/others.jpg', use_column_width='Auto')
    st.metric(label='Total Other', value=numerize(total_other, 2))

# Row B
st.markdown('### Graphs')
QT1, QT2, QT3, QT4 = st.tabs(["Oil per Country", "Coal per Country", "Gas per Country", "Cement per Country"])

# Oil per Country
with QT1:
    st.header("Total Oil Consumption per Country")
    Q1, Q2 = st.columns(2)
    with Q1:
        st.subheader("Bar Graph")
        df2 = df1.groupby(by=['Country']).sum()[['Oil', 'Total']].reset_index()
        df2['OTR'] = round(df2['Oil'] / df2['Total'] * 100, 3)
        fig_OTR = px.bar(df2, x='Country', y='OTR', title='<b>% of Oil against Totals</b>')
        fig_OTR.update_layout(title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)", xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)))
        st.plotly_chart(fig_OTR, use_container_width=True)

    with Q2:
        st.subheader("Line Graph")
        fig_oil_per_country = px.line(df1, x='Year', y=['Oil'], color='Country', title='<b>Yearly Oil Emmission By Countries</b>')
        fig_oil_per_country.update_xaxes(rangeslider_visible=True)
        fig_oil_per_country.update_layout(xaxis_range=['1950', '2021'], showlegend=False, title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)", xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)),)
        st.plotly_chart(fig_oil_per_country, use_container_width=True)

    st.header("Oil Purchase By Country")
    Q3, Q4 = st.columns(2)
    with Q3:
        st.subheader("Pie Chart")
        df3 = df1.groupby(by='Total').max()[(['Oil', 'Country'])].sort_values(by='Oil', ascending=False).reset_index().head(500)
        fig_oil_by_country = px.pie(df3, names='Country', values='Oil', title='<b>Oil Purchase By Country</b>')
        fig_oil_by_country.update_layout(title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_oil_by_country, use_container_width=True)

    with Q4:
        st.subheader("Bar Graph")
        df4 = df1.groupby(by='Country')[(['Oil', 'Total', 'Year'])].sum().sort_values(by='Country', ascending=False).reset_index().head(500)
        df4['OPC'] = round(df4['Oil'] / df4['Total'] * 100, 2)
        fig_OPC_by_year = px.bar(df4, x='Country', y='OPC', title='<b>Top Country with Highest % of Oil Purchase</b>')
        fig_OPC_by_year.update_layout(title={'x': 0.5}, xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)), plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_OPC_by_year, use_container_width=True)

# Coal per Country
with QT2:
    st.header("Total Coal Consumption per Country")
    Q1, Q2 = st.columns(2)
    with Q1:
        st.subheader("Bar Graph")
        df2 = df1.groupby(by=['Country']).sum()[['Coal', 'Total']].reset_index()
        df2['CTR'] = round(df2['Coal'] / df2['Total'] * 100, 3)
        fig_CTR = px.bar(df2, x='Country', y='CTR', title='<b>% of Coal against Totals</b>')
        fig_CTR.update_layout(title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)", xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)))
        st.plotly_chart(fig_CTR, use_container_width=True)

    with Q2:
        st.subheader("Line Graph")
        fig_coal_per_country = px.line(df1, x='Year', y=['Coal'], color='Country', title='<b>Yearly Coal Emmission By Countries</b>')
        fig_coal_per_country.update_xaxes(rangeslider_visible=True)
        fig_coal_per_country.update_layout(xaxis_range=['1950', '2021'], showlegend=False, title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)", xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)),)
        st.plotly_chart(fig_coal_per_country, use_container_width=True)

    st.header("Coal Purchase By Country")
    Q3, Q4 = st.columns(2)
    with Q3:
        st.subheader("Pie Chart")
        df3 = df1.groupby(by='Total').max()[(['Coal', 'Country'])].sort_values(by='Coal', ascending=False).reset_index().head(500)
        fig_coal_by_country = px.pie(df3, names='Country', values='Coal', title='<b>Coal Purchase By Country</b>')
        fig_coal_by_country.update_layout(title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_coal_by_country, use_container_width=True)

    with Q4:
        st.subheader("Bar Graph")
        df4 = df1.groupby(by='Country')[(['Coal', 'Total', 'Year'])].sum().sort_values(by='Country', ascending=False).reset_index().head(500)
        df4['CPC'] = round(df4['Coal'] / df4['Total'] * 100, 2)
        fig_CPC_by_year = px.bar(df4, x='Country', y='CPC', title='<b>Top Country with Highest % of Coal Purchase</b>')
        fig_CPC_by_year.update_layout(title={'x': 0.5}, xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)), plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_CPC_by_year, use_container_width=True)

# Gas per country
with QT3:
    st.header("Total Gas Consumption per Country")
    Q1, Q2 = st.columns(2)
    with Q1:
        st.subheader("Bar Graph")
        df2 = df1.groupby(by=['Country']).sum()[['Gas', 'Total']].reset_index()
        df2['GTR'] = round(df2['Gas'] / df2['Total'] * 100, 3)
        fig_GTR = px.bar(df2, x='Country', y='GTR', title='<b>% of Gas against Totals</b>')
        fig_GTR.update_layout(title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)", xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)))
        st.plotly_chart(fig_GTR, use_container_width=True)

    with Q2:
        st.subheader("Line Graph")
        fig_gas_per_country = px.line(df1, x='Year', y=['Gas'], color='Country', title='<b>Yearly Gas Emmission By Countries</b>')
        fig_gas_per_country.update_xaxes(rangeslider_visible=True)
        fig_gas_per_country.update_layout(xaxis_range=['1950', '2021'], showlegend=False, title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)", xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)),)
        st.plotly_chart(fig_gas_per_country, use_container_width=True)

    st.header("Coal Purchase By Country")
    Q3, Q4 = st.columns(2)
    with Q3:
        st.subheader("Pie Chart")
        df3 = df1.groupby(by='Total').max()[(['Gas', 'Country'])].sort_values(by='Gas', ascending=False).reset_index().head(500)
        fig_gas_by_country = px.pie(df3, names='Country', values='Gas', title='<b>Gas Purchase By Country</b>')
        fig_gas_by_country.update_layout(title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_gas_by_country, use_container_width=True)

    with Q4:
        st.subheader("Bar Graph")
        df4 = df1.groupby(by='Country')[(['Gas', 'Total', 'Year'])].sum().sort_values(by='Country', ascending=False).reset_index().head(500)
        df4['GPC'] = round(df4['Gas'] / df4['Total'] * 100, 2)
        fig_GPC_by_year = px.bar(df4, x='Country', y='GPC', title='<b>Top Country with Highest % of Gas Purchase</b>')
        fig_GPC_by_year.update_layout(title={'x': 0.5}, xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)), plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_GPC_by_year, use_container_width=True)

# Cement per Country
with QT4:
    st.header("Total Cement Consumption per Country")
    Q1, Q2 = st.columns(2)
    with Q1:
        st.subheader("Bar Graph")
        df2 = df1.groupby(by=['Country']).sum()[['Cement', 'Total']].reset_index()
        df2['CTR'] = round(df2['Cement'] / df2['Total'] * 100, 3)
        fig_CTR = px.bar(df2, x='Country', y='CTR', title='<b>% of Cement against Totals</b>')
        fig_CTR.update_layout(title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)", xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)))
        st.plotly_chart(fig_CTR, use_container_width=True)

    with Q2:
        st.subheader("Line Graph")
        fig_cement_per_country = px.line(df1, x='Year', y=['Cement'], color='Country', title='<b>Yearly Cement Emmission By Countries</b>')
        fig_cement_per_country.update_xaxes(rangeslider_visible=True)
        fig_cement_per_country.update_layout(xaxis_range=['1950', '2021'], showlegend=False, title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)", xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)),)
        st.plotly_chart(fig_cement_per_country, use_container_width=True)

    st.header("Coal Purchase By Country")
    Q3, Q4 = st.columns(2)
    with Q3:
        st.subheader("Pie Chart")
        df3 = df1.groupby(by='Total').max()[(['Cement', 'Country'])].sort_values(by='Cement', ascending=False).reset_index().head(500)
        fig_cement_by_country = px.pie(df3, names='Country', values='Cement', title='<b>Cement Purchase By Country</b>')
        fig_cement_by_country.update_layout(title={'x': 0.5}, plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_cement_by_country, use_container_width=True)

    with Q4:
        st.subheader("Bar Graph")
        df4 = df1.groupby(by='Country')[(['Cement', 'Total', 'Year'])].sum().sort_values(by='Country', ascending=False).reset_index().head(500)
        df4['CPC'] = round(df4['Cement'] / df4['Total'] * 100, 2)
        fig_CPC_by_year = px.bar(df4, x='Country', y='CPC', title='<b>Top Country with Highest % of Cement Purchase</b>')
        fig_CPC_by_year.update_layout(title={'x': 0.5}, xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)), plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_CPC_by_year, use_container_width=True)

git = 'https://github.com/MoBrian254'
linkdin = 'https://www.linkedin.com/in/brian-owana-web-developer/'
portfolio = 'https://mobrian-portfolio-01.vercel.app/'
st.markdown(f"<span>Follow me: <a href={git} target='_blank'>@Github</a> | <a href='{linkdin}' target='_blank'>@LinkedIn</a> | <a href='{portfolio}' target='_blank'>@Portfolio</a></span>", unsafe_allow_html=True)
