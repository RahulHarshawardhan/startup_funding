import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='startUp Analysis')

df = pd.read_csv("startup_cleaned.csv")

def load_investor_details(investor):
    st.title(investor)
    #Load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader("Most Recent Investments")
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        #biggest investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending = False).head()
        st.subheader("Biggest Investments")
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)
    with col2:
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series, autopct="%0.01f%%")
        st.pyplot(fig1)

        




    #st.dataframe(big_series)





st.sidebar.title("Startup Funding Analysis")

option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUP', 'Investors'])

if option == "Overall Analysis":
    st.title('Overall Analysis')

elif option == 'StartUP':
    st.sidebar.selectbox('Select StartUP', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button("Find startup Details ")
    st.title('StartUP Analysis')


else:
    selected_investor = st.sidebar.selectbox('Select StartUP', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)




