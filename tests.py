import unittest
import numpy as np

from SecretSantaSolver.data_structures import *


class TestPerson(unittest.TestCase):
    
    soup = Person("Soup", "example@email.com")
    xian = Person("Xian", "another@email.com")
    cole = Person("Cole", "example@google.com")
    kate = Person("Kate", "email@gmail.com")
    jong = Person("Jong", "anyemail@email.com")
    
    #Tests
    def testBanUser(self):
        self.soup.banUser(self.xian)
        self.soup.banUser(self.cole)
        
        result = self.soup.getBanlist()
        expected = [self.xian, self.cole]
        
        self.assertEqual(result, expected)
    
    def testGetters(self):
        result = self.kate.getName()
        expected = "Kate"
        
        self.assertEqual(result, expected)
        
        result = self.jong.getEmail()
        expected = "anyemail@email.com"
        
        self.assertEqual(result, expected)
    
    
class TestAdj_Matrix(unittest.TestCase):
    #setup
    soup = Person("Soup", "example@email.com")
    xian = Person("Xian", "another@email.com")
    cole = Person("Cole", "example@google.com")
    kate = Person("Kate", "email@gmail.com")
    jong = Person("Jong", "anyemail@email.com")
    
    users = [soup, xian, cole, kate, jong]
    
    def testMatrixCreation(self):
        matrix = Adjacency_Matrix(self.users)
        result = matrix.getMatrix()
        
        expected = np.array([
            [0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0]
        ])
        
        self.assertIsNone(np.testing.assert_array_equal(result, expected))
    
    def testMatrixModification(self):
        matrix = Adjacency_Matrix(self.users)
        
        self.xian.banUser(self.xian)
        self.xian.banUser(self.kate)
        self.jong.banUser(self.cole)
        
        matrix.initBans()
        
        result = matrix.getMatrix()
        
        expected = np.array([
            [0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 0, 1, 0]
        ])
        
        self.assertIsNone(np.testing.assert_array_equal(result, expected))
    

if __name__ == '__main__':
    unittest.main()