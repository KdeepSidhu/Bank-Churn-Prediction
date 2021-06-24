![image](https://user-images.githubusercontent.com/64827508/122140576-e27f8400-ce08-11eb-89c5-f56099efd9d1.png)

# Live Demo:
check out this project live here
https://kukaurchurn.herokuapp.com/ 

# Problem Statement:
A Bank wants to take care of customer retention for its product: savings accounts. The bank wants you to identify customers likely to churn balances below the minimum balance. You have the customers information such as age, gender, demographics along with their transactions with the bank.
My task as a data scientist would be to predict the propensity to churn for each customer.

# Challenges:
Some financial services customers become quite valuable as they generate fees on transactions and grow a portfolio of business over the years including banking fees, credit cards, home loans, personal loans and more. Simple churn analysis uses rules based on known behaviors to identify potential churn risks. Rules-based systems, however, are inflexible and miss many customers who do churn and generate false positives that end up giving expensive incentives to customers who were not at risk to leave the bank.

# Opportunity :
AI is a great solution for customer churn prediction as the problem involves complex data over time and interactions between different customer behaviors that can be difficult for people to identify. AI can look at a variety of data, including new data sources, and at relatively complex interactions between behaviors and compared to individual history to determine risk. AI can also be used to recommend the best offer that will most likely retain a valuable customer. In addition, AI can identify the reasons why a customer is at risk and allow financial institution to act against those areas for the individual customer and more globally.


I build a HtML CSS website and build Backend with Django and connect with model and deploy it on heroku platform

# Approaching the Solution:


# Step One: Collecting Data
Took data From UCi machine learning repository. There are many other sources available for taking data like kaggle , open source databases etc.

# Step two: setup your computer:
First of all download all the required library and tools. and setup our Machine.
- Anaconda
- VS Code
- Numpy
- Pandas
- Sklearn
- Git
- Django
- setup vertual enviornment
- Create heroku account
- download heroku on local computer

# Step Three: Data Analisys:
Analyse the data with the help of matplotlib and seaborn library. done analisys by Univariate and Bivariate method and
find out meaningfull insights of the data. this insights help us to taking some decision regarding data engineering and model building and selection.
for whole analysys insights go to the final project file and read it.

# Step Four: Data Engineering:
After geting the data undestanding we move forward for the data cleaning or data engineering parts. In this data have lots have null values and there are many outliers we 
fill null values with some logical undestanding, delete unwanted columns, and standardize the data, encode the data also.
- Remove unwanted Columns.
- Fill Null values with analisys.
- Remove outliers
- create dummy variable for categorical data
- Scale the data with min max scaler
# Step five: Model building:
After data cleaning build a ML model on that. split data and build a five models
- Decision tree
- Random Forest
- SVM
- Logistic Regression
- KNN
after building model Evalute uits performance metrics find out confusion metrix , precision , recall and accuracy for each model.


# Step Six: HyperparameterTuning:
 For each model tune the hyper parameter with the help of gridSearch CV. 
 
 # Step Seven: Model Selection:
 
 SElect best model on the basis of Best performance we select random forest becouse its accuracy, precision, recall is better than other model.
 
 # Step Eight: Build Website and Deploye:
 Built a HtML CSS website and build Backend with Django and connect with model and deploy it on heroku platform
 



