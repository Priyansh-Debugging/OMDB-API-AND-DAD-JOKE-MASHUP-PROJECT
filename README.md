# OMDB API AND icanhazdadjokes API 🧠
Coursera project on mashing two different API's to  
create a fun readup message for the user.

# Skills used 🔧
- Python
- Functions, API's, etc.
- API documentaion reading

# ABOUT✏️
In this project we take data from two API's.  
One is popular API [OMDB](https://www.omdbapi.com) which has detailed data about popular movies.  
Another is [icanhazdadzokes](https://icanhazdadjoke.com) created by Dr. Chuck. This has vast amount  
of data regarding dad jokes.

# OMDB API 📽️
Following are the set of data available on this API about many famous movies:-  
- Movie PLOT description
- Lastest poster of movies
- Ratings from different sources like:
- Rotten Tomatoes Score
- IMDB Score
- and much more...

# ICANHAZDADJOKES 🤣
Following are the data available:-
- Many dad jokes.
- Option to search jokes with specific words.
- and much more...

# WORKING📈
Here are the functions created in this code and there functionality:-  
- **highlight** == This function takes a word and the sentence to highlight that word (For EX. ** forward **).
- **get_movie_data** == This function takes data about the movie from api and turns the json into redable dictionary format.
- **get_joke_data** == This function takes data about the joke, searched by a specifi word.
- **get_jokes** == This function takes the data from above function and only send the required data.
- **rt_rating** == This function returns the rotten tomatoes data of the input movies.
- **haha_me** == This function returns a fun string readble by the user using all the data from above functions.
  
# ADDITIONAL FILES📁:
- **permanent_cache.txt** == Stores all the permanent cache.
- **requests_with_caching** == It is a smaller verson of request library with only functions related to this project.
- **this_page_cache.txt** == It stores all the temproary cache.
