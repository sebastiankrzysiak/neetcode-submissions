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
    private int result = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        findMaxPathSum(root);
        return result;
    }

    private int findMaxPathSum(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = Math.max(findMaxPathSum(root.left), 0);
        int right = Math.max(findMaxPathSum(root.right), 0);

        result = Math.max(result, root.val + left + right);

        return root.val + Math.max(left, right);
    }
}
