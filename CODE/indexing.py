import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import defaultdict
import csv
import string

def preprocess_review(review):
    
    tokens = word_tokenize(review)
    
    tokens = [word.lower() for word in tokens if word.isalpha()]
    
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    return tokens

file_path = 'amazon_reviews_us_Mobile_Electronics_v1_00.tsv'
df = pd.read_csv(file_path, sep='\t', on_bad_lines='skip')
term_document_index = {}

for index, row in df.iterrows():
    p_id = row['product_id']
    p_title = row['product_title']
    r_body = row['review_body']
    visited = []
    if (pd.isna(p_title)):
        continue
    print(p_id)
    # tokens = preprocess_review(p_title)
    if p_id in visited:
        term_document_index[(p_id, p_title)].append(r_body)
    else:
        term_document_index[(p_id, p_title)] = [r_body]
# inverted indexing #
    # for term in tokens:
    #     if p_id not in term_document_index[term]:
    #         term_document_index[term].append(p_id)

# output_file = 'product_inverted_indexing.csv'
# for j in term_document_index.values():
#     print(len(j))
# with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Term', 'PRODUCT_IDs']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()

#     for term, doc_ids in term_document_index.items():
#         writer.writerow({'Term': term, 'PRODUCT_IDs': ', '.join(map(str, doc_ids))})

# product review mapping #
output_file = 'product_review_mapping.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Product_ID', 'Product_title' ,'review']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for term, review in term_document_index.items():
        review = [str(f) for f in review]
        cleaned_strings = [s.replace('<br />', '') for s in review]
        if term[1]=='Amazon Kindle Voyage Case, [Book Case Carve] GMYLE Premium PU leather Book style Flip Folio Stand Case Cover for Kindle Voyage - Brown':
            print(cleaned_strings)
        writer.writerow({'Product_ID': term[0],'Product_title': term[1], 'review': '. '.join(map(str, cleaned_strings))})
    
    
print("done!")