# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
---
## API reference
### Getting Started
 - Base URL: runs Locally and is not hosted as a base URL. the backend app is hosted at http://127.0.0.1:5000 as a proxy in the frontend configurations 
 - Authentication: Doesn't require authentication or API keys
### Error Handling
errors are returned as a json objects in the following format:
```JSON
{
    "success": False,
    'error': 404,
    'message': "resource not found",
}
```
the API will return three error types when requests fail:
 - 400: Bad Request
 - 404: Resource Not Found
 - 422: Not Processable
 <!-- - 500: Internal server Error  -->
 ### Endpoints
 - GET /categories
 - GET /categorise/{categories_id}/questions
 - GET /questions?page={page_number}
 - POST /questions
 - DELETE /questions/{question_id}
 - POST /quizzes

 #### GET /categories 
 - Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
 - Request Arguments: None
 - Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
```JSON
{
    '1' : "Science",
    '2' : "Art",
    '3' : "Geography",
    '4' : "History",
    '5' : "Entertainment",
    '6' : "Sports"
}
```
#### GET /categorise/{categories_id}/questions
 - Fetches a list of questions JSON with that category
 - Request Arguments: None
 - Returns: an object "current_category": current_category_id and a list of questions JSON
```JSON
{
  "current_category": 6, 
  "questions": [
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }
  ], 
  "total_questions": 2
}

```
#### GET /questions?page={page_number}
 - Fetches a question page, 10 questions per page. if page in the url is ommited it gets the first page 
 - Request Argument: None
 - Returns: a json object that has a list of 10 or less question objects, the number of total questions,  a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category, the current_cattegory
 ```JSON
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_cattegory": {
    "id": 1, 
    "type": "Science"
  }, 
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": 4, 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "total_questions": 19
}

 ```
#### POST /questions
 - Creates a new question using the submitted question, answer, difficulty and category 
 - Request Argument: question text, answer text, difficutly intiger, category text
 ```json
{"question":"When was the pyramid built? ","answer":"2630 B.C.","difficulty":"3","category":"4"}
```
 - Returns: json success flag
 ```JSON
 {
  "success": true
}
 ```
#### POST /questions
 - searches all the questions for partialy matching case insensetive text specified in the 'searchTerm' we send in the request body
 - Request Argument: json object with 'searchTerm' as id and the text to be matched as the value
 ```json
 {"searchTerm":"tom"}
 ```
 - Returns: a JSON object with a list of JSON question objects, the number of total questions matching and the current_category
```JSON
{
  "current_category": 5, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }
  ], 
  "total_questions": 1
}
```
#### DELETE /questions/{question_id}
 - delete the question with that id
 - Request Argument: None
 - Returns: json succes flag
 ```json
 {
    "success": true,
}
```
#### POST /quizzes
 - Gets questions to play the quiz. takes category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
 - Request Argument: a json object with previous_questions list  which is a list of questions id (can be ommited on the first question of the quiz), and a quiz_category  which is an object with a single key, categories, that contains a object of id: category_string key:value pairs
 ```JSON
 {"previous_questions":[20,21],"quiz_category":{"type":"Science","id":"1"}}
 ```
 - Returns: a json object with a question dictionary with it id,  question, answer, difficulty, and category as key and there values
 ```JSON
{
  "question": {
    "answer": "Blood", 
    "category": 1, 
    "difficulty": 4, 
    "id": 22, 
    "question": "Hematology is a branch of medicine involving the study of what?"
  }
}
 ```
 ---
## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
