import ast

from utils.embeddings import (
    create_embedding
)

from utils.similarity import (
    cosine_similarity
)

from utils.bm25_search import (
    get_bm25_scores
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

    chunks = get_all_chunks(
        user_id
    )

    if not chunks:
        return []

    bm25_scores = (
        get_bm25_scores(
            question,
            chunks
        )
    )

    max_bm25 = max(
        bm25_scores
    ) if len(
        bm25_scores
    ) > 0 else 1

    results = []

    for i, chunk in enumerate(
            chunks
    ):

        try:

            document_name = (
                chunk[1]
            )

            if (
                selected_document
                and
                document_name
                !=
                selected_document
            ):
                continue

            stored_embedding = (
                ast.literal_eval(
                    chunk[3]
                )
            )

            vector_score = (
                cosine_similarity(
                    question_embedding,
                    stored_embedding
                )
            )

            bm25_score = (
                bm25_scores[i]
            )

            normalized_bm25 = (
                bm25_score
                /
                max_bm25
            ) if max_bm25 > 0 else 0

            hybrid_score = (
                (
                    vector_score
                    * 0.7
                )
                +
                (
                    normalized_bm25
                    * 0.3
                )
            )

            results.append(
                (
                    hybrid_score,
                    chunk
                )
            )

        except Exception:

            continue

    results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    top_chunks = (
        results[:10]
    )

    reranked = []

    for score, chunk in (
            top_chunks
    ):

        chunk_text = (
            chunk[2]
            .lower()
        )

        bonus = 0

        for word in (
                question
                .lower()
                .split()
        ):

            if word in chunk_text:

                bonus += 0.05

        final_score = (
            score
            +
            bonus
        )

        reranked.append(
            (
                final_score,
                chunk
            )
        )

    reranked.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return reranked[
           :top_k
           ]