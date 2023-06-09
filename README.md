# Immo_step_4


## Description
In this step of the Immo Eliza project, my task was to deploy my regression model made in the previous step using API, Render and Docker.<br>

## Installation DIY
- Clone the git repository.
- Import all teh components from the file "requirements.txt".
- Run the app.py with the command "uvicorn app:app"
- Check Fast api localhost

## Usage
This script is used to predict a price based on different characteristics of a property.
In this case, we are using "Furnished, Equipped-kitchen, area, property type". <br>

## Issues Faced
- Getting familiar with Fast API and testing the POST method input, I thought my code was wrong so I spent a lot of time trying to debug something that was working just fine. The issue was my tests, my input into a JSON file was wrongly typed.
- Importing the model, same issue, lot of time wasted to fix something that was in reality a "/" too much in the path.

## Known issues
- Properties appear to have negative numbers for apartments, they start at 30, houses at 15 so there is a weird spot, Others at 58.
- The code predicts a weirdly small number whenever there is no Furnished AND Equipped-kitchen, so one of them HAS to be True to get a normal price.
