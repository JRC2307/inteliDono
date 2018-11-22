# Random Forests
## Doughnut per day prediction
## Wine quality prediction
#### Subject: Artificial Intelligence

    A01184855 Esteban Quintana C.
    A01152572 Javier Rodríguez C. L.
    Professor: Ruben Stranders.

### Introduction
&nbsp;This challenge was chosen on the premise of a real life trouble we encountered: A recently built Food-based startup has a lot of trouble finding out how many doughnuts should be made for a certain day while reducing waste from sloppy sales days. We looked for different ways of building a reliable prediction system for this case, like **Neural Networks** and **Decision Trees** but we ended up implementing the solution on a **Random Forest**.

In order to understand how the algorithm works in a more profound manner we tested the program using two different datasets;
  - Data from the doughnut business from the past year
  - Data of wine quality scores using certain attributes of it, like alcohol grade, acidity and others.

### Justification
&nbsp; A Random Forest(RF) is a supervised machine learning algorithm. It can be used for both, _classification_ and _regression_. A **RF** is created by a collection of _Decision Trees_, the more trees that are used in the forest the highest accuracy the model has.

The implementation of AI on small businesses can be a great way of kickstarting them by reducing loss and improving areas to satisfy the customers better.
Calculating the amount of food that might be sold on a certain day is a complex problem, because many factors have to come into account, for example; the weather, the day of the week or the variety of ingredients available. By using **RF** we can train the model over almost every possible variation there is for the dataset and valuing the importance of each label.
It would take a way bigger effort to attempt to approach this result by using common statistical methods. Therefore we attempted to solve it by using a **ML** Algorithm.


### Documentation
This project was developed using **Python 3.7** mounted on a **Jupyter notebook**

For the implementation we made use of the following libraries:
    - **Numpy**: A python library used very commonly for the bast amount of mathematical functions it contains.
    - **Pandas**: A Data Analysis-focused library for python.
    - **SciKit-Learn**: This is a Machine learning focused library which enables the user to use many algorithms like: random forests, clustering, classification, SVM etc..
    - **matplotlib**: Very usefull library for plotting data on python.

After installing Python3, run the following commands from the terminal:

    $ python3 -m pip install jupyter
    $ pip install -U scikit-learn
    $ pip install pandas
    $ pip install numpy
    $ pip install matplotlib

After installing the libraries go into the folder the project is located and run:
    $ jupyter notebook

While inside Jupyter Notebook click on the **.ipynb** project and click on the double arrow to run it.

### Analysis
After looking and understanding at the results for the doughnut business we noticed that the amount of data was:
  1. Very little, since it only had 140 days worth of data.
  2. Didn't have enough features to be able to categorize the information correctly.

After interpreting the data from the wine ****

If there are too many trees and too little info it's probable that the result will be overfitted providing misleading or wrong results.

In order to improve this experiment we believe we first need to improve the data gathering process, also the preprocessing of data is also crucial since we can exclude the information that might interfere with the results or add features obtained from other data that is present on the data set. Some examples of the features we plan to retrieve for a future iteration are;
    - Day of the week
    - Season of the year
    - Previous week same day sales
    - Two weeks ago same day sales
    - A year ago same day sales

We believe this information will provide a better accuracy when predicting the amount of product that will be needed on a certain day to reduce the amount of waste that the business produces.
