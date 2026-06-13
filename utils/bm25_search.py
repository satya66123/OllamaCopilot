from rank_bm25 import BM25Okapi


def get_bm25_scores(
        query,
        chunks
):

    corpus = []

    for chunk in chunks:

        corpus.append(
            chunk[2].lower().split()
        )

    bm25 = BM25Okapi(
        corpus
    )

    return bm25.get_scores(
        query.lower().split()
    )