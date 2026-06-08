from database.db import get_connection


def save_chunk(
        document_name,
        chunk_text,
        embedding
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO document_chunks(
        document_name,
        chunk_text,
        embedding
    )
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            document_name,
            chunk_text,
            str(embedding)
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

def get_documents():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT DISTINCT document_name
    FROM document_chunks
    ORDER BY document_name
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows
def get_document_count():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(
        DISTINCT document_name
    )
    FROM document_chunks
    """)

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

def get_all_chunks():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT
        id,
        document_name,
        chunk_text,
        embedding
    FROM document_chunks
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows