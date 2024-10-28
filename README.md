# SQL-Python-R5

## Overview
This project its an assesment that demonstrates the integration of SQL and Python for data manipulation and analysis. It includes exercises involving creating lists and dictionaries in Python, transforming JSON files into structured DataFrames, and performing SQL queries on a PostgreSQL database.

## Repository
Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/ImBetterThanYesterday/sql-python-r5.git
```
## Setup
### 1. Create a Virtual Environment Navigate to the project directory and create a virtual environment:

``` bash
cd sql-python-r5
python -m venv venv
``` 

### 2. Activate the Virtual Environment

On Windows:

``` bash
./venv/Scripts/activate
``` 
On macOS/Linux:

``` bash
source venv/bin/activate
``` 
### 3. Install Required Packages Install the required Python packages using:
``` bash
pip install -r requirements.txt
``` 
# Python Section

## Part 1: List to Dictionary Transformation
In this section, we perform the following tasks:

### 1. Create a List of Numbers Create a list containing 10 elements:

### 2. Create a Dictionary Create a dictionary where the key is the number from the list, and the value is the number multiplied by 2. Example:
 - Input List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
 - Output Dictionary:
    ```bash
    {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
    ``` 

``` bash
pip install -r requirements.txt
``` 

### Running the Script
Open a terminal, ensure you are in the project directory, and run the following commands:
```bash
pwd  # Display current directory
ls   # List files in the current directory
python list_To_Dict.py  # Run the script
```
## Part 2: JSON File Transformation
Read a JSON file and perform the necessary transformations to organize the columns in a DataFrame. Output the resulting DataFrame as a CSV file.

### Database Connection Testing
To test the connection to the database, run:
``` bash
python test_Db_Connection.py
``` 
### Uploading CSV to PostgreSQL
To upload the resulting CSV file to a PostgreSQL database, execute:
``` bash
python upload_Csv_Files_To_Database.py
``` 
### Running SQL Queries
To upload the resulting CSV file to a PostgreSQL database, execute:
``` bash
python sql_Questions.py
``` 
## Sample Queries
### 1.Name of the Longest Song
``` bash
SELECT track_name, duration_ms
FROM dataset
ORDER BY duration_ms DESC
LIMIT 1;
``` 
### 2. Most Popular Song per Album In case there are two songs with the same popularity, the one with the shorter duration is selected:
``` bash
WITH ranked_songs AS (
    SELECT 
        album_id, 
        track_name, 
        track_popularity, 
        duration_ms,
        ROW_NUMBER() OVER (
            PARTITION BY album_id 
            ORDER BY track_popularity DESC, duration_ms ASC
        ) AS rank
    FROM dataset
)
SELECT album_id, track_name, track_popularity, duration_ms
FROM ranked_songs
WHERE rank = 1
ORDER BY track_popularity DESC;
``` 
