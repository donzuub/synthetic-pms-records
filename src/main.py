from src.config import DB_CONFIG, BOT_IDS
from src.db.connection import create_connection
from src.db.query import fetch_and_process_data
from src.utils.guid import generate_guid
from src.utils.json_utils import write_json_file

def main():
    try:
        conn = create_connection(DB_CONFIG)
        for bot_id in BOT_IDS:
            patients = fetch_and_process_data(conn, bot_id)
            
            output_data = {
                "batchId": f"batch_{generate_guid()}",
                "patients": patients
            }
            
            output_file = f"{bot_id}_patients.json"
            write_json_file(output_data, output_file)
            print(f"Data for botid {bot_id} has been fetched, transformed, and written to {output_file}.")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    finally:
        if conn:
            conn.close()
    
    print("All data has been fetched, transformed, and written to respective files.")

if __name__ == "__main__":
    main()
