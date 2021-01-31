#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/30 5:21 PM
# @Author: wisdom
# @File:permute.py
from typing import List


def claimbStairs(n: int) -> int:
    dp = {}
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    print('claimb stairs')
    nums = [1, 2, 3]
    n = int(input())
    print(claimbStairs(n))
