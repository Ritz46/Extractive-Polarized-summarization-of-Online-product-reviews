POLARIZED SUMMARIZATION OF ONILNE PRODUCT REVIEWS

This project aims to develop a Extractive Polarized Summarization System for Online Product Reviews, leveraging information retrieval (IR) techniques to provide concise and insightful summaries.


------------DRIVE LINK TO ALL CSVs-----------

https://drive.google.com/drive/folders/16QA45fA4UGf6R-xkryTsMZzcWWCaAWGk?usp=sharing



------------COMPONENTS-------------------

P37-MiniProject-ERITZ/
    CODE/
        indexing.py
        main.py
        amazon_reviews_us_Mobile_Electronics_v1_00.tsv
        product_inverted_indexing.csv
        product_review_mapping.csv
    README.txt
    ProjDesc.pdf



------------IMPORTANT NOTE------------

YOU MAY NOT NEED TO RUN "indexing.py" SINCE THE ALDREADY INDEXED FILE IS AVAILABLE IN THE DRIVE FOLDER.
UNCOMMENT 'nltk.download('punkt')' in main.py if you dont have it.
MAKE SURE THE DATASETS ARE IN THE RIGHT FOLDER AND THE CODE IS BEING RUN USING CMD

ONLY USE CMD TO RUN !


------------STEPS TO RUN THE CODE----------

1. First, download all three CSV/TSV(from drive link) into the /CODE folder. (DATASET, IVERTED-INDEXING, AND THE MAPPING)
2. OPEN CMD !!!
3. Make sure that all libraries are installed. if not run "pip install -r requirements.txt" in the /CODE directory
4. Go to the /CODE directory and type "Python main.py"
5. A window will pop-up
6. Search for any product name that is available in the dataset (EX - 'amazon kindle case')
7. Click on any of the listed products 
8. Now, you may see the polarized reviews of that respective product



------------PROJECT BY-----------------

E RITHICK
S20210010072


------------THANK YOU !!!-------------