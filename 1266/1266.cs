// Accepted: 01/14/2026
Console.WriteLine("LeetCode 1266");
var solution = new Solution();
var test1 = new int[][]
{
    [1,1],
    [3,4],
    [-1,0]
};

var test2 = new int[][]
{
    [3,2],
    [-2,2]
};
var result1 = solution.MinTimeToVisitAllPoints(test1);
Console.WriteLine(result1);
var result2 = solution.MinTimeToVisitAllPoints(test2);
Console.WriteLine(result2);
public class Solution
{
    public int MinTimeToVisitAllPoints(int[][] points)
    {
        int time = 0;
        for (int i = 0; i < points.Length - 1; i++)
        {
            int diag = Math.Min(Math.Abs(points[i][0] - points[i + 1][0]), Math.Abs(points[i][1] - points[i + 1][1]));
            int straight = Math.Abs(points[i][0] - points[i + 1][0]) + Math.Abs(points[i][1] - points[i + 1][1]) - diag * 2;
            time += diag + straight;
        }
        return time;
    }
}
