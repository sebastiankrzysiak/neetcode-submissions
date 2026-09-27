class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;

        if (nums[l] <= nums[r]) {
            return nums[l];
        }

        while (r - l > 1) {
            int m = (l + r) / 2;
            if (isBefore(nums, m)) {
                l = m;
            } else {
                r = m;
            }
        }

        return nums[r];
    }

    private boolean isBefore(int[] nums, int i) {
        return nums[0] < nums[i];
    }
}
