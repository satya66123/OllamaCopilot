import mysql.connector


def get_connection():

    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="ollamacopilot"
    )


def save_chat(title, content, messages_json):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO chats(
        title,
        content,
        messages_json
    )
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            title,
            content,
            messages_json
        )
    )

    conn.commit()

    inserted_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return inserted_id

def get_all_chats():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT id,title,created_at
    FROM chats
    ORDER BY id DESC
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def get_chat_by_id(chat_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT *
    FROM chats
    WHERE id=%s
    """

    cursor.execute(query, (chat_id,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return row


def delete_chat(chat_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    DELETE FROM chats
    WHERE id=%s
    """

    cursor.execute(query, (chat_id,))

    conn.commit()

    cursor.close()
    conn.close()


def update_chat(
        chat_id,
        title,
        content,
        messages_json
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    UPDATE chats
    SET title=%s,
        content=%s,
        messages_json=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (
            title,
            content,
            messages_json,
            chat_id
        )
    )

    conn.commit()

    print(
        "Rows Updated:",
        cursor.rowcount
    )

    cursor.close()
    conn.close()


def get_chat_titles():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT id,title
    FROM chats
    ORDER BY id DESC
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows