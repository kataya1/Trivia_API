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

            # creating a dummy entry
            self.q = Question(question="how u doing?", answer="ok", category=4, difficulty=1)
            self.db.session.add(self.q)
            self.db.session.flush()
        
    
    def tearDown(self):
        """Executed after reach test"""
        
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['categories'])
    
    def test_get_categories_questions(self):
        res = self.client().get(f'/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['current_category'], 1)
        

    def test_delete_questions(self):
        res = self.client().delete(f'/questions/{self.q.id}')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.q, None)
    
    def test_delete_questions_nonexistant_book(self):
        id = 99999
        res = self.client().delete(f'/questions/{id}')
        self.assertEqual(res.status_code, 422)
        q = Question.query.filter(Question.id == id).one_or_none()
        self.assertEqual(q, None)
    
    def test_search_question_with_result(self):
        res = self.client().post('/questions', json={'searchTerm': 'who'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])
 
    def test_search_question_without_result(self):
        res = self.client().post('/questions', json={'searchTerm': 'wsrtrhrethrshtiuarhe'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['questions'], [])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])

    def test_add_question(self):
        res = self.client().post('/questions', json={'question' : 'who?', 'answer' : 'who who?', 'difficulty' : 2, 'category' : 4})
        self.assertEqual(res.status_code, 200)
    
    def test_add_question_fail(self):
        res = self.client().post('/questions', json={ 'answer' : 'who who?', 'difficulty' : 2, 'category' : 4})
        self.assertEqual(res.status_code, 400)
    
    def test_405_create_queston(self):
        res = self.client().post('/questions/1', json={'question' : 'who?', 'answer' : 'who who?', 'difficulty' : 2, 'category' : 4})
        self.assertEqual(res.status_code, 405)
        

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
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()