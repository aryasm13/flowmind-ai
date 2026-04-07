def preprocess_input(text):
    text = text.strip()

    # normalize
    text = text.replace("\n", " ")

    # split into chunks (sentence-based)
    sentences = text.split(". ")

    # clean + filter
    chunks = []
    for s in sentences:
        s = s.strip()
        if len(s) > 10:
            chunks.append(s)

    # limit chunks (safety)
    return chunks[:20]