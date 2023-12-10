import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import defaultdict
import nltk
import math
import os
from nltk.sentiment import SentimentIntensityAnalyzer

# uncomment the next line if you havent installed punkt from nltk
# nltk.download('punkt')

cwd = os.getcwd()

def sentiment_analysis(name):
    window = tk.Toplevel(root, bg='lightblue')
    temp = df2[df2['Product_title'] == name]
    string = temp['review'].tolist()
    arr = string[0].split('.')

    sia = SentimentIntensityAnalyzer()

    polarized_reviews = {'Positive': [], 'Neutral': [], 'Negative': []}

    for i in arr:
        sentiment_score = sia.polarity_scores(i)['compound']
        if sentiment_score >= 0.35:
            polarized_reviews['Positive'].append(i)
        elif -0.35 < sentiment_score < 0.35:
            polarized_reviews['Neutral'].append(i)
        else:
            polarized_reviews['Negative'].append(i)

    # Set a fixed height for each row
    window.rowconfigure(0, minsize=120)
    window.rowconfigure(2, minsize=720)

    pane1 = tk.Frame(window, bg='lightgreen', width=450, height=50)
    pane1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    label_pos = tk.Label(pane1, text='POSITIVE REVIEWS', fg='black', bg='lightgreen', font=("Arial", 14, "bold"))
    label_pos.pack()

    pane2 = tk.Frame(window, bg='yellow', width=450, height=50)
    pane2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    label_neu = tk.Label(pane2, text='NEUTRAL REVIEWS', fg='black', bg='yellow', font=("Arial", 14, "bold"))
    label_neu.pack()

    pane3 = tk.Frame(window, bg='red', width=450, height=50)
    pane3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
    label_neg = tk.Label(pane3, text='NEGATIVE REVIEWS', fg='black', bg='red', font=("Arial", 14, "bold"))
    label_neg.pack()

    pane4 = tk.Frame(window, bg='lightgreen', width=450, height=700)
    pane4.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    pane5 = tk.Frame(window, bg='yellow', width=450, height=700)
    pane5.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    pane6 = tk.Frame(window, bg='red', width=450, height=700)
    pane6.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

    all_review_labels = []
    for i, j in polarized_reviews.items():

        if (i == 'Positive'):
            curr_pane = pane4
            color = 'lightgreen'
        elif (i == 'Neutral'):
            curr_pane = pane5
            color = 'yellow'
        else:
            curr_pane = pane6
            color = 'red'
        for k in j:
            temp_label = tk.Label(curr_pane, text=k + '\n', wraplength=400, bg=color)
            temp_label.pack()
            all_review_labels.append(temp_label)

        
def fetchProducts():
    global df1
    global df2
    
    product_inverted_indexing = str(cwd) +'/product_inverted_indexing.csv'
    product_review_mapping = str(cwd) + '/product_review_mapping.csv'
    df1 = pd.read_csv(product_inverted_indexing)
    df2 = pd.read_csv(product_review_mapping)
    
    search_query = query.get()
    
    tokens = word_tokenize(search_query)
    tokens = [word.lower() for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]

    p_id_lists = []
    for i in tokens:
        term_column = df1.iloc[:, 0] 
        filtered_rows = df1.loc[df1.iloc[:, 0] == i].iloc[:, 1].tolist()
        filtered_rows = filtered_rows[0].split(', ')
        p_id_lists.extend(tuple(filtered_rows))

    # if p_id_lists:
    #     intersection = list(set.intersection(*p_id_lists))
    #     print(intersection)
    # else:
    #     print("No results found.")
    
    dictt = {}
    for i in p_id_lists:
        if i in dictt.keys():
            dictt[i] += 1
        else:
            dictt[i] = 1
            
    for i,j in dictt.items():
        log_tf= 1 + math.log2(j)
        dictt[i] = log_tf
    
    dictt = dict(sorted(dictt.items(), key=lambda item: item[1], reverse=True))
    keys = list(dictt.keys())
    intersection = keys
    
    result_label = tk.Label(root, text=f"Search Results for {search_query}")
    result_label.config(font=('Arial', 14,'bold'), bg='lightblue')
    result_label.pack(pady=20)

    product_labels = []
    for i in intersection:
        if len(product_labels) < 20:
            temp_arr = df2[df2['Product_ID'] == i]['Product_title'].tolist()
            product_label = tk.Label(frame, text=temp_arr[0]+'\n' )
            product_label.bind("<Button-1>", lambda event, name=temp_arr[0]: sentiment_analysis(name))
            product_label.config(bg='lightblue', font=('Arial', 11), cursor='hand2', anchor=tk.W)
            product_label.pack(anchor='w', padx=30)
            product_labels.append(product_label)

    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

    canvas.pack(side='left', expand=True, fill='both')
    
    

root = tk.Tk()
root.title("Search Window")

label1 = tk.Label(root, text="EXTRACTIVE POLARIZED SUMMARIZATION")
label1.config(font=("Arial", 22, 'bold'), bg='lightblue') 
label1.pack(pady = 20)

label3 = tk.Label(root, text="- E RITHICK")
label3.config(font=("Arial", 16, 'bold' ), bg='lightblue', fg='purple') 
label3.pack()

label2 = tk.Label(root, text="SEARCH FOR A PRODUCT")
label2.config(font=("Arial", 14, ), bg='lightblue') 
label2.pack(pady=20)


query = tk.Entry(root)
entry_style = {'foreground': 'black', 'background': 'white', 'font': ('Arial', 12), 'width':'50'}
query.config(**entry_style)
query.pack(pady=10)


search_button = tk.Button(root, text="Search", command=fetchProducts)
button_style = {'background': 'black', 'foreground':'white', 'width': '20', 'font':('Arial', 10, 'bold')}
search_button.config(**button_style)
search_button.pack(pady=20)

canvas = tk.Canvas(root, bg='lightblue', width=400, height=300, scrollregion=(0, 0, 0, 500))

frame = tk.Frame(canvas, bg='lightblue')

canvas.create_window((0, 0), window=frame, anchor='nw')

scrollbar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

canvas.config(yscrollcommand=scrollbar.set)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (1300 // 2)
y = (screen_height // 2) - (700 // 2)

root.geometry(f'{1300}x{640}+{x}+{y}')

root.configure(bg='lightblue')

root.mainloop()