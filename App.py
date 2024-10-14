import streamlit as st
import pickle
import json
import numpy as np
import sklearn


# Load the model and columns
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    with open("columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 are sqft, bath, bhk

    with open("banglore_home_prices_model.pkl", "rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


# def predict_price(location, sqft, bath, bhk):
#     try:
#         loc_index = __data_columns.index(location.lower())
#     except:
#         loc_index = -1
#
#     x = np.zeros(len(__data_columns))
#     x[0] = sqft
#     x[1] = bath
#     x[2] = bhk
#     if loc_index >= 0:
#         x[loc_index] = 1
#
#     return round(__model.predict([x])[0], 2)
def predict_price(location, sqft, bath, bhk):
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    if loc_index >= 0:
        x[loc_index] = 1

    # Debugging info
    print(f"Number of features in data columns: {len(__data_columns)}")
    print(f"Feature vector length: {len(x)}")
    print(f"Model expected input length: {__model.n_features_in_}")

    return round(__model.predict([x])[0], 2)


# Load the model and columns when the app starts
load_saved_artifacts()

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Set background color */
    body {
        background-color: #f0f2f6;
    }

    /* Change title color and size */
    .stTitle {
        color: #4a4e69;
        font-size: 40px;
    }

    /* Change headers color */
    .stHeader {
        color: #9a8c98;
    }

    /* Style the input fields */
    input[type=number] {
        background-color: #fefae0;
        color: #3a3b3c;
        border-radius: 10px;
    }

    /* Style the select box */
    .stSelectbox {
        border-radius: 10px;
        color: #4a4e69;
        
    }
    .stSelectbox label{
        color: 'black';
        display:none;
    }

    /* Style the button */
    .stButton button {
        background-color: #f77f00;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 8px 20px;
    }

    /* Align the button and center it */
    .stButton {
        display: flex;
        justify-content: center;
    }

    /* Customize success message */
    .stAlert {
        background-color: #d8f3dc;
        color: #2d6a4f;
        font-weight: bold;
        border-radius: 5px;
    }
    .location-label {
        color: white !important;
        background: none !important;
        padding: 0 0 5px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
st.title("Bangalore House Price Prediction")

# Input fields
st.header("Enter the details:")

sqft = st.number_input("Total Square Feet", min_value=300.0, max_value=10000.0, step=100.0, value=1000.0)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1, value=2)
bhk = st.number_input("Number of BHK", min_value=1, max_value=10, step=1, value=3)

# Location select box from pre-loaded locations
location_label = st.empty()
location_label.markdown('<div class="location-label">Location</div>', unsafe_allow_html=True)
location = st.selectbox("", __locations)


# When the user clicks the "Predict" button
if st.button("Predict Price"):
    price = predict_price(location, sqft, bath, bhk)
    st.markdown(f"<h3 style='color: white;'>The estimated price for the house is ₹ {price} Lakh.</h3>", unsafe_allow_html=True)
