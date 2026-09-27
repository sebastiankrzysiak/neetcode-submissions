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
    private boolean result = true;

    public boolean isBalanced(TreeNode root) {
        dfs(root);
        return result;
    }

    private int dfs(TreeNode root) {
        if (root == null || result == false) {
            return 0;
        }

        int left = dfs(root.left);
        int right = dfs(root.right);
        int diff = Math.abs(left - right);

        if (diff > 1) {
            result = false;
        }

        return 1 + Math.max(left, right);
    }
}
