import streamlit as st
import yfinance as yf

st.set_page_config(page_title='MoBrian254 Stock Price App',
                    layout='wide',
                    initial_sidebar_state='expanded')

tickerSymbols = ['GOOGL', 'AAPL', 'AIMD', 'PXMD', 'TSLA', 'SGEN', 'ILMN', 'MTCH', 'SGTX']

header_mid, header_right = st.columns([3, 1], gap='large')

with st.sidebar:
    st.header("MoBrian254")
    ticker_input = st.sidebar.selectbox(label="Choose stock", options=tickerSymbols)


with header_mid:
    st.write("""
    # MoBrian254 Demo Stock Price App
    
    Displays the Closing price , Opening price and Volumes for various Stock Markets 
    in the period 2020-8-31 to 2022-8-31
    
    """)

    ticker_data = yf.Ticker(ticker_input)
    ticker_df = ticker_data.history(period='1d', start='2020-8-31', end='2022-8-31')

    t1, t2, t3 = st.tabs(["Closing", "Opening", "Volume"])
    with t1:
        st.header(f"{ticker_input} Closing Price Chart")
        st.line_chart(ticker_df.Close)

    with t2:
        st.header(f"{ticker_input} Opening Price Chart")
        st.line_chart(ticker_df.Open)

    with t3:
        st.header(f"{ticker_input} Volume Chart")
        st.line_chart(ticker_df.Volume)

git = 'https://github.com/MoBrian254'
linkdin = 'https://www.linkedin.com/in/brian-owana-web-developer/'
portfolio = 'https://mobrian-portfolio-01.vercel.app/'
st.markdown(f"<span>Follow me: <a href={git} target='_blank'>@Github</a> | <a href='{linkdin}' target='_blank'>@LinkedIn</a> | <a href='{portfolio}' target='_blank'>@Portfolio</a></span>", unsafe_allow_html=True)