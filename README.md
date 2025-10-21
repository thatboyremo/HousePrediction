# HousePrediction
# Imported the necessary Python libraries (pandas, numpy, scikit-learn, etc.).
# Imported the housing dataset.
# Cleaned the data by checking for missing values and duplicated entries.
# Mapped the categorical values “Yes” and “No” to 1 and 2 respectively using the map() function.
# Dropped the Furnishing Status column since it was not needed for the model.
# Separated the dataset into features (X) and target variable (Y).
# Split the data into training and testing sets.
# Trained the regression model using the training data.
# Used the model to make predictions on the test (X_test) data.
# Evaluated the model’s performance using R² score and RMSE.
# Saved the trained model as hmodel.pkl.
# Logged in to GitHub and created a repository named “House Prediction”.
# Created a requirements.txt file to document dependencies.
# Opened the terminal and created a new virtual environment named “housing”.(conda create)
# Initialized Conda (conda init) and activated the environment (conda activate housing).
# Installed the required libraries using pip install streamlit numpy pandas matplotlib scikit-learn.
# Created a Python file named app.py.
# Loaded the trained model inside app.py.
# Built the Streamlit interface to collect user input.
# Converted user input into a DataFrame.
# Added a “Predict” button to display the estimated house price.
# Ran pip freeze > requirements.txt to update the dependency file.
# Deployed the application on Streamlit Cloud.
