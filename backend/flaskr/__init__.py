import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from random import choice

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods','GET,POST,PATCH,DELETE,OPTIONS')
        return response

    #Pagination commmon function
    def paginate_questions(request, selection):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10
        end = start + 10
        questions = [question.format() for question in selection]
        current_questions = questions[start:end]
        return current_questions


    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.all()
        #formatted_category = [category.format() for category in categories]

         #create dict item
        categoriesD = {}
        for category in categories:
            categoriesD[category.id] = category.type

        if categories is None:
            abort(403) #no data found
        else:
            return jsonify({
                'success':True,
                'categories':categoriesD
            })



    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions', methods=['GET'])
    def get_questions():
        page=request.args.get('page',1,type=int)
        start = (page-1)*10
        end = start+10
        #get all questions list
        questions = Question.query.order_by(Question.id).all()
        #formatted_question = [question.format() for question in questions]
        categories = Category.query.order_by(Category.id).all()
        # Get all Categories
        
        #create dict item
        categoriesD = {}
        for category in categories:
            categoriesD[category.id] = category.type


        if questions is None:
            abort(403) #no data found
        else:
            return jsonify({
                'success':True,
                'questions':paginate_questions(request,questions),
                'total_questions':len(questions),
                'categories':categoriesD,
                'current_category':'why this is required'
            })

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question_by_id(question_id):
        question=Question.query.filter(Question.id==question_id).one_or_none()
        
        if question is None:
            abort(403)
        else:
            question.delete()
            return jsonify({
                'success':True
              })
   

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route('/questions', methods=['POST'])
    def add_question():
        body=request.get_json()
        new_question =Question(question=body.get('question'),answer=body.get('answer'),difficulty=body.get('difficulty'),category=body.get('category'))
        try:
            new_question.insert()

            # send back the current questions
            questions = Question.query.order_by(Question.id).all()
            updated_questions = paginate_questions(request, questions)
            return jsonify({
                'success': True,
                'questions': updated_questions,
                'total_questions': len(questions)
            })
        except:
            abort(422)
        

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/search_question', methods=['POST'])
    def search_question():
        body=request.get_json()
        searchString="%{}%".format(body.get('searchTerm'))
        print(searchString)
        try:
            #search question by search string 
            questions = Question.query.filter(Question.question.like(searchString)).all()
            formatted_question = [question.format() for question in questions]
            return jsonify({
                'success':True,
                'questions':formatted_question,
                'totalQuestions':len(questions),
                'currentCategory':'none'
            })
        except:
            abort(422)



    """
    @TODO:
    Create a GET endpoint to get questions based on category.
    
    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<int:id>/questions', methods=['GET'])
    def get_cat_question(id):

        #gET QUESTION BY Category id, id is available in request
        questions = Question.query.filter(Question.category==id).all()
        category=Category.query.filter_by(id=id).one_or_none()
        if questions is None:
            abort(403)   
        else:
            #format question in dict view
            formatted_question = [question.format() for question in questions]
            return jsonify({
                'success':True,
                'questions':formatted_question,
                'totalQuestions':len(questions),
                'currentCategory':category.type
            })
            
    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/quizzes', methods=['POST'])
    def quizze_question():
        body=request.get_json()  # fetch json parameters         
        prev_question=body.get('previous_questions') 
        qz_category=body.get('quiz_category') 
        if prev_question is None:
            prev_question=['0']
        print(qz_category['id'])
        try:
            #if selected all 
            if qz_category['id']==0:
                questions = Question.query.order_by(Question.id).all()      
            else:
                questions = Question.query.filter(Question.category==qz_category['id']).all()
           

            #get random question id not equal to previous question
            nextQuestion_id=choice([i for i in range(0,len(questions)) if i not in prev_question])
            if nextQuestion_id ==0:
                return jsonify({
                    'success':False         
                })
            else:
                next_question=questions[nextQuestion_id]
                 #create dict item
                #QuestionD = {}            
                #QuestionD[next_question.id] = next_question.question
                #print(QuestionD)   
                return jsonify({
                    'success':True,
                    'question':next_question.format(),
                    'previousQuestion': prev_question                
                })
        except:
            abort(422)

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            'error': 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({
            "success": False,
            'error': 404,
            "message": "Resource Not found"
        }), 404
    
    @app.errorhandler(403)
    def page_not_found(error):
        return jsonify({
            "success": False,
            'error': 403,
            "message": "Question not found"
        }), 403

    @app.errorhandler(422)
    def unprocessable_recource(error):
        return jsonify({
            "success": False,
            'error': 422,
            "message": "Unprocessable Resource"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            'error': 500,
            "message": "Internal Server Error"
        }), 500

    @app.errorhandler(405)
    def invalid_method(error):
        return jsonify({
            "success": False,
            'error': 405,
            "message": "Method not allowed!"
        }), 405


    return app

