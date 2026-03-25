def preprocess_input(text):
    # Clean text
    text = text.strip()

    # Remove unnecessary line breaks
    text = text.replace("\n", " ")

    # Basic filtering (can expand later)
    if len(text) > 2000:
        text = text[:2000]

    return text