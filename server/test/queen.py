# coding=utf-8

"""
    八皇后问题
    在一个 8×8 国际象棋盘上,有 8 个皇后,每个皇后占一格;
    要求皇后间不会出现相互攻击的现象,即不能有两个皇后处在同一行、同一列或同一对角线上,问共有多少种不同的方法。
"""

from copy import deepcopy

queenNum = 8  # 皇后数
resultList = []  # 结果列表


# 判断2个皇后位置是否可以并存
def canQueen(t1, t2):
    r1, c1 = t1
    r2, c2 = t2
    if r1 == r2 or c1 == c2 or (r1 - c1 == r2 - c2) or (r1 + c1 == r2 + c2):
        return False
    else:
        return True


# 判断此皇后位置是否可以和之前的皇后们并存
def canQueenWithList(queenList, t):
    for v in queenList:
        if not canQueen(v, t):
            return False
    return True


def findQueen(existList, curRow):
    """ 递归查找皇后
        Args:
            existList: 已确定的 之前行的 皇后位置列表
            curRow: 当前查找行
    """
    global resultList
    global queenNum

    if curRow > queenNum:
        resultList.append(existList)
    else:
        for v in range(1, queenNum + 1):
            t = (curRow, v)
            if canQueenWithList(existList, t):
                childList = deepcopy(existList)
                childList.append(t)
                findQueen(childList, curRow + 1)

# 从第一行发起查找
findQueen([], 1)

print len(resultList)

