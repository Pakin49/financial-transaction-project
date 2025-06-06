# Financial Transactions Dataset: Analytics 💳
This comprehensive financial dataset combines transaction records, customer information, and card data from a banking institution, spanning across the 2010s decade. The dataset is designed for multiple analytical purposes, including synthetic fraud detection, customer behavior analysis, and expense forecasting

Dataset Source : https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets?resource=download&select=transactions_data.csv

What we did was using Google Cloud Service along with hadoop MapReduce to analyze the large amount of data 

## Analyzed data ✨
### mapper_city
The count of each state and country involved in the transactions 
#### [python_code](./mapper_city.py)
#### [output](./outputs/output_part-city.txt)

### mapper_year
The count of transactions involved in each year 
#### [python_code](./mapper_year.py)
#### [output](./outputs/output_part-year.txt)

## Fraud Detection Dataset 🔍
Dataset Source : https://www.kaggle.com/datasets/aryan208/financial-transactions-dataset-for-fraud-detection?resource=download

### [Fraud Detection](./Fraud%20Detection/)
for fraud detection data 