import pandas as pd
# Create a dataFarame from a dictionary
data = {'name': ['Alice', 'Bob','Caarlie'],
        'age': {25, 30, 22},
        'city': ['New york', 'san francisco', 'Los Angeles']
        }
df = pd.DataFrame(data)

# Display the DateFrame
print ("orginal Dataframe:")
print (df)

# Select and display only the 'Name' column
name_column = df ['name']
print ("\nName column:")
print (name_column)

# Add a new column 'Salary'
df ['salary'] = [50000, 60000, 450000]

# Display the updated DataFrame
print ("\nUpdataed DataFrame with Salary column:")
print (df)

# Calculate the mean age of individuals in the DataFrame
mean_age = df ['age'].mean()
print ("\nMean age:",mean_age)