import numpy as np
import streamlit as st
import pandas as pd
import pickle 

encoded_dict={
    "gender": {"Male":1, "Female":2},
    "product_no":{"1":1,"2":2,"3":3,"4":4},
    "credit_card":{"Yes":1,"No":2},
    "active_member":{"Yes":1,"No":2}
}
def model_pred(age,tenure,credit_score,gender,product_no,credit_card,active_member):
    #loading the model
    with open("churn_pred.pkl","rb") as file:
        reg_model=pickle.load(file)
    if(gender=="Male"):
        gen=1
    else:
        gen=0
    if(credit_card=="Yes"):
        cred=1
    else:
        cred=0
    if(active_member=="Yes"):
        active=1
    else:
        active=0
    input_features=[[age,credit_score,gen,tenure,0,product_no,cred,active,0]]
    return reg_model.predict(input_features)

col1,col2,col3,col4=st.columns(4)
gender = col1.selectbox("Select Gender",
                      ["Male","Female"])
product_no =col2.selectbox("Select product number",
                      [1,2,3,4])
credit_card =col3.selectbox("Credit card",
                      ["Yes","No"])
active_member = col4.selectbox("Member",
                      ["Yes","No"])
col11,col21,col31=st.columns(3)
age=col11.slider("Set age",
                100,18)
tenure=col21.number_input("tenure")
credit_score=col31.number_input("credit score")

if(st.button("Predict Churn")):
    churn=model_pred(age,tenure,credit_score,gender,product_no,credit_card,active_member)
    st.text("Will customer churn?: "+str(churn))