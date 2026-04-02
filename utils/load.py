from utils.db import get_connection

def load_to_mysql(jobs):

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO raw_jobs (company, title, location, link, source)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.executemany(query, jobs)
        conn.commit()

        print("Data inserted into MySQL")

    except Exception as e:
        print("Database Error:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()