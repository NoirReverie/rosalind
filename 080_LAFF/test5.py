from laff5 import *
import unittest

class MatrixTestCase(unittest.TestCase):
    def test_spot_check_matrix(self):
        print('test_spot_check_matrix')
        scoring_matrix = read_scoring_matrix('BLOSUM62.txt')
        self.assertEqual( scoring_matrix['AA'], 4 )
        self.assertEqual( scoring_matrix['WC'], -2 )
        self.assertEqual( scoring_matrix['CW'], -2 )
        self.assertEqual( scoring_matrix['WW'], 11 )
        
    def test_align(self):
        print('test_align')
        scoring_matrix = read_scoring_matrix('BLOSUM62.txt')
        best_score, local_a, local_b = local_align('PLEASANTLY', 'MEANLY', scoring_matrix)
        self.assertEqual(best_score, 12)
        self.assertEqual(local_a, 'LEAS')
        self.assertEqual(local_b, 'MEAN')
        
    def test_align_2(self):
        print('test_align_2')
        scoring_matrix = read_scoring_matrix('BLOSUM62.txt')
        a = 'LLLLLWWWWWCCCCCCCCWWWWWWWWWWLLLLL'
        b = 'DDDDDWWWWWWWWWWQQQQQQQQWWWWWDDDDD'
        best_score, local_a, local_b = local_align(a, b, scoring_matrix)
        self.assertEqual(best_score, (11*5*3)-(18*2))
        self.assertEqual(local_a, 'WWWWWCCCCCCCCWWWWWWWWWW')
        self.assertEqual(local_b, 'WWWWWWWWWWQQQQQQQQWWWWW')
        
if __name__=='__main__':
    unittest.main()