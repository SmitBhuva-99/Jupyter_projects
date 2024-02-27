# **Yield Prediction Model for Cumin:** 

This script contains a yield prediction model for cumin using various regression techniques. The model is built using historical yield data and weather variables.

## **Team members:**
1. Parth Patel : www.github.com/Parth-Patel-4403
2. Piyush Pandya : www.github.com/Piyushpandya83
3. Viraj Hirpara : www.github.com/Viraj-Patel07

## **Table of Contents**: 
1. Data Preparation 
2. Regression Models 
   1. Linear Regression 
   2. Polynomial Regression 
   3. Deep Neural Network 
   4. Elastic Net Regression 
   5. Random Forest Regression 
   6. Ridge Regression 
   7. Lasso Regression 
3. Prediction for New Years 
4. Data Preparation

The first part of the script focuses on preparing the data for the regression models. The CSV file is loaded, and rows with zero values in 'area' or 'yield' are removed. Then, the features (X) and target variable (y) are defined. The data is split into training and testing sets, and the features are scaled using StandardScaler. Finally, Principal Component Analysis (PCA) is applied to keep only 8 principal components, and the data is transformed.

## **Data Sources:**
1. For Mean Evapotranspiration and Mean NDVI : MODIS dataset using Google Earth Engine
2. For Area and Production of crop: Directorate of Agriculture, Gujarat Government (Link: https://dag.gujarat.gov.in/estimate.htm)
3. For Average temperature, Minimum temperature, Maximum temperature, Mean Rainfall and Dew point temperature : ERA5 dataset using Google Earth Engine

## **Regression Models**:
1. **Linear Regression**: A simple linear regression model is implemented using TensorFlow's Sequential API. The model is trained on the scaled and transformed data using the Mean Squared Error loss function and Adam optimizer.


2. **Polynomial Regression:**: A polynomial regression model of degree 2 is implemented in this section. PolynomialFeatures from scikit-learn is used to create polynomial and interaction features, and the transformed data is used to train the model.


3. **Deep Neural Network:** A deep neural network regression model is implemented using TensorFlow's Sequential API. The model consists of two hidden layers with 64 neurons each, and one output layer. The model is trained on the scaled and transformed data using the Mean Squared Error loss function and Adam optimizer.


4. **Elastic Net Regression:**: Elastic net regression combines L1 and L2 regularization and is implemented using TensorFlow's Sequential API. The model is trained on the scaled and transformed data using the Mean Squared Error loss function and Adam optimizer.


5. **Random Forest Regression:**: Random Forest Regression is a non-parametric ensemble model that averages the predictions of multiple decision trees. The model is implemented using scikit-learn's RandomForestRegressor and trained on the scaled and transformed data.


6. **Ridge Regression:**: Ridge regression adds L2 regularization to the model and is implemented using TensorFlow's Sequential API. The model is trained on the scaled and transformed data using the Mean Squared Error loss function and Adam optimizer.


7. **Lasso Regression:** Lasso regression adds L1 regularization to the model and is implemented using TensorFlow's Sequential API. The model is trained on the scaled and transformed data using the Mean Squared Error loss function and Adam optimizer.

**Prediction for New Years:** After selecting the best model based on evaluation metrics, the user can prepare a new DataFrame with the required features for predicting the cumin yield in the new years. The best model is used to predict the yields for the new years, and the predictions are printed.

## **Dependencies**:
1. pandas 
2. tensorflow 
3. scikit-learn 

**Running the Script:** To run the script, make sure the required dependencies are installed, and execute the script using a Python interpreter. The cumin_data.csv file should be in the specified path in the script.
