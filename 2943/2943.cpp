// Accepted: 01/15/2026
#include <bits/stdc++.h>
#include <vector>
using namespace std;
class Solution
{
  public:
    int maximizeSquareHoleArea(int n, int m, vector<int> &hBars, vector<int> &vBars)
    {
        // n -
        // m -
        // hBars -
        // vBars -
        // Grid has n + 2 horizontal and m + 2 vertical bars (1x1 unit cells).
        // Bars are indexed starting from 1.

        // ok i see now -- we have something like this:
        // n = 1, m = 3 -> hBars = [1,3,5], vBars = [1,3,5,7,9]
        // |--|--|--|--|
        // |  |  |  |  |
        // |--|--|--|--|
        // |  |  |  |  |
        // |--|--|--|--|
        quickSort(hBars, 0, hBars.size() - 1);
        quickSort(vBars, 0, vBars.size() - 1);
        int x = 0;
        int y = 0;
        int hx = 0;
        int hy = 0;
        for (int i = 1; i < hBars.size(); ++i)
        {
            if (hBars[i] - hBars[i - 1] == 1)
            {
                ++y;
            }
            else
            {
                if (y - x > hy - hx)
                {
                    hy = y;
                    hx = x;
                }
                x = i;
                y = i;
            }
        }

        if (y - x > hy - hx)
        {
            hy = y;
            hx = x;
        }
        x = y = 0;
        int vx = 0;
        int vy = 0;
        for (int i = 1; i < vBars.size(); ++i)
        {
            if (vBars[i] - vBars[i - 1] == 1)
            {
                ++y;
            }
            else
            {
                if (y - x > vy - vx)
                {
                    vy = y;
                    vx = x;
                }
                x = i;
                y = i;
            }
        }

        if (y - x > vy - vx)
        {
            vy = y;
            vx = x;
        }
        int width = min(hy - hx + 2, vy - vx + 2);
        return width * width;
    }

    int partition(vector<int> &vec, int low, int high)
    {

        // Selecting last element as the pivot
        int pivot = vec[high];

        // Index of elemment just before the last element
        // It is used for swapping
        int i = (low - 1);

        for (int j = low; j <= high - 1; j++)
        {

            // If current element is smaller than or
            // equal to pivot
            if (vec[j] <= pivot)
            {
                i++;
                swap(vec[i], vec[j]);
            }
        }

        // Put pivot to its position
        swap(vec[i + 1], vec[high]);

        // Return the point of partition
        return (i + 1);
    }

    void quickSort(vector<int> &vec, int low, int high)
    {

        // Base case: This part will be executed till the starting
        // index low is lesser than the ending index high
        if (low < high)
        {

            // pi is Partitioning Index, arr[p] is now at
            // right place
            int pi = partition(vec, low, high);

            // Separately sort elements before and after the
            // Partition Index pi
            quickSort(vec, low, pi - 1);
            quickSort(vec, pi + 1, high);
        }
    }
};

int main()
{
    Solution sol;
    int n = 2;
    int m = 1;
    vector<int> hBars = {1, 2, 4};
    vector<int> vBars = {2};

    int result = sol.maximizeSquareHoleArea(n, m, hBars, vBars);
    cout << result << endl;

    n = 1;
    m = 1;
    hBars = {2};
    vBars = {2};

    result = sol.maximizeSquareHoleArea(n, m, hBars, vBars);
    cout << result << endl;

    n = 2;
    m = 3;
    hBars = {2, 3};
    vBars = {2, 4};

    result = sol.maximizeSquareHoleArea(n, m, hBars, vBars);
    cout << result << endl;

    n = 3;
    m = 2;
    hBars = {3, 2, 4};
    vBars = {3, 2};

    result = sol.maximizeSquareHoleArea(n, m, hBars, vBars);
    cout << result << endl;

    return 0;
}