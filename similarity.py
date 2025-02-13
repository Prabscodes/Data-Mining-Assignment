# -------------------------------------------------------------------------
# AUTHOR: Prabhakara Teja Kambhammettu
# FILENAME: similarity.py
# SPECIFICATION: Python program to find and output the two most similar documents from the dataset based on their cosine similarity.
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: 6 hours+
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy,
#pandas, or other sklearn modules.
#You have to work here only with standard dictionaries, lists, and arrays

# Importing some Python libraries
import csv
from sklearn.metrics.pairwise import cosine_similarity

documents = []

#reading the documents in a csv file
with open('cleaned_documents.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         documents.append (row)
         print(row)

#Building the document-term matrix by using binary encoding.
#You must identify each distinct word in the collection without applying any transformations, using
# the spaces as your character delimiter.
#--> 
# Creating Vocabulary
vocabulary = set()
for doc in documents:
    words = doc[1].split()
    vocabulary.update(words)

# Converting vocabulary into ordered list 
vocabulary = list(vocabulary)

# Building document-term matrix
docTermMatrix = []
for doc in documents:
    vector = [0] * len(vocabulary)
    words = doc[1].split()
    
    for word in words:
        if word in vocabulary:
            vector[vocabulary.index(word)] = 1
            
    docTermMatrix.append(vector)

# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> 
max_similarity = -1  
doc1_index = -1
doc2_index = -1

# Comparing each pair of documents
for i in range(len(docTermMatrix)):
    for j in range(i + 1, len(docTermMatrix)):
        # Calculating cosine similarity between documents i and j
        similarity = cosine_similarity([docTermMatrix[i]], [docTermMatrix[j]])[0][0]
        
        if similarity > max_similarity:
            max_similarity = similarity
            doc1_index = i
            doc2_index = j

# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> 
print(f"The most similar documents are document {documents[doc1_index][0]} and document {documents[doc2_index][0]} with cosine similarity = {max_similarity:.4f}")