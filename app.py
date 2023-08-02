import streamlit as st
import pandas as pd
import pickle
from PIL import Image
model = pickle.load(open("cpp.pkl", "rb"))

df = pd.read_csv("Cleaned_CarPrice.csv")
cname = df["carname"].unique()
ftype = df["fueltype"].unique()
cbody = df["carbody"].unique()
dwheel = df["drivewheel"].unique()
etype = df["enginetype"].unique()


st.title("Car Price Predictor")

image = Image.open('dealer-lot-hero.jpg')
st.image(image)


cname1 = st.selectbox("**Select Car Name :**", cname, index=0)
ftype1 = st.selectbox("**Select Fuel Type :**", ftype, index=0)
cbody1 = st.selectbox("**Select Car Body Type :**", cbody, index=0)
dwheel1 = st.selectbox("**Select Drive Wheel :**", dwheel, index=0)
etype1 = st.selectbox("**Select Engine Type :**", etype, index=0)
hp1 = st.number_input("**Enter horsepower :**")

if st.button("Predict"):
    prediction = int(model.predict(pd.DataFrame([[cname1, ftype1, cbody1, dwheel1, etype1, hp1]],
                                                columns=["carname", "fueltype", "carbody", "drivewheel", "enginetype", "horsepower"])))
    st.write(f"### Predicted Price is :- $ {prediction} ")
