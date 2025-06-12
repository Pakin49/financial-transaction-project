# Financial Transactions Dataset: Analytics 💳
This comprehensive financial dataset combines transaction records, customer information, and card data from a banking institution, spanning across the 2010s decade. The dataset is designed for multiple analytical purposes, including synthetic fraud detection, customer behavior analysis, and expense forecasting

Dataset Source : https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets?resource=download&select=transactions_data.csv

What we did was using Google Cloud Service with hadoop MapReduce to analyze the large amount of data and then uploaded the output to MongoDB

## Analyzed data ✨
### Transaction Summary by State/Country
This lists the number of states and countries involved in the transactions. Each line includes the amount of times, the total amount of money (in US dollars) and the average amount of money each country has involved in a transaction

#### [python_mapper_code](./mapper_city.py)
#### [python_reducer_code](./reducer.py)
#### [output](./outputs/output_part_city.txt)

### Transaction Summary by year (from 2010-2019)
This list the amount of transactions involved in each year, along with the total amount of money (in US dollars) and the average amount of money per year
#### [python_mapper_code](./mapper_year.py)
#### [python_reducer_code](./reducer.py)
#### [output](./outputs/output_part_year.txt)

## Database (MongoDB) 💖
Here is the file that we used to move the output file to MongoDB
#### [MongoDB_Midterm](./BigData_midterm_proj.ipynb)

## Members 🙆‍♀️
### Rapeepat Pokpattanakul 6480358
### Mark Kittiphat Kuprasertwong 6481322
### Pakin Panawattanakul 6580043
### Nitchayanin Thamkunaon 6580081
