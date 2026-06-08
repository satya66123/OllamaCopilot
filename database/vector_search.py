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
        top_k=5
):

    question_embedding = (
        create_embedding(question)
    )

    chunks = get_all_chunks()

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

            similarity = (
                cosine_similarity(
                    question_embedding,
                    stored_embedding
                )
            )

            results.append(
                (
                    similarity,
                    chunk
                )
            )

        except Exception:

            continue

    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return results[:top_k]