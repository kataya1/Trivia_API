import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://postgres:postgres@{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

            # creating a dummy entry. for a question to be deleted
            self.q = Question(question="how u doing?", answer="ok", category=4, difficulty=1)
            self.db.session.add(self.q)
            self.db.session.flush()
            self.id_to_be_deleted = self.q.id
            self.db.session.commit()
            
        
    
    def tearDown(self):
        """Executed after reach test"""
        
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # categories
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['categories'])
    
    def test_get_categories_questions(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['current_category'], 1)
        
    # questions
    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])
        self.assertTrue(data['current_cattegory'])

    def test_get_paginated_questions_beyond(self):
        res = self.client().get('/questions?page=999')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_add_question(self):
        res = self.client().post('/questions', json={'question' : 'who?', 'answer' : 'who who?', 'difficulty' : 2, 'category' : 4})
        self.assertEqual(res.status_code, 200)
    
    def test_add_question_fail(self):
        res = self.client().post('/questions', json={ 'answer' : 'who who?', 'difficulty' : 2, 'category' : 4})
        self.assertEqual(res.status_code, 422)

    def test_search_question_with_result(self):
        res = self.client().post('/questions', json={'searchTerm': 'who'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])
 
    def test_search_question_without_result(self):
        res = self.client().post('/questions', json={'searchTerm': 'whpftrsuetrsyuothreshtreho'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['questions'], [])
        self.assertEqual(data['total_questions'], 0)
        

    def test_405_create_queston(self):
        res = self.client().post('/questions/1', json={'question' : 'who?', 'answer' : 'who who?', 'difficulty' : 2, 'category' : 4})
        self.assertEqual(res.status_code, 405)
        

    
    def test_delete_question(self):
        id = self.id_to_be_deleted
        res = self.client().delete(f'/questions/{id}')
        self.assertEqual(res.status_code, 200)
        q = Question.query.filter(Question.id == id).one_or_none()
        self.assertEqual(q, None)

    def test_delete_questions_nonexistant_question(self):
        
        res = self.client().delete('/questions/999')
        self.assertEqual(res.status_code, 404)
        
    # quizzez
    def test_quizes(self):
        previous_questions = []
        res = self.client().post('/quizzes', json={'previous_questions' : previous_questions, 'quiz_category' :{'id': 2, 'type': "Art"}})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertNotIn(data['question'], previous_questions)
        
        

    # server connection
    def test_server_connection(self):
        # test if there is a postgres server running
        res = self.client()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()