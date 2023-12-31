# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
assert project_name == "leetcode_jy" and project_name == "leetcode_jy" and \
       url_ == "www.yuque.com/it-coach"
from typing import List, Dict
# jy: 记录该题的难度系数
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "wildcard-matching(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | 双指针 |  | 相似题: 0010 (匹配规则有所不同)"


"""
Given an input string `s` and a pattern `p`, implement wildcard pattern
matching with support for "?" and "*".
1) "?" Matches any single character.
2) "*" Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).


Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not
             match 'b'.

Example 4:
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*'
             matches the substring "dce".

Example 5:
Input: s = "acdcb", p = "a*c?b"
Output: false


Constraints:
1) 0 <= s.length, p.length <= 2000
2) `s` contains only lowercase English letters.
3) `p` contains only lowercase English letters, '?' or '*'.
"""


class Solution:
    """
解法 1: 动态规划

0010 (regular-expression-matching) 中的匹配规则:
1) "." Matches any single character.
2) "*" Matches zero or more of the preceding element. 
   注意: 是匹配前一个字符 0 次或多次

本题中的匹配规则:
1) "?" Matches any single character.
2) "*" Matches any sequence of characters (including the empty sequence).
   注意: "*" 匹配任意字符 0 个或多个字符


定义 dp[i][j] = True 表示 s 的前 i 个字符 s[:i] 和 p 的前 j 个字符 p[:j] 匹配
    """
    def isMatch_v1(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        # jy: 初始化 dp 二维列表, 并设置 dp[0][0] 为 True (空字符与空匹配模
        #     式相互匹配)
        dp = [[False for _ in range(len_p + 1)] for _ in range(len_s+1)]
        dp[0][0] = True

        for j in range(1, len_p+1):
            # jy: 如果 p 的第 j 个字符 p[j-1] 为 "*", 则 dp[0][j] = dp[0][j-1],
            #     即: s 的前 0 个字符 (空字符) 与 p 的前 j 个字符的匹配情况等同
            #     于 s 的前 0 个字符 (即空字符) 与 p 的前 j-1 个字符的匹配情况
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        # jy: 从前往后遍历 s 中的每一个字符 (为了便于理解, i 从 1 开始, 代表第
        #     i 个字符, 对应的下标为 i-1, 即 s[i-1])
        for i in range(1, len_s+1):
            # jy: 从前往后遍历 p 中的每一个字符 (j 从 1 开始, 代表第 j 个, 对应
            #     的下标为 j-1, 即 p[j-1])
            for j in range(1, len_p+1):
                # jy: 如果 p 的第 j 个字符 p[j-1] 为 "*", 则满足以下条件中的任
                #     何一个即可确认 s 的前 i 个字符与 p 的前 j 个字符匹配:
                #     1) s 的前 i-1 与 p 的前 j 个的匹配 (即 dp[i-1][j] == True)
                #        因为当 s 的前 i-1 个字符已经与 p 的前 j 个字符匹配, 此
                #        时 s 的第 i 个字符也同样可以被 p 的第 j 个字符 "*" 匹配
                #        (因为 "*" 可匹配 0 个或多个任意字符)
                #     2) s 的前 i 个字符与 p 的前 j-1 个字符匹配 (即 dp[i][j-1] == True)
                #        因为当 s 的前 i 个字符与 p 的前 j-1 个字符匹配了, 且此
                #        时 p 的第 j 个字符为 "*", 由于其可以匹配 0 个字符, 因
                #        此也能确认 s 的前 i 个字符与 p 的前 j 个字符匹配
                if p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                # jy: 如果 p 的第 j 个字符 p[j-1] 不为 "*", 则只有确保 s 的前
                #     i-1 个字符与 p 的前 j-1 个字符匹配 (dp[i-1][j-1] == True)
                #     且满足以下任意一个条件时, 才能确保 s 的前 i 个字符与 p 的
                #     前 j 个字符相互匹配:
                #     1) s 的第 i 个字符与 p 的第 j 个字符相等 (即 s[i-1] == p[j-1])
                #     2) p 的第 j 个字符 p[j-1] 为 "?" (此时不管 s 的第 i 个字
                #        符是什么, "?" 都可以与之匹配)
                else:
                    dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == '?') and dp[i-1][j-1]
        return dp[len_s][len_p]


    """
解法 2: 动态规划 (另一角度的理解)

看代码注解之前, 先参考图解: https://www.yuque.com/it-coach/leetcode/qeuski 
    """
    def isMatch_v2(self, s: str, p: str) -> bool:
        """
        s 作为横轴 (对应列), p 作为纵轴 (对应行)

        table[i][j] == True 表示 s 的前 j 个字符 s[:j] 与 p 的前 i 个字符
        p[:i] 匹配; table[0][0] 初始化为 True, 表示 s[:0] 与 p[:0] (均为空
        字符) 相互匹配
        """
        # jy: 如果模式串 p 中的字符均为 "*", 则直接返回 True
        if set(p) == {"*"}:
            return True

        # jy: 纵轴长度 (即行数, 比模式串 p 的长度多 1)
        num_row = len(p) + 1
        # jy: 横轴长度 (即列数, 比原字符串 s 的长度多 1)
        num_column = len(s) + 1

        # jy: 初始化表格, 左上角设置为 True
        table = [[False] * num_column for i in range(num_row)]
        table[0][0] = True

        # jy: 如果模式串 p 的第一个字符为 "*", 则将 table[1] 均设置为 True,
        #     表明 s 的前 j 个字符 s[:j] (j 为任意有效值) 均与 p 的第 1 个
        #     字符 p[:1] 匹配 ("*" 能匹配任意字符 0 次或多次)
        if p.startswith("*"):
            table[1] = [True] * num_column

        # jy: 遍历表中的所有行 (行数为模式串 p 的长度加 1)
        for m in range(1, num_row):
            # jy: 遍历表中的所有列 (列数为原字符串 s 的长度加 1)
            for n in range(1, num_column):
                # jy: 如果模式串 p 的第 m 个字符 p[m-1] 为 "*", 此时判断第 m 个
                #     字符对应的行的前一行中的第一列开始列 (即 table[m-1][0]) 
                #     是否为 True, 如果是, 则下一行中该列及以后的所有列均应设置
                #     为 True (使用 "*" 角色的特技)
                if p[m-1] == "*":
                    if table[m-1][0]:
                        # jy: 以下两个语句等价
                        #table[m][0:] = [True] * num_column
                        table[m] = [True] * num_column
                        # jy: 此处补充 break 优化性能
                        break
                    # jy; 只要顶上有 True, 就可以使用 "*" 角色的特技 (上一行某列
                    #     的值为 True, 则当前行的该列以及之后的列均设置为 True)
                    if table[m-1][n]:
                        table[m][n:] = [True] * (num_column - n)
                        # jy: 此处补充 break 优化性能
                        break
                # jy: 如果模式串 p 的第 m 个字符 p[m-1] 不为 "*", 而是以下两种
                #     情况之一时, 则 s 的前 n 个字符与 p 的前 m 个字符的匹配情
                #     况等同于 s 的前 n-1 个字符与 p 的前 m-1 个字的匹配情况:
                #     1) p 的第 m 个字符 p[m-1] 为 "?"
                #     2) p 的第 m 个字符 p[m-1] 与 s 的第 n 个字符 s[n-1] 相同
                elif p[m-1] == "?" or p[m-1] == s[n-1]:
                    table[m][n] = table[m-1][n-1]

        # jy: 最终返回表格中的最右下角中的值
        return table[num_row - 1][num_column - 1]


    """
解法 3: 双指针法 (性能极佳, 逻辑值得深度思考)

因为 "*" 能匹配任意字符 0 至 n 次, 因此可以用元组 (i, j) 记录当碰到 "*" 时,
用 "*" 匹配 s 中的字符 n 次 (n 可以为 0) 后, 下一个需要对 s 和 p 进行匹配的
位置下标 (i 为 s 的位置下标, j 为 p 的位置下标)
    """
    def isMatch_v3(self, s: str, p: str) -> bool:
        # jy: 初始化双指针 i 和 j 分别指向 s 和 p 的初始位置
        i, j = 0, 0
        # jy: 记录截止目前为止是否碰到了 "*" 字符
        flag = False
        # jy: tmp 用于记录当模式串 p 中碰到 "*" 时, 用 "*" 匹配 n 次 (n 可以
        #     为 0) s 中的字符后, 下一个 s 和 p 要进行匹配的下标位置 (tmp[0]
        #     记录 s 的下标, tmp[1] 记录 p 的下标)
        # jy: 注意: 此处初始化主要是为了规范变量定义, 注释掉逻辑也正常
        tmp = (None, None)
        while i < len(s):
            # jy: 优先进行精确匹配, 如果 s[i] == p[j], 或 p[j] 为 "?", 则表示
            #     截止当前位置 s[i] 和 p[j] 均能相互匹配, 此时双指针均进 1
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            # jy: 如果 s[i] 和 p[j] 不能精确匹配, 则判断 p 是否有 "*" 可以与
            #     s[i] 匹配; 如果当前字符 p[j] 为 "*", 则让其优先匹配 0 个 s
            #     中的字符 (即当前的 "*" 先不匹配 s[i]), 尝试用 p 的下一个字
            #     符 (即 j 加 1) 与 s[i] 匹配, 将后续要匹配的位置记录到 tmp
            #     变量, 并更新 flag 为 True (表示碰到了 "*")
            elif j < len(p) and p[j] == '*':
                flag = True
                j += 1
                tmp = (i, j)
            # jy: 当以上 "*" 匹配 0 个字符后, 进入下一轮循环进行下一个位置的
            #     匹配, 此时如果 s[i] 和 p[j] 不能匹配, 则再尝试用 "*" 匹配 s
            #     中的 1 个字符 (即 i 在 tmp[0] 的基础上进 1, j 保持不变), 更 
            #     新 tmp 为最新的 (i, j), 即后续需要对该下标对应的字符进行匹
            #     配; 如果 "*" 匹配 s 中的 1 个字符后, 还是不能使得后续的 i 和
            #     j 相互匹配, 则继续用 "*" 匹配 s 中的 2 个, 3 个, ... (即 i 
            #     不断在原 tmp[0] 基础上进 1) 直到把 s 中的所有字符都匹配完(此
            #     时会退出当前 while 循环) 或后续的 s 和 p 的相应位置可以匹配
            #     (此时会基于后续的字符进行匹配, 如果后续匹配过程中发现不能正
            #     常匹配, 会再重新回到 tmp 的位置用 p 中的指定位置的 "*" 匹配
            #     更多次的 s 中的字符) 为止
            elif flag:
                i = tmp[0] + 1
                j = tmp[1]
                tmp = (i, j)
            # jy: 当 p 中的字符遍历完 (没发现有 "*"), 但 s 中还有剩余待匹配字
            #     符时, 此时表明 s 和 p 不能匹配, 直接返回 False
            else:
                return False

        # jy: 如果 s 中的字符都被匹配完 (即退出以上 while 循环), 但 p 中还有待
        #     匹配的字符时, 如果剩余字符中有非 "*" 字符, 表明 s 和 p 不能匹配
        while j < len(p):
            if p[j] != '*':
                return False
            j += 1
        return True


s = "aa"
p = "a"
res = Solution().isMatch_v1(s, p)
print(s, " === ", p, " === ", res)

s = "aa"
p = "*"
res = Solution().isMatch_v1(s, p)
print(s, " === ", p, " === ", res)

s = "cb"
p = "?a"
res = Solution().isMatch_v2(s, p)
print(s, " === ", p, " === ", res)

s = "adceb"
p = "*a*b"
res = Solution().isMatch_v3(s, p)
print(s, " === ", p, " === ", res)

s = "acdcb"
p = "a*c?b"
res = Solution().isMatch_v3(s, p)
print(s, " === ", p, " === ", res)



