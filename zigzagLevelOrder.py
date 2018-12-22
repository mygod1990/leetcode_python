#锯齿二叉树
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        quene=[[root,0]]
        out=[]
        pre=0
        new=[]
        while(len(quene)>0):
            next=quene.pop(0)
            if next[1]!=pre:
                if pre%2==1:
                    new.reverse()
                out.append(new)
                new=[]
            new.append(next[0].val)
            pre=next[1]
            if next[0].left:
                quene.append([next[0].left,next[1]+1])
            if next[0].right:
                quene.append([next[0].right,next[1]+1])
        out.append(new)
        return out
root=TreeNode(3)
left=TreeNode(5)
right=TreeNode(7)
root.left=left
root.right=right
right_1=TreeNode(20)
left_1=TreeNode(9)
right.left=left_1
right.right=right_1
slu=Solution()
slu.zigzagLevelOrder(root)



