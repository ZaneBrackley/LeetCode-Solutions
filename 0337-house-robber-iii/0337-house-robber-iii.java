/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.*;

class Solution {
    public int rob(TreeNode root) {
        Map<TreeNode, Integer> memory = new HashMap<>();
        return robTree(root, memory);
    }

    private int robTree(TreeNode node, Map<TreeNode, Integer> memory) {
        if (node == null) return 0;
        if (memory.containsKey(node)) return memory.get(node);

        int robCurrent = node.val;
        if (node.left != null) {
            robCurrent += robTree(node.left.left, memory) + robTree(node.left.right, memory);
        }
        if (node.right != null) {
            robCurrent += robTree(node.right.left, memory) + robTree(node.right.right, memory);
        }

        int skipCurrent = robTree(node.left, memory) + robTree(node.right, memory);

        int maxMoney = Math.max(robCurrent, skipCurrent);
        memory.put(node, maxMoney);
        return maxMoney;
    }
}
