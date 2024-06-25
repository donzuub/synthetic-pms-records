from src.transform.query_transform import transform_query_result
from src.transform.data_transform import transform_data

def fetch_and_process_data(conn, bot_id):
    query = """
    SELECT result
    FROM main
    WHERE status = 'Succeeded' AND botid = %s;
    """
    
    patients = []
    try:
        cursor = conn.cursor()
        cursor.execute(query, (bot_id,))
        rows = cursor.fetchall()
        for row in rows:
            if len(row) == 1:  # Ensure there is exactly one column in the result
                result_data = transform_query_result(row)
                if result_data:
                    patient_data = transform_data(result_data)
                    patients.append(patient_data)
            else:
                print(f"Unexpected number of columns in row: {row}")
        cursor.close()
    except Exception as e:
        print(f"Error fetching data for botid {bot_id}: {e}")
    
    return patients
