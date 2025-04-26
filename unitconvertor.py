#project 01 unit convertor
#build a unit convertor using python and streamlit

#Project 01: Unit Converter
#Build a google unit converter using python and streamlit

import streamlit as st
st.markdown (
    """
    <style>
    body {
        background-color:rgb(6, 6, 26);
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #1e1e2f);
        padding: 30px;
        border-radius:15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.4);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: black;
    }
    .stButton>button{
        backgrround: sky;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px darkblue;

    }
    .stButton>button:hover{
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9a7);
        color: black;
    }
    .result-box {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background: black(135deg,rgb(1, 1, 48),rgb(1, 1, 24));
        padding: 20px;
        border-radius: 10px;
        marging-top: 20px;
        box-shadow: 0px 5px 15px rgba(8, 187, 236, 0.3);
    }
    .footer{
        text-align: center;
        marging-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1> Unit Convertor using Python and Streamlit </h1>", unsafe_allow_html=True)
st.write("Easily conversion between different units of length, weight, and temperature.")

conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value =st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilograms", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feets"])
        with col2:
            to_unit = st.selectbox("To",["Meters", "Kilograms", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feets"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From",["Kilogram", "Grams", "Miligrams", "Pound" ]) 
        with col2:
            to_unit = st.selectbox("To",["Kilogram", "Grams", "Miligrams", "Pound" ])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Fahrenheit", "Celsius", "Kelvin"])
        with col2:
            to_unit = st.selectbox("To", ["Fahrenheit", "Celsius", "Kelvin"])


def length_convertor(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Milimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28, 'Inches': 39.37
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
         'Kilogram': 1, 'Gram': 1000, 'Miligram': 1000000, 'Pound': 2.2046,  
    }
    return (value / weight_units[from_unit]) * weight_units[from_unit] 

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 +32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value -32) * 5/9 + 273.15 if to_unit == "Kelvin" else value 
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit =="Fahrenheit" else value
    return value 

if st.button("Convertor"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_convertor(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

    st.markdown("<div class='footer'>Created with lots of efforts by Sundas Dilawer</div>", unsafe_allow_html=True)                                        

