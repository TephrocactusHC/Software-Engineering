import unittest
import max_product as mxpd
from unittest.mock import patch
class TestMaxProduct(unittest.TestCase):
    """单元测试类"""
    def test_common_case(self):
        #数组长度为1
        self.assertEqual(mxpd.unit_test([2]),2)
        self.assertEqual(mxpd.unit_test([-2]),-2)
        #全正整数
        self.assertEqual(mxpd.unit_test([3,4,5]),60)
        #全负整数
        self.assertEqual(mxpd.unit_test([-3,-4,-5]),20)
        #正负整数混合
        self.assertEqual(mxpd.unit_test([2,3,-4,5]),6)
        #全浮点数
        self.assertEqual(mxpd.unit_test([2.0,-3.0,4.0,5.0]),20)
        #整数浮点数混合
        self.assertEqual(mxpd.unit_test([2,-3.0,4,5.0]),20)
        #带0
        self.assertEqual(mxpd.unit_test([-2,0,-1]),0)

    @patch('builtins.input')
    def test_read_from_stdin(self, mock_input):
        #数组长度为1
        mock_input.return_value = '[2]'
        self.assertEqual(mxpd.unit_test([2]),2)
        mock_input.return_value = '[-2]'
        self.assertEqual(mxpd.unit_test([-2]),-2)
        #全正整数
        mock_input.return_value = '[3，4，5]'
        self.assertEqual(mxpd.unit_test([3,4,5]),60)
        #全负整数
        mock_input.return_value = '[-3,-4,-5]'
        self.assertEqual(mxpd.unit_test([-3,-4,-5]),20)
        #正负整数混合
        mock_input.return_value = '[2,3,-4,5]'
        self.assertEqual(mxpd.unit_test([2,3,-4,5]),6)
        #全浮点数
        mock_input.return_value = '[2.0,-3.0,4.0,5.0]'
        self.assertEqual(mxpd.unit_test([2.0,-3.0,4.0,5.0]),20)
        #整数浮点数混合
        mock_input.return_value = '[2,-3.0,4,5.0]'
        self.assertEqual(mxpd.unit_test([2,-3.0,4,5.0]),20)
        #带0
        mock_input.return_value = '[-2,0,-1]'
        self.assertEqual(mxpd.unit_test([-2,0,-1]),0)



if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestMaxProduct("test_common_case"), TestMaxProduct("test_read_from_stdin")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)