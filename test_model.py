import unittest
import pickle
import pandas as pd
from sklearn.metrics import r2_score


class TestModel(unittest.TestCase):

    def setUp(self):
        self.val = pd.read_csv('temp_data/val.csv')
        self.y_val = pd.read_csv('temp_data/y_val.csv')
        with open('pickle_model.pkl', 'rb') as file:
            self.model = pickle.load(file)

    def test_r2_score(self):
        predict = self.model.predict(self.val)
        score = r2_score(self.y_val, predict)
        self.assertGreaterEqual(score, 0.5)
        #self.assertLessEqual(score, 0.5)
