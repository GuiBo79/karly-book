import pandas as pd
import subprocess
import os
from sqlalchemy import create_engine, text
from db_utils import create_table_from_df
from sql_queries import SUMMARY_INCIDENTS, INCIDENTS_DETAILS

def main():
    """
    Main function to execute the application.
    - Downloads a CSV file from a specified URL.
    - Reads the CSV into a pandas DataFrame.
    - Creates a table in MySQL database using DataFrame schema.
    - Inserts data from DataFrame into the MySQL table.
    """
    db_user = 'user'
    db_password = 'password'
    db_host = 'db'
    db_port = '3306'
    db_name = 'fire_incidents'
    views = [SUMMARY_INCIDENTS, INCIDENTS_DETAILS]

    engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    csv_file = 'data/fire_incidents.csv'
    url = 'https://data.sfgov.org/resource/wr8u-xric.csv'

    if not os.path.exists('data'):
        os.makedirs('data')

    subprocess.run(f"curl -o {csv_file} {url}", shell=True, check=True)

    df = pd.read_csv(csv_file)

    create_table_from_df(df, engine, 'fire_incidents_data')

    df.to_sql('fire_incidents_data', con=engine, if_exists='replace', index=False)

    for view in views:
        with engine.connect() as connection:
            connection.execute(text(view))
    print("############################################")
    print("# Go to phpAdmin at: http://localhost:8080 #")
    print("############################################")

if __name__ == "__main__":
    main()
