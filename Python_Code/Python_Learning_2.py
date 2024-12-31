import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import seaborn as sns
from sklearn.datasets import load_iris
#-------------------------------------------------------------------------------
# st.write ('Hello World!')

#-------------------------------------------------------------------------------

# col_name = ['Column1', 'Column2', 'Column3']

# data = pd.DataFrame(np.random.randint(30, size=(30, 3)), columns=col_name)

# 'Line Graph:'
# st.line_chart(data)

# 'Bar Chart:'
# st.bar_chart(data)


# # animal example

# animals = ['cat', 'cow', 'dog']
# heights = [30, 150, 80]

# 'Pie Chart:'
# fig, ax = plt.subplots()
# ax.pie(heights, labels=animals)

# st.pyplot(fig)
# ------------------------------------------------------------------------------
## Line charts in Streamlit
# Create a line chart which we'll grow overtime

# rows = np.random.randn(1,1)

# 'Growing Line Chart:'
# Chart = st.line_chart(rows)

# for i in range(1,100):
#     new_rows = rows[0] + np.random.randn(1,1)
#     # add rows method
#     Chart.add_rows(new_rows)
#     rows = new_rows
#     time.sleep(0.05) # to stop it for 5 milscond
    
    
#     values = np.random.rand(10)
#     'Matplotlibs Line Chart:'
#     fig, ax = plt.subplots()
#     ax.plot(values)
#     st.pyplot(fig)
#-------------------------------------------------------------------------------
## Bar charts and pie charts in Streamlit  
    
    
# animal = ['cat', 'cow', 'dog', 'goat']
# heights = [30, 150, 80, 60]
# weights = [5, 400, 40, 50]

# fig, ax = plt.subplots()

# x = np.arange(len(heights))
# width = 0.40 

# ax.bar(x - 0.2, heights, width, color='red')
# ax.bar(x + 0.2, weights, width, color='orange')

# # legend method out of the ax object
# ax.legend(['height', 'weight'])
# ax.set_xticks(x)
# ax.set_xticklabels(animal) 


# st.pyplot(fig) 

# # same thing in pie chart

# explode = [0.2, 0.1, 0.1, 0.1]

# plot_pie, ax = plt.subplots()
# ax.pie(heights, explode=explode, labels=animal, autopct='%1.1f%%', shadow=True) # show the percentage in pie chart with autopct='%1.1f%%'
# ax.axis('equal') # equal is a key word that make sure pie as a cyrcle 
# st.pyplot(plot_pie)
#-------------------------------------------------------------------------------
## Create statistical charts

iris_data = load_iris()
data = pd.DataFrame(iris_data.data, columns = iris_data.feature_names)

fig = plt.figure()
sns.histplot(data=data, bins=20)
st.pyplot(fig)

# box plot
fig = plt.figure()
sns.boxplot(data=data)
st.pyplot(fig)
    
# scatter plot

fig = plt.figure()
sns.scatterplot(data=data)
st.pyplot(fig)
    
    
    
    
    
    
    
    
    
    
    
    





































