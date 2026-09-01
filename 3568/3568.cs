// Accepted: 08/31/2026

public class Solution
{
    readonly (int Row, int Col)[] directions =
    [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ];

    private (
    (int Row, int Col) Student,
    (int Type, int LitterIndex)[][] Grid,
    int LitterCount
) GenerateGrid(string[] classroom)
    {
        var grid = new (int Type, int LitterIndex)[classroom.Length][];
        (int Row, int Col) student = (-1, -1);
        int litterCount = 0;

        for (int i = 0; i < classroom.Length; ++i)
        {
            grid[i] = new (int Type, int LitterIndex)[classroom[i].Length];

            for (int j = 0; j < classroom[i].Length; ++j)
            {
                switch (classroom[i][j])
                {
                    case 'S':
                        grid[i][j] = (0, -1);
                        student = (i, j);
                        break;

                    case 'L':
                        grid[i][j] = (1, litterCount++);
                        break;

                    case 'R':
                        grid[i][j] = (2, -1);
                        break;

                    case 'X':
                        grid[i][j] = (3, -1);
                        break;

                    default:
                        grid[i][j] = (0, -1);
                        break;
                }
            }
        }

        return (student, grid, litterCount);
    }

    private int BFS(
    (int Type, int LitterIndex)[][] grid,
    (int Row, int Col) root,
    int energy,
    int litterCount)
    {
        var Q = new Queue<(int Row, int Col, int Energy, int Moves, int Mask)>();

        int allLitter = (1 << litterCount) - 1;

        int[][][] bestEnergy = new int[grid.Length][][];

        for (int i = 0; i < grid.Length; ++i)
        {
            bestEnergy[i] = new int[grid[i].Length][];

            for (int j = 0; j < grid[i].Length; ++j)
            {
                bestEnergy[i][j] = new int[1 << litterCount];
                Array.Fill(bestEnergy[i][j], -1);
            }
        }

        bestEnergy[root.Row][root.Col][0] = energy;

        Q.Enqueue((root.Row, root.Col, energy, 0, 0));

        while (Q.Count > 0)
        {
            var (Row, Col, Energy, Moves, Mask) = Q.Dequeue();

            foreach (var (dr, dc) in directions)
            {
                int row = Row + dr;
                int col = Col + dc;

                if (row < 0 || row >= grid.Length)
                    continue;

                if (col < 0 || col >= grid[row].Length)
                    continue;

                if (grid[row][col].Type == 3)
                    continue;

                int nextEnergy = Energy - 1;

                if (nextEnergy < 0)
                    continue;

                if (grid[row][col].Type == 2)
                    nextEnergy = energy;

                int nextMask = Mask;

                if (grid[row][col].Type == 1)
                {
                    int litterIndex = grid[row][col].LitterIndex;
                    nextMask |= 1 << litterIndex;
                }

                if (nextMask == allLitter)
                    return Moves + 1;

                if (bestEnergy[row][col][nextMask] >= nextEnergy)
                    continue;

                bestEnergy[row][col][nextMask] = nextEnergy;

                Q.Enqueue((
                    row,
                    col,
                    nextEnergy,
                    Moves + 1,
                    nextMask
                ));
            }
        }

        return -1;
    }

    public int MinMoves(string[] classroom, int energy)
    {
        // S = 0, . = 0, L = 1, R = 2, X = 3
        var (student, grid, litterCount) = GenerateGrid(classroom);
        if (litterCount == 0) return 0;
        return BFS(grid, student, energy, litterCount);
    }
}