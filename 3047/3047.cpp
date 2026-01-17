// Accepted: 01/16/2026
#include <iostream>
#include <vector>
using namespace std;
class Solution
{
    struct Rect
    {
        int xL; // left
        int yB; // bottom
        int xR; // right
        int yT; // top
    };

  public:
    long long largestSquareArea(vector<vector<int>> &bottomLeft, vector<vector<int>> &topRight)
    {
        struct Rect
        {
            int xL, yB, xR, yT;
        };

        const int n = (int)bottomLeft.size();
        vector<Rect> rects;
        rects.reserve(n);

        for (int i = 0; i < n; ++i)
        {
            rects.push_back(Rect{bottomLeft[i][0], bottomLeft[i][1], topRight[i][0], topRight[i][1]});
        }

        long long maxArea = 0;

        for (int i = 0; i < n; ++i)
        {
            for (int j = i + 1; j < n; ++j)
            {
                int left = max(rects[i].xL, rects[j].xL);
                int right = min(rects[i].xR, rects[j].xR);
                int bottom = max(rects[i].yB, rects[j].yB);
                int top = min(rects[i].yT, rects[j].yT);

                int w = right - left;
                int h = top - bottom;
                if (w <= 0 || h <= 0)
                    continue;

                long long side = (long long)min(w, h);
                long long area = side * side;
                if (area > maxArea)
                    maxArea = area;
            }
        }
        return maxArea;
    }
};

int main()
{
    Solution sol;
    vector<vector<int>> bottomLeft = {{1, 1}, {2, 2}, {3, 1}};
    vector<vector<int>> topRight = {{3, 3}, {4, 4}, {6, 6}};
    long long result = sol.largestSquareArea(bottomLeft, topRight);

    cout << result << endl;

    return 0;
}