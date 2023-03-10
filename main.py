import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='startUp Analysis')

df = pd.read_csv("startup_cleaned.csv")
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month


def load_overall_analysis():
    st.title("Overall Analysis")

    #total Invested Amount:
    total= round(df['amount'].sum())

    # Max amount infused in startup
    max_funding= df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]

    #Total Funded Startups
    total_funded = df['startup'].nunique()

    #Average ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('Total Funding', str(total) + " Cr")
    with col2:
        st.metric('Max Funded startup', str(max_funding) + " Cr")
    with col3:
        st.metric('Overall Average Funding in India', str(round(avg_funding)) + " Cr")
    with col4:
        st.metric('Total Funded startups', str(total_funded))


    st.header('MOM graph')
    selected_options = st.selectbox('select Type',['Total', 'Count'])
    if selected_options == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])
    st.pyplot(fig3)


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

    df["year"] = df["date"].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('YOY Investment')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index, year_series.values)
    st.pyplot(fig2)




    #st.dataframe(big_series)





st.sidebar.title("Startup Funding Analysis")

option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUP', 'Investors'])

if option == "Overall Analysis":
    load_overall_analysis()



elif option == 'StartUP':
    st.sidebar.selectbox('Select StartUP', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button("Find startup Details ")
    st.title('StartUP Analysis')


else:
    selected_investor = st.sidebar.selectbox('Select StartUP', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)




