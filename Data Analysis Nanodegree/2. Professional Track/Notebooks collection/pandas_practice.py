import time
import numpy as np
import pandas as pd
import math
"""
# We create a dictionary of lists (arrays)
data = {'Integers' : [1,2,3],
        'Floats' : [4.5, 8.2, 9.6]}
k: DatetimeIndex = pd.date_range()
# We create a DataFrame 
df = pd.DataFrame(data)

# We display the DataFrame
print(df)
"""
# DO NOT CHANGE THE VARIABLE NAMES

# Set the precision of our dataframes to one decimal place.
pd.set_option('precision', 1)

# Create a Pandas DataFrame that contains the ratings some users have given to a series of books. 
# The ratings given are in the range from 1 to 5, with 5 being the best score. 
# The names of the books, the corresponding authors, and the ratings of each user are given below:

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

# User ratings are in the order of the book titles mentioned above
# If a user has not rated all books, Pandas will automatically consider the missing values as NaN.
# If a user has mentioned `np.nan` value, then also it means that the user has not yet rated that book.
user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])


# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. 
# Let Pandas automatically assign numerical row indices to the DataFrame. 

# TO DO: Create a dictionary with the data given above
dat = {'Author':authors,'Book Title':books,'User 1':user_1,'User 2':user_2,'User 3':user_3,'User 4':user_4}

# TO DO: Create a Pandas DataFrame using the dictionary created above
book_ratings = pd.DataFrame(dat)

# TO DO:
# If you created the dictionary correctly you should have a Pandas DataFrame
# that has column labels: 
# 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4' 
# and row indices 0 through 4.

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. 
# HINT: Use the `pandas.DataFrame.fillna(value, inplace = True)` function for substituting the NaN values. 
# Write your code below:
book_ratings.fillna(np.mean(book_ratings),axis=0, inplace = True)
print(book_ratings)

# Step 1 - Highlight the rows containing a value = 5. 
# This step will replace all values != 5 with NaN in the entire DataFrame. 
best_rated = book_ratings[(book_ratings == 5)]
        #print('\n',best_rated,'\n',type(best_rated))
# Step 2 - Extract the DataFrame containing only those rows that have a value = 5. 
best_rated = book_ratings[(book_ratings == 5).any(axis = 1)]
        #print('\n',best_rated,'\n',type(best_rated))
# Step 3 - Find the corresponding Book Title of the rows identified above. 
# Returns a numpy.ndarray containing only the Book Titles
best_rated = book_ratings[(book_ratings == 5).any(axis = 1)]['Book Title'].values
print('\n',best_rated,'\n',type(best_rated))