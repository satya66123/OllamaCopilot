def rrf_score(
        rank,
        k=60
):

    return 1 / (
        k + rank
    )