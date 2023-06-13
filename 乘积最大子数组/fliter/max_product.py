"""提供计算给定整形数组的乘积最大的非空连续子数组"""
import numpy as np
class Solution:
    """Solution Class"""
    def __init__(self) -> None:
        """初始化数组"""
        self.array = []
    def setarray(self):
        """输入数组，如果输入数组不是int数组则要求重新输入"""
        while True:
            #输入数组
            numsstr = input("please input an array, use space to split numbers:")
            #将输入的字符串数组转换为int数组
            temp = numsstr.split(' ')
            #判断输入的数组是否为int数组
            try:
                self.array = [int (x) for x in temp]
                break
            except(SyntaxError,ValueError):
                print("your input is illegal, please input again")
                continue
    def maxproduct(self) -> int:
        """考虑到乘以负数会反转符号，所以要同时存储当前最大乘积与最小乘积"""
        maxval = float('-inf')#存储当前最大乘积
        imax, imin = 1, 1#存储当前最小乘积
        for i in range(0,len(self.array)):
            #如果当前坐标的值小于0，则最大乘积与最小乘积交换
            if self.array[i] < 0:
                #比较当前最大乘积，当前坐标的值，当前最小乘积与当前坐标值的乘积
                imax, imin = imin, imax
            #比较当前最小乘积，当前坐标的值，当前最大乘积与当前坐标值的乘积
            imax = max(imax * self.array[i], self.array[i])
            imin = min(imin * self.array[i], self.array[i])
            #比较当前最大乘积与最大乘积
            maxval = max(maxval, imax)
        return maxval
    def test_set_array(self,testnum:list[int]):
        "直接设置数组"
        self.array = testnum
def profile_test(scale):
    """测试性能"""
    test_array = [np.random.randint(-10, 10) for i in range(scale)]
    mxpd = Solution()
    mxpd.test_set_array(test_array)
    mxpd.maxproduct()
def unit_test(test_array:list)->int:
    """unit测试"""
    mxpd = Solution()
    mxpd.test_set_array(test_array)
    return mxpd.maxproduct()
def main():
    """主函数"""
    solution = Solution()
    solution.setarray()
    print("the result is: "+str(solution.maxproduct()))
if __name__ == '__main__':
    main()
