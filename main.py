import streamlit as st
import pandas as pd

df = pd.read_csv("startup_cleaned.csv")



st.sidebar.title("Startup Funding Analysis")

option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUP', 'Investors'])

if option == "Overall Analysis":
    st.title('Overall Analysis')

elif option == 'StartUP':
    st.sidebar.selectbox('Select StartUP', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button("Find startup Details ")
    st.title('StartUP Analysis')


else:
    st.sidebar.selectbox('Select StartUP', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    st.title('Investor Analysis')


