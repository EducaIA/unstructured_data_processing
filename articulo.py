#title starts with articulo.

# Open the input file
with open('input.txt', 'r', encoding='utf-8') as f:

    # Initialize variables
    article = {}
    articles = []
    content = []

    # Loop over each line in the file
    for line in f:

        # Strip any leading/trailing whitespace
        line = line.strip()

        # If the line starts with 'Artículo', we've found a new article
        if line.startswith('Artículo'):
            # Extract the article number
            try:
                article_number = int(line.split()[1].strip('.-'))
            except (IndexError, ValueError):
                continue

            # Save the previous article (if there was one)
            if article:
                article['content'] = '\n'.join(content)
                articles.append(article)

            # Start a new article
            article = { 'ArtículoNumber': article_number, 'ArtículoHeader': line, 'content': ''}
            content = []

        # If we're inside an article, add the line to its content
        elif article:
            content.append(line)

    # Add the last article (if there was one)
    if article:
        article['content'] = '\n'.join(content)
        articles.append(article)

# Write the output file
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False)
