import streamlit as st
import pandas as pd

df = pd.read_csv("startup_funding.csv")

#data cleaning
df['Investors Name']= df["Investors Name"].fillna('Undisclosed')

st.sidebar.title("Startup Funding Analysis")

option =st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUP', 'Investors'])

if option == "Overall Analysis":
    st.title('Overall Analysis')

elif option == 'StartUP':
    st.sidebar.selectbox('Select StartUP', sorted(df['Startup Name'].unique().tolist()))
    btn1 = st.sidebar.button("Find startup Details ")
    st.title('StartUP Analysis')


else:
    st.sidebar.selectbox('Select StartUP', sorted(df['Investors Name'].unique().tolist()))
    btn2 = st.sidebar.button('Find Investor Details')
    st.title('Investor Analysis')


