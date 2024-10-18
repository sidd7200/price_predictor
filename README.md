# Bangalore House Price Predictor

Overview:
The Bangalore House Price Predictor is a machine learning-based web application that predicts house prices in Bangalore, India, based on various features like location, square footage, number of bedrooms, bathrooms, and more. This project aims to help users estimate the value of residential properties by providing an easy-to-use interface that gives quick, accurate price predictions.

The prediction model is trained on historical data from real estate listings in Bangalore, offering insights into property prices across different localities and house configurations.

Key Features
Price Prediction: Predicts the price of a property based on user input.
User-friendly Interface: Simple and intuitive UI built using Streamlit.
Efficient and Accurate: Leverages machine learning algorithms to provide accurate predictions.
Dynamic Data Handling: Flexible input options for users to define the property details like location, size, and configuration.

How It Works
The model behind the Bangalore House Price Predictor is built using a Linear Regression algorithm, trained on a dataset containing real estate information from Bangalore. The features used in the model include:

- Location of the property
- Total square footage
- Number of bedrooms
- Number of bathrooms
- Availability status
These features allow the model to predict house prices based on historical data trends.

The data is preprocessed, including handling missing values, removing outliers, and encoding categorical variables like location. After training the model, it is integrated into a web app using Streamlit, which provides a seamless user interface for interacting with the prediction model.

Data Source
The dataset used in this project contains real estate listings from various localities in Bangalore. It includes features such as:

- Location
- Total Square Footage
- Bedrooms
- Bathrooms
- Price
  
The data was cleaned, and outliers were removed to improve the model's performance. Categorical variables, such as location, were encoded using OneHotEncoding to make the data suitable for the regression model.

Machine Learning Model
The house price prediction model was developed using Multiple Linear Regression. Key metrics used to evaluate the model include:

Technologies Used
- *Streamlit:* To build the web application interface.
- *Pandas:* For data manipulation and preprocessing.
- *Scikit-learn:* To develop and train the regression model.
- *NumPy:* For numerical computations.
- *Python:* The main programming language used for building the model and web app.

App Link: [https://pricepredictor-2w9q8k3xaizff9rzar5bd2.streamlit.app]
