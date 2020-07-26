# Analysis and Prediction of used car prices
## -Anmol Agarwal
## Aim
The aim is here to develop a ML model that predicts the price of used cars based on its features, in order to make informed purchases. The model is trained on a dataset consisting of sale prices of different makes and models across cities in India.

## Motivation
When shopping for a used vehicle, typically an overriding concern is: **Am I paying too much?**  This question is often difficult to answer due to the fact that it's hard to keep track of all the vehicles of interest currently available on the market.

Deciding if a used car is worth the cost put by the seller is a difficult task. Even for the seller, it is a challenge to decide the selling price of a car as it should neither be too low so as to cause a loss, nor too high that it puts off potential customers. Several factors including **make,model,year,kms driven etc** can affect the actual worth of a car. The motivation of this project is to help predict correct worth of used cars.

## Dataset and preprocessing
For this project, we are using the dataset on used car sales from India.The features available in this dataset are **Mileage, Make, Model, Year, kms travelled,transmisson, fuel type and City.**
The dataset is [here](Data_Train(1).xlsx). The missing outliers/anomalous data was dealt with/replaced with data from [CarDekho](https://www.cardekho.com/)

## The Model and analysis
The model and corresponding analysis can be found [here](ML_model.ipynb).

## Deployment
The model is being hosted [here](https://prediction-of-used-car-prices.herokuapp.com/).
The data was processed and stored [here](ideal.xlsx) to be used by [index.py](index.py).

[index.py](index.py) trains the model and stores the regressor as a .pickle file.
The routes developed via Flask along with the code to manage user inputs can be found in [actual.py](actual.py).

## Final Conclusions
Like most data science problems, this work would have undoubtedly benefitted from cleaner (and more) data. While the details provided in the downloaded listings are quite comprehensive,some features, especially 'name',seemed to have too many variations with even the same car model having multiple sub-categories.

I utilized several classic and state-of-the-art methods, including
ensemble learning techniques, with a 90-10 split on test and training
data.



| Model             	| R2 scores for a 90-10 split on Training data 	|
|-------------------	|----------------------------------------------	|
| XgBoost           	| 0.95                                         	|
| RandomForest      	| 0.927                                        	|
| Linear Regression 	| 0.60                                         	|
| Gradient Boosting 	| 0.90                                         	|

Although the scores predicted by both **XgBoost** and **Random Forest** seem quite reasonable, ***XgBoost seems to give slightly better results than RandomForest.***

# Future Plans
When I have time,I plan to improve the predictions and to include an option in the form where the user himself/herself selects the algorithm which he/she wants to use to predict the price of the specified car.
