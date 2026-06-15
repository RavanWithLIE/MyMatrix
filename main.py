import streamlit as st
import requests

st.title("My Updater")

with st.form("form"):
    ACName=st.text_input("Enter Acount")
    TType=st.selectbox("Select your Transaction Type",["Credit","Debit"])
    AMT=st.number_input("Enter your amount per month",step=0.1)

    submitted=st.form_submit_button("Submit")

if submitted:
    url="https://4hggabmds3.execute-api.ap-south-1.amazonaws.com/PreProduction/Tracker"

    payload={
        "command":"Add",
        "ACName":ACName,
        "trans": TType=="Credit",
        "amount":AMT,
    }

    headers = {
        "Content-Type": "application/json",
    }

    try:
        response=requests.post(url,json=payload,headers=headers)

        if response.status_code == 201 or response.status_code == 200:
            st.success("Your command has been submitted")
            st.json(response.json())
        else:
            st.error("Your command is not valid")
            st.write("Your command is not valid")
    except requests.exceptions.RequestException as e:
        st.error(e)
