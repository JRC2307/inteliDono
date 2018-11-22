# Random Forests
## Doughnut per day prediction
## Wine quality prediction
#### Subject: Artificial Intelligence

    A01184855 Esteban Quintana C.
    A01152572 Javier Rodríguez C. L.
    Professor: Ruben Stranders.

### Introduction
&nbsp;This challenge was chosen on the premise of a real life trouble we encountered: A recently built Food-based startup has a lot of trouble finding out how many doughnuts should be made for a certain day while reducing waste from sloppy sales days. We looked for different ways of building a reliable prediction system for this case, like **Neural Networks** and **Decision Trees** but we ended up implementing the solution on a **Random Forest**.

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
