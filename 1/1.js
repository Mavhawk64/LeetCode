// Accepted: 08/02/2021
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    for (var i = 0; i < nums.length; i++) {
        var j = target - nums[i];
        if (nums.includes(j)) {
            var y = nums.indexOf(j);
            if (y != i) {
                var x = [i, y];
                return x;
            }
        }
    }
    return null;
};