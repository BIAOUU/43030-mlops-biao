import pandas as pd
import sqlite3

# Simulate Data Processing Pipeline
def process_data():
    # 1. Load data via Pandas
    df = pd.DataFrame({'user_id': [1, 2], 'query': ['What is RAG?', 'Azure setup']})

    # 2. SQL integration
    conn = sqlite3.connect(':memory:')
    df.to_sql('logs', conn, index=False)

    # 3. Query using SQL
    result = pd.read_sql('SELECT * FROM logs WHERE user_id = 1', conn)
    print("Pipeline executed successfully.")
    return result
