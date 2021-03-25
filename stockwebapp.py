from PIL import Image
import streamlit as st
import pandas as pd



image=Image.open("C:/Python/Python38/stock_market.jpg")
st.image(image,use_column_width=True)
st.sidebar.header('User Input')
#creating a function for users iput
def get_input():
    start_date=st.sidebar.text_input("Start Date","10/21/2019")
    end_date = st.sidebar.text_input("End Date", "10/16/2020")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date,end_date,stock_symbol
#create the functiom with company name
def get_company_name(symbol):
    if symbol=="AMZN":
        return 'Amazon'
    elif symbol=="TSLA":
        return "Tesla"
    elif symbol=="GOOG":
        return "Alphabet"
    else:
        'None'
#create a function to get the proper company name and the proper timeframe from the user start date to end date
def get_data(symbol,start,end):
    #load the data
    if symbol.upper()=='AMZN':
        df=pd.read_csv('C:/Users/Sai Ram/PycharmProjects/pythonProject/test1/AMZN.csv')
    elif symbol.upper()=='TSLA':
        df=pd.read_csv('C:/Users/Sai Ram/PycharmProjects/pythonProject/test1/TSLA.csv')
    elif symbol.upper()=='GOOG':
        df=pd.read_csv('C:/Users/Sai Ram/PycharmProjects/pythonProject/test1/GOOG.csv')
    else:
        df=pd.DataFrame(columns=['Date','Open','High','Low','Adj Close','Volume'])
    # get the data rage
    start=pd.to_datetime(start)
    end=pd.to_datetime(end)
    #set the start and end to 0
    start_row=0
    end_row=0
    #start the date from data set  top to down if the users start date is less than equal to date it he dataset
    for i in range(0, len(df)):
        if start<= pd.to_datetime(df['Date'][i] ):
            start_row=i
            break
    for j in range(0,len((df))):
        if end>=pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row=len(df)-1-j
            break
    df=df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row+1,:]
start,end,symbol=get_input()
df=get_data(symbol,start,end)
company_name=get_company_name(symbol.upper())
st.header(company_name+"Close Price\n")
st.line_chart(df['Close'])
st.header(company_name+"Volume\n")
st.line_chart(df['Volume'])
st.header('Data Statistics')
st.write(df.describe())








