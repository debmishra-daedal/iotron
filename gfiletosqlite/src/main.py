import uvicorn
from gfiletosqlite import download_file_from_gdrive, csv_to_sqlite, create_api
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware

# Configuration
DRIVE_FILE_ID = "1D3DS-b6-SD9gutfGsct1ueiEG3x76c5i"  # Replace with your file ID
CSV_FILE = "debmishra-emergency-contacts.csv"
DB_FILE = "data.db"
TABLE_NAME = "emergency_contacts"  # Replace with your desired table name

if __name__ == "__main__":
    # Option 2: Process directly without saving file
    csv_content = download_file_from_gdrive(DRIVE_FILE_ID)
    columns = csv_to_sqlite(csv_content, DB_FILE, TABLE_NAME)
    app = create_api(DB_FILE, TABLE_NAME)

    # Add CORS middleware to allow requests from the frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8080"],  # Frontend origin
        allow_credentials=True,
        allow_methods=["*"],  # Allow all HTTP methods
        allow_headers=["*"],  # Allow all headers
    )

    # Start the API server
    uvicorn.run(app, host="0.0.0.0", port=8000)
