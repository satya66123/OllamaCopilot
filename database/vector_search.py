import ast

from utils.embeddings import (
    create_embedding
)

from utils.similarity import (
    cosine_similarity
)

from database.vector_db import (
    get_all_chunks
)


def search_chunks(
        question,
        selected_document=None,
        top_k=5,
        user_id=0
):

    question_embedding = (
        create_embedding(question)
    )

    chunks = get_all_chunks(user_id)

    results = []

    for chunk in chunks:

        try:

            # chunk structure:
            # chunk[0] = id
            # chunk[1] = document_name
            # chunk[2] = chunk_text
            # chunk[3] = embedding

            document_name = chunk[1]

            if (
                selected_document
                and
                document_name != selected_document
            ):
                continue

            stored_embedding = (
                ast.literal_eval(
                    chunk[3]
                )
            )

            vector_score = cosine_similarity(
                question_embedding,
                stored_embedding
            )

            keyword_match = keyword_score(
                question,
                chunk[2]
            )

            hybrid_score = (
                    vector_score * 0.7
                    +
                    keyword_match * 0.3
            )

            results.append(
                (
                    hybrid_score,
                    chunk
                )
            )
            results.sort(
                reverse=True,
                key=lambda x: x[0]
            )

            top_chunks = results[:10]
            reranked = []

            for score, chunk1 in top_chunks:

                chunk_text = (
                    chunk1[2].lower()
                )

                question_text = (
                    question.lower()
                )

                bonus = 0

                for word in (
                        question_text.split()
                ):

                    if word in chunk_text:
                        bonus += 0.05

                final_score = (
                        score + bonus
                )

                reranked.append(
                    (
                        final_score,
                        chunk1
                    )
                )
                reranked.sort(
                    reverse=True,
                    key=lambda x: x[0]
                )

                return reranked[:top_k]

        except Exception:

            continue

    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return results[:top_k]


def keyword_score(
        query,
        text
):

    query_words = (
        query.lower().split()
    )

    text = text.lower()

    score = 0

    for word in query_words:

        if word in text:

            score += 1

    return score