import streamlit as st
import requests

st.title("API Data Sample")

with st.form("form"):
    command=st.text_input("Enter your command")
    worktype=st.text_input("Enter your work type")
    workrate=st.text_input("Enter your work rate")

    submitted=st.form_submit_button("Submit")

if submitted:
    url="https://4hggabmds3.execute-api.ap-south-1.amazonaws.com/PreProduction/Tracker"

    payload={
        "command":command,
        "worktype":worktype,
        "workrate":workrate,
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
