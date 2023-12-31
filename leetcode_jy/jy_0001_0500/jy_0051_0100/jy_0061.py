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
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Rotate-List(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = "链表反转技巧 | IMP"



"""
Given a linked list, rotate the list to the right by `k` places, where `k`
is non-negative.


Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation: rotate 1 steps to the right: 5->1->2->3->4->NULL
             rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation: rotate 1 steps to the right: 2->0->1->NULL
             rotate 2 steps to the right: 1->2->0->NULL
             rotate 3 steps to the right: 0->1->2->NULL
             rotate 4 steps to the right: 2->0->1->NULL


Constraints:
1) The number of nodes in the list is in the range [0, 500].
2) -100 <= Node.val <= 100
3) 0 <= k <= 2 * 10^9
"""

from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法 1: 寻找旋转规律 (以 1->2->3->4->5 和 k=2 为例进行思考)

假设将单链表的尾结点指向头结点成为一个环, 则旋转链表等价于从头结点
开始逆时针方向后退 k mod L 步 (L 为链表的长度), 后退结束后所处的结
点即为新链表的头结点, 同时解除前继结点对此结点的 next 指向

遍历链表, 将链表的结点放入 Map 中, key 为结点的序号 (从 1 开始), value 为
结点, 然后计算出需要后退的步数, 记为 step, 则 L - step + 1 对应的节点就是
新链表的头结点, 从 Map 中取出即可
    """
    def rotateRight_v1(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        current = head
        i, index_to_node = 0, {}
        # jy: 将链表的结点放入一个 Map 中, key 为结点的序号 (从 1 开始)
        while current:
            i += 1
            index_to_node[i] = current
            current = current.next

        # jy: 计算需要后退的步数 (此时的 i 即为链表的长度)
        step = k % i
        if step == 0:
            return head

        # jy: 将原链表的末尾节点与头节点进行拼接, 形成一个环;
        #     index_to_node[i] 即旋转前链表 (原链表) 的末尾节点
        index_to_node[i].next = head

        # jy: index_to_cut 即旋转后新链表的末尾节点, 将末尾节点
        #     的 next 设置为 None
        index_to_cut = i - step
        index_to_node[index_to_cut].next = None

        # jy: 旋转后新链表的头节点即下标为 index_to_cut + 1 对应的节点
        return index_to_node[index_to_cut + 1]


    """
解法 2: 优化解法 1, 无需使用 Map 存储节点

将链表进行首尾相连变成一个环, 解法 1 是从头结点后退 k mod L 步, 而当前解法是
从头结点正向移动 L - (k mod L) - 1 步 (无需使用 Map 来记录每个结点的位置), 求
得步数后正向再遍历一次指定步数的链表即可, 遍历完成后的结点的下一个结点就是新
链表的头结点, 同时断开此结点的 next 指针
    """
    def rotateRight_v2(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        # jy: 计算出链表的长度
        i = 1
        current = head
        while current.next:
            i += 1
            current = current.next

        # jy: 计算出需要正向移动的步数 (经过以上步骤后, i 为链表的长度,
        #     current 为链表结尾)
        step = i - k % i - 1

        # jy: 此时的 current 为末尾节点, 将 current.next 设置为 head 使
        #     得链表成为一个环
        current.next = head

        # jy: 重新从头节点正向移动 step 步后, current 节点即为新链表的末
        #     尾节点, 其 next 值应为新链表的头节点, 先通过 current.next
        #     获取头节点, 随后将 current.next 设置为 None, 并返回头节点,
        #     即完成了整个反转过程
        current = head
        for i in range(step):
            current = current.next
        new_head = current.next
        current.next = None
        return new_head



ls1 = [1, 2, 3, 4, 5]
ln1 = getListNodeFromList(ls1)
showLnValue(ln1, "ListNode1")
k = 2
res = Solution().rotateRight_v1(ln1, k)
# jy: "4->5->1->2->3->NULL"
showLnValue(res, "result(k=%s)" % k)


ls2 = [0, 1, 2]
ln2 = getListNodeFromList(ls2)
showLnValue(ln2, "ListNode1")
k = 4
res = Solution().rotateRight_v2(ln2, k)
# jy: "2->0->1->NULL"
showLnValue(res, "result(k=%s)" % k)






