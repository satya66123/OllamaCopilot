from database.db import get_connection


user_id=0

def save_chunk(
        document_name,
        chunk_text,
        embedding,
        user_id
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO document_chunks(
        document_name,
        chunk_text,
        embedding,
        user_id
    )
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            document_name,
            chunk_text,
            str(embedding),
            user_id
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

def get_documents(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT DISTINCT document_name
    FROM document_chunks
    WHERE user_id=%s
    ORDER BY document_name
    """

    cursor.execute(
        query,
        (user_id,)
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows
def get_document_count(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT COUNT(
        DISTINCT document_name
    )
    FROM document_chunks
    WHERE user_id=%s
    """

    cursor.execute(
        query,
        (user_id,)
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

def get_all_chunks(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT
        id,
        document_name,
        chunk_text,
        embedding
    FROM document_chunks
    WHERE user_id=%s
    """

    cursor.execute(
        query,
        (user_id,)
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def delete_document(
        document_name,
        user_id
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    DELETE
    FROM document_chunks
    WHERE document_name=%s
    AND user_id=%s
    """

    cursor.execute(
        query,
        (
            document_name,
            user_id
        )
    )

    conn.commit()

    cursor.close()
    conn.close()
def get_document_count_admin():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(
            DISTINCT document_name
        )
        FROM document_chunks
        """
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count