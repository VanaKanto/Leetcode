'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # add letter with increase (if start<end) or decrease(start>end) index
        def zadd(shape,index,row,increase=True):
            nonlocal numRows,s
            # each time add numRows-1 letters into shape
            end = index + numRows-1  # end before this index
            while index < len(s) and index < end:  # check remain items
            # push letter
            # update row: from [row 0 -> row numRows-2] or [row numRow-1 -> row 1]
            # update index
                shape[row].append(s[index])
                row = row+1 if increase else row-1
                index += 1

        # main
        if numRows==1: return s
        n = len(s)
        zshape = [[] for _ in range(numRows)]
        for i in range(0,n,numRows-1):
            # 分组，每numRows-1字母一组，双数【0开始】increase,单数decrease
            if (i // (numRows-1)) % 2 == 0:
                # 双数increase row=0 ~ numRows-2
                zadd(zshape,i,0)
            else:
                # 单数decrease row=numRows-1 ~ 1
                zadd(zshape,i,numRows-1,False)

        return ''.join(''.join(zshape[i]) for i in range(numRows))

def showResult(inputStr,inputN,pred_output):
    print("测试用例: ")
    print("s: %s\nnumRows: %d"%(inputStr,inputN))
    print("----------------------------------")
    print("答案:")
    print(pred_output)

def main():
    s = "PAYPALISHIRING"
    numRows = 3
    p6 = Solution()
    ans = p6.convert(s,numRows)
    showResult(s,numRows,ans)


if __name__=='__main__':
    main()