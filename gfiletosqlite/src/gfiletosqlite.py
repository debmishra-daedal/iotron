import pandas as pd
import sqlite3
import requests
import io
from fastapi import FastAPI


# Step 1: Download CSV from Google Drive (public link)
def download_file_from_gdrive(file_id, destination=None):
    """Download a file from Google Drive using direct link (for public files)."""
    # Direct download link format
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    # For larger files that might trigger warning page
    session = requests.Session()
    response = session.get(url, stream=True)

    if destination:
        # Save to file
        with open(destination, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return destination
    else:
        # Return content directly
        return io.StringIO(response.content.decode("utf-8"))


# Step 2: Read CSV and load to SQLite
def csv_to_sqlite(csv_content, db_file, table_name):
    """Read CSV and load to SQLite database."""
    # Read CSV file
    if isinstance(csv_content, str):  # If it's a file path
        df = pd.read_csv(csv_content)
    else:  # If it's already a file-like object
        df = pd.read_csv(csv_content)
    df["id"] = df.index

    # Connect to SQLite database
    conn = sqlite3.connect(db_file)

    # Write to SQLite
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Data loaded to SQLite table '{table_name}'")

    # Close connection
    conn.close()
    return df.columns.tolist()


# Step 3: Create FastAPI app to serve the data
def create_api(DB_FILE, TABLE_NAME):
    app = FastAPI()

    @app.get("/emergency-contacts")
    def root():
        return {"message": "Emergency contacts API is running"}

    @app.get("/emergency-contacts/data")
    def get_all_data():
        """Get all records from the database."""
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        data = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return data

    @app.get("/emergency-contacts/data/{record_id}")
    def get_record(record_id: int):
        """Get a specific record by ID."""
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = ?", (record_id,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return dict(result)
        return {"error": "Record not found"}

    return app
