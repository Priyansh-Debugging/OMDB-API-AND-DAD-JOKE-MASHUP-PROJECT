import requests_with_caching
import json

def highlight(word: str, sentence: str) -> str:
    """
    Highlights a specific word in a sentence by surrounding it with asterisks (**).
    The highlighting is case-insensitive.

    Args:
        word (str): The word to be highlighted.
        sentence (str): The sentence in which the word should be highlighted.

    Returns:
        str: The sentence with the specified word highlighted.
    """
    import re

    # Escape special characters in the word to treat it as a literal string
    # Use re.sub() to replace the word with the highlighted version
    # Use re.IGNORECASE flag to perform case-insensitive replacement
    return re.sub(re.escape(word), f"**{word}**", sentence, flags=re.IGNORECASE)


def get_movie_data(name):
    resp = requests_with_caching.get(
        "http://www.omdbapi.com/",
        params={"apikey": "[abcd1234]", "r": "json", "t": name},
    )
    data = resp.json()

    if "Title" not in data:
        return f"No movie found: {name}"

    return data


def get_joke_data(term):
    url = "https://icanhazdadjoke.com/search"
    params = {"term": term, "limit": 2}
    headers = {"Accept": "application/json"}

    resp = requests_with_caching.get(url, params=params, headers=headers)
    return resp.json()


# longest first + alphabetical tie break
def sort_words(words):
    return sorted(words, key=lambda w: (-len(w), w.lower()))


def get_jokes(plot: str, verbosity=0):
    words = [w.strip(",.!;:") for w in plot.split()]
    words_sorted = sort_words(words)

    for word in words_sorted:
        if not word:
            continue

        joke_data = get_joke_data(word)

        if joke_data["total_jokes"] > 0:
            jokes = [j["joke"] for j in joke_data["results"]]
            return word, jokes

    return None, None


def rt_rating(movie_dict):
    for item in movie_dict["Ratings"]:
        if item["Source"] == "Rotten Tomatoes":
            return int(item["Value"].replace("%", ""))
    return -1

def haha_me(movie_title: str, verbosity=0) -> str:
    movie_data = get_movie_data(movie_title)

    if isinstance(movie_data, str):
        return movie_data

    keyword, jokes = get_jokes(movie_data["Plot"])

    if keyword is None:
        return "I've got no jokes about this movie. It's too serious!"

    rating = rt_rating(movie_data)

    if rating == -1:
        comment = "Hope you like them!"
    elif rating < 70:
        comment = "Hope they're better than the movie!"
    else:
        comment = "Hope they're as good as the movie!"

    jokes_text = "\n".join(jokes)
    xyz = highlight(keyword,jokes_text)
    x = (
        f"{movie_data['Title']}\n"
        f"Rotten Tomatoes rating: {rating}%\n"
        f"{highlight(keyword, movie_data['Plot'])}\n"
        f"Speaking of **{keyword}**, that reminds me of some jokes.\n"
        f"{comment}\n\n"
        f"{xyz}"
    )
    return str(x)

    
haha_me("Black Panther")
