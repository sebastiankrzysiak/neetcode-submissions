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

class Solution {
    private int result = 0;

    public int goodNodes(TreeNode root) {
        dfs(root, Integer.MIN_VALUE);
        return result;
    }

    private void dfs(TreeNode root, int biggest) {
        if (root == null) {
            return;
        }

        if (root.val >= biggest) {
            result++;
            biggest = root.val;
        }

        dfs(root.left, biggest);
        dfs(root.right, biggest);
    }
}
