import mysql.connector
import bcrypt

user_id=0
def get_connection():

    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="ollamacopilot"
    )


def save_chat(title, content, messages_json,user_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO chats(
        title,
        content,
        messages_json,
        user_id
    )
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            title,
            content,
            messages_json,
            user_id
        )
    )

    conn.commit()

    inserted_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return inserted_id

def get_all_chats(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT id,title,created_at
    FROM chats
    WHERE title NOT LIKE 'RAG - %'
    AND user_id=%s
    ORDER BY id DESC
    """

    cursor.execute(
        query,
        (user_id,)
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def get_all_rag_chats(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT id,title,created_at
    FROM chats
    WHERE title  LIKE 'RAG - %' AND user_id=%s
    ORDER BY id DESC
    """

    cursor.execute(
        query,
        (user_id,)
    )

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


def delete_chat(chat_id, user_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    DELETE FROM chats
    WHERE id=%s AND user_id=%s
    """

    cursor.execute(query, (chat_id,user_id,))

    conn.commit()

    cursor.close()
    conn.close()


def update_chat(
        chat_id,
        title,
        content,
        messages_json,
        user_id
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    UPDATE chats
    SET title=%s,
        content=%s,
        messages_json=%s,
        user_id=%s
    WHERE id=%s
    """


    cursor.execute(
        query,
        (
            title,
            content,
            messages_json,
            user_id,
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

def get_total_chats(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM chats
        WHERE user_id=%s
        """,
        (user_id,)
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

def get_max_chat_id():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT MAX(id)
    FROM chats
    """

    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result and result[0]:
        return result[0]

    return 0

def get_latest_chat():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT id,title
    FROM chats
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return row

def get_rag_chats(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT
        id,
        title
    FROM chats
    WHERE title LIKE 'RAG - %' AND user_id=%s
    ORDER BY id DESC
    """

    cursor.execute(query,(user_id,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def get_chat_titles(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT id,title
    FROM chats
    WHERE title NOT LIKE 'RAG - %' AND user_id= %s
    ORDER BY id DESC
    """

    cursor.execute(query,(user_id,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def search_chats(keyword,user_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT
        id,
        title
    FROM chats
    WHERE title LIKE %s AND user_id=%s
    ORDER BY id DESC
    """

    cursor.execute(
        query,
        (f"%{keyword}%",user_id,)
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def create_user(
        username,
        password
):

    hashed_password = (
        bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )
    )

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users(
            username,
            password
        )
        VALUES(%s,%s)
        """,
        (
            username,
            hashed_password.decode()
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

def login_user(
        username,
        password
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=%s
        """,
        (username,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return None

    stored_hash = (
        user[2]
    )

    if bcrypt.checkpw(
        password.encode(),
        stored_hash.encode()
    ):

        return user

    return None

def get_total_users():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM users
        """
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

def get_all_users():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            username,
            role
        FROM users
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def get_total_chats_admin():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM chats
        """
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count
