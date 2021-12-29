# Assignment 9

### Hey, my name is Or Braf. Those are the main things I did in this assignment:
- I created a simple dictionary holding a list of six users, which are my family members.
- I created a template called 'assignment9.html' and linked it to 'base.html' and 'menu.html'. this template contains two forms: one is for searching a user (from the dictionary) by email address and the other is for registration & signing in.
- If the email address in the search form appears in the dictionary, the search result will be displayed. If it doesn't, the whole list of users will be displayed.
- Submitting the registration form will be followed by the greeting "Logged in, [name]". I created a global session variable so this message will appear at the menu in every page of the website. While a user is logged in, a logout button is shown in the menu - clicking on this button will end the session of the logged-in user and lead him to the registration form. 