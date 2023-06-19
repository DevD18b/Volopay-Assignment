# API 

>## API Assignment for VOLO Pay

## Installation:

### Prerequisites
- Python [3.7.*]
- Django 
- Django REST framework 

### Steps
1. Clone the repository:
   ```shell
   git clone [repository URL]
   ```

2. Navigate to the project directory:
   ```shell
   cd project-directory
   ```

3. Create and activate a virtual environment:
   ```shell
   # Using virtualenv
   virtualenv env
   source env/bin/activate

   # Using venv (Python 3)
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the required dependencies:
   ```shell
   pip install django djangorestframework restframework
   ```

5. Set up the database:
   ```shell
   python manage.py migrate
   ```

6. Start the development server:
   ```shell
   python manage.py runserver
   ```

7. Access the API:
   ```
   http://localhost:8000/api/
   ```

## Inserting CSV Data
To insert the data from the provided CSV file into the SQLite3 database, a script named script.py is included in the project. Follow the steps below to run the script:

Make sure you have activated your virtual environment.

Place the CSV file containing the data in the project directory.

Open the script.py file and update the CSV_FILE_PATH variable with the correct path to your CSV file.

Run the script:


```
python script.py
```

The script will read the CSV file and insert the data into the SQLite3 database.

Note: Ensure that the CSV file has the correct structure and matches the fields expected by your Django models.

