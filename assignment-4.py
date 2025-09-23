import streamlit as st

st.title("Assignment 4")

unit = st.radio("Select Units for Temperature Convertion: ",['Celsius',"Fahrenheit"])
temp = st.text_input(f"Enter Temperature in {unit}")
bt = st.button("Convert",type="primary",width="stretch")
targetUnit = "Fahrenheit" if unit == "Celsius" else "Celsius"
if bt:
    try:
        temp = int(temp)
        if unit == "Celsius":
            targetUnit ="Fahrenheit"
            temp = ((temp * 9) / 5) + 32

        elif unit == "Fahrenheit":
            targetUnit = "Celsius"
            temp = ((temp - 32) * 5) / 9
    except:
        st.error("Please enter a valid number.")
        exit();


    st.success(f"Temperature in {targetUnit} is {temp.__round__()}")

clearBtn = st.button("Clear",width="stretch")
if clearBtn:
    st.rerun()
