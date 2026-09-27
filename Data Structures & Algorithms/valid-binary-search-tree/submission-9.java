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
    public boolean isValidBST(TreeNode root) {
        return validBST(Integer.MIN_VALUE, root, Integer.MAX_VALUE);
    }
    private boolean validBST(int left, TreeNode root, int right) {
        if (root == null) {
            return true;
        }
        if (left < root.val && root.val < right) {
            return validBST(left, root.left, root.val) && validBST(root.val, root.right, right);
        }
        else {
            return false;
        }
    }
}
