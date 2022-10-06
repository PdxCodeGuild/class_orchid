# Dirty Wordy
## Project Overview

The app I've choosen to create is a vocabulary study app.
The will give the user to ability to search words and obtain definitions for that specific word. They will have the option to continue search or add word to their favorites list. The second feature is when a word is added to their favorite word list, the can go to the study tab and they can use the automated study cards to train on words and definitions. The third and final feature will be the quiz tab were the you can take a small quiz on the the words in your favorites list by mixing up multiple different definitions and having you pick the correct one. The user will be directed to a page with how many they scored corectly and the words they need to study more. I have Decide to use Django as my base foundation for my app, and i will be using Javscript to consume my api, and Html, Css, and Bootstrap for the front end of my project.


# Data Model

User Model
- Registration
- Login
- Logout

Quiz Model
- Randomize definitions and words
- result page with how many are wrong and right

Flashcard Model
- Saves favorites words and makes a study system

Word Model
- user inputs word
- definitions comes back
- can save the favorites list



<!-- 
The data that will be stored are The Words and definitions of those words. I'll be using the DictionaryApi (https://dictionaryapi.dev/). I will have 2 different lists. One to store the words and definitions in the favorites list and one to to store random definitions to quiz the user. https://api.dictionaryapi.dev/api/v2/entries/en/<word>. Also a user login/registion will be used to hold the users username/Password. when logged in with their cridentials, they will have access to their lists, quizzes, and flashcards. -->


# Schedule

### Week 1: 
The first week i will build the basic layout of the webpages and make sure everything is routed properly. I will also implement the login/logout and registion pages. I will also get the first feature which is the word search working properly.

### Week 2:
The second week I will focus on the making the flashcards for the studying part of the app and the quiz. I will be using Bootstrap to make the flashcards. I will try to make the quizzes by importing random into my project.

### Week 3:
For my final week, I will be finishing any final touch ups to my features. This week i will also be doing CSS and making to app look more professional.
