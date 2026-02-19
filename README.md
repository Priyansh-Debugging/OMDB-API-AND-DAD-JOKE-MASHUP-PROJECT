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

# 

# WORKING📈
- We create two functions get_pos and get_neg to get no. of positive/negative words respectively.
- In these functions we take each word at a time and remove any punctuations in the word using a  
  list of punctuation chracters.
- We also then check if the word is positive or negative by matching the words in given text files
  and returning back the result
- At last we compose all the necceasy data into the resulting_data.csv and plot the scatter plot.
