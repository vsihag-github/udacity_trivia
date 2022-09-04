# Trivia API Project 

Trivia API project is online game app to test your knowledge. This project is to create multiple APIs and unit test for implementing the following features

1- Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.

2- Delete questions.

3- Add questions and require that they include question and answer text.

4- Search for questions based on a text query string.

5- Play the quiz game, randomizing either all questions or within a specific category.

## Getting Started
### Installing Dependencies

You shoul have Python3, pip3, node, and npm installed. 

### Frontend dependencies
#### Installing Node and NPM 

This project depends on Nodejs and Node Package Manager (NPM). Find and download Node and npm (which is included) at: [https://nodejs.com/en/download](https://nodejs.org/en/download/).

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```
### Backend Dependencies 

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

## Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

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

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
``` 

## API Reference

### Getting Started 
Base URL: Currently this application is only hosted locally. The backend is hosted at http://127.0.0.1:5000/
Authentication: This version does not require authentication or API keys.

### Error Handling

There are four types of errors the API will return`;
- 400 - bad request
- 403 - no Question found
- 404 - resource not found
- 422 - unprocessable

### Endpoints

#### GET '/categories'
- Fetches a dictionary of all available categories.
- return list of all categories. 
- Sample: `curl http://127.0.0.1:5000/categories`
```
"categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}

```

#### GET '/categories/<int:id>/questions'
- Get list of all question based on category selected
- Returns a JSON object with paginated questions of a selected category
- Sample: `curl http://127.0.0.1:5000/categories/3/questions`
```
  "currentCategory": "Geography",
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "New Delhi",
      "category": 3,
      "difficulty": 1,
      "id": 25,
      "question": "Which is the capital of India?"
    },
    {
      "answer": "New Delhi",
      "category": 3,
      "difficulty": 1,
      "id": 26,
      "question": "Which is the capital of India?"
    }
  ],
  "success": true,
  "totalQuestions": 5
}

```

#### GET '/questions'
  - Returns a list of all questions
  - Includes a list of all categories
  - Paginated in groups of 10
  - returns total_questions and success as True
- Sample: `curl http://127.0.0.1:5000/questions`
```
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": "why this is required",
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
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
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 21
}

```

#### POST '/questions'
- Creates a new question using JSON request parameters in the database
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "Which is the capital of India?", "answer": "New Delhi", "difficulty": 3, "category": "3" }'`
- Created question:


#### POST '/search_question'
- Serach questions questions using a searchTerm, 
- Returns a JSON object with paginated questions matching the search term
- Sample: `curl http://127.0.0.1:5000/search_question -X POST -H "Content-Type: application/json" -d '{"searchTerm": "capital"}'`
```
  "currentCategory": "none",
  "questions": [
    {
      "answer": "New Delhi",
      "category": 3,
      "difficulty": 1,
      "id": 25,
      "question": "Which is the capital of India?"
    },
    {
      "answer": "New Delhi",
      "category": 3,
      "difficulty": 1,
      "id": 26,
      "question": "Which is the capital of India?"
    }
  ],
  "success": true,
  "totalQuestions": 2
}

```

#### POST '/quizzes'
- play the trivia game
- Send category and previouls question as JSON object with request
- Returns JSON object with random available questions which are not among previous used questions
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [1, 2], "quiz_category": {"type": "Geography", "id": "3"}}'`
```
 "previousQuestion": [
    1,
    2
  ],
  "question": {
    "answer": "New Delhi",
    "category": 3,
    "difficulty": 1,
    "id": 25,
    "question": "Which is the capital of India?"
  },
  "success": true
}


```

#### DELETE '/questions/<int:id>'
- Deletes a question by id using url parameters
- Sample: `curl http://127.0.0.1:5000/questions/4 -X DELETE`
```
  {
    "success": true
  }
```

