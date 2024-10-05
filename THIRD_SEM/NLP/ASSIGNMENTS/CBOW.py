import re
import numpy as np
import string
import pandas as pd 
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Load the dataset from the provided file path
file_path = 'data.csv'
df = pd.read_csv(file_path)

# Check the first few rows to understand the structure
print(df.head())

# Assuming the text column in the dataset is named 'text', you may need to adjust the column name
# if it is different. You can inspect the column names using df.columns to check.

# Join all the sentences from the text column into a single string
data = " ".join(df['Sentence'].values)

# Initialize the set of stopwords
stopwords = set(STOPWORDS)

# Generate the word cloud
wordcloud = WordCloud(
    background_color='white',
    stopwords=stopwords,
    max_words=200,
    max_font_size=40, 
    random_state=42
).generate(data)

# Create a plot with three identical word clouds for visualization
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(24, 24))

# Plot the word cloud in each of the three axes
for ax in axes:
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')  # Hide the axis

# Adjust the layout of the figure
fig.tight_layout()

# Display the plot
plt.show()
