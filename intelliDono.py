#!/usr/bin/env python
# coding: utf-8

# In[374]:


import pandas as pd
# Describing the anomalies
features = pd.read_csv('winequalityN.csv')
#features= features.drop('ID', axis = 1)

features.head(10)


# In[375]:


# Describing anoma
features.describe()


# In[376]:


import numpy as np


# ### We want to predict the average in the next days.

# In[377]:



labels = np.array(features['quality'])
features= features.drop('quality', axis = 1)


feature_list = list(features.columns)


features = np.array(features)


# ## Make the training set and using the 25% of the data as testing set.
# ### The other 75% is used for training

# In[378]:


from sklearn.model_selection import train_test_split

train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.1, random_state = 42)


# ## Create 1000 decision trees
# #### Each one will calculate it's own prediction so everyone together can come up with a solution.

# In[379]:


from sklearn.ensemble import RandomForestRegressor

randomForest = RandomForestRegressor(n_estimators= 100, random_state=42)


# #### Train the trees with the training data

# In[380]:


randomForest.fit(train_features, train_labels);


# In[381]:


predictions = randomForest.predict(test_features)

errors = abs(predictions - test_labels)

print('Error:', round(np.mean(errors), 2), 'degrees.')


# In[382]:


mape = 100 * (errors / test_labels)


# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', accuracy, '%.')


# #### Improve number of decision trees if needed

# In[383]:


#improve model
rf_new = RandomForestRegressor(n_estimators = 100, criterion = 'mse', max_depth = None, 
                               min_samples_split = 2, min_samples_leaf = 1)


# In[384]:



# Get numerical feature importances
importances = list(randomForest.feature_importances_)

# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]

# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)

# Print out the feature and importances 
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];


# In[385]:


# New random forest with only the two most important variables
rf_most_important = RandomForestRegressor(n_estimators= 1000, random_state=42)

# Extract the two most important features
important_indices = [feature_list.index('alcohol'), feature_list.index('volatile acidity')]
train_important = train_features[:, important_indices]
test_important = test_features[:, important_indices]

# Train the random forest
rf_most_important.fit(train_important, train_labels)

# Make predictions and determine the error
predictions = rf_most_important.predict(test_important)

errors = abs(predictions - test_labels)

# Display the performance metrics
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

mape = np.mean(100 * (errors / 17))
accuracy = 100 - mape

print('Accuracy:', round(accuracy, 2), '%.')


# In[386]:


import matplotlib.pyplot as plt

# list of x locations for plotting
x_values = list(range(len(importances)))

# Make a bar chart
plt.bar(x_values, importances, orientation = 'vertical')

# Tick labels for x axis
plt.xticks(x_values, feature_list, rotation='vertical')

# Axis labels and title
plt.ylabel('Importance'); plt.xlabel('Variable'); plt.title('Variable Importances');


# In[387]:


import datetime
# Dates of training values
#months = features[:, feature_list.index('MONTH')]
#days = features[:, feature_list.index('DAY')]
#years = features[:, feature_list.index('YEAR')]

# List and then convert to datetime object
#dates = [str(int(year)) + '-' + str(int(month)) + '-' + str(int(day)) for year, month, day in zip(years, months, days)]
#dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in dates]

# Dataframe with true values and dates

alcohol = features[:, feature_list.index('alcohol')]

true_data = pd.DataFrame(data = {'alcohol': alcohol, 'actual': labels})

# Dates of predictions
alcohol = test_features[:, feature_list.index('alcohol')]

# Column of dates
#test_dates = [str(int(year)) + '-' + str(int(month)) + '-' + str(int(day)) for year, month, day in zip(years, months, days)]

# Convert to datetime objects
#test_dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in test_dates]

# Dataframe with predictions and dates
predictions_data = pd.DataFrame(data = {'alcohol': alcohol, 'prediction': predictions})


# In[ ]:





# In[392]:


# Plot the actual values
plt.plot(true_data['alcohol'], true_data['actual'], 'b-', label = 'real')

# Plot the predicted values
plt.plot(predictions_data['alcohol'], predictions_data['prediction'], 'ro', label = 'prediction')
plt.xticks(rotation = '60'); 
plt.legend()

# Graph labels
plt.xlabel('Alcohol'); plt.ylabel('Quality'); plt.title('Alcohol');


# In[ ]:





# In[ ]:





# In[ ]:




