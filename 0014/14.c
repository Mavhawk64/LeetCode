// Accepted: 01/17/2026
char *build_str_prefix(const char *, int);
int str_cmp_prefix(const char *, const char *, int);

char *longestCommonPrefix(char **strs, int strsSize)
{
    // idea: the biggest common prefix cannot be longer than the first string
    // ... or the shortest string!
    int minLen = strlen(
        strs[0]); // we can just subtract at each element. if 0, return 0, else return minLen after continuing to end.
    for (int i = 1; i < strsSize; i++)
    {
        int currLen = str_cmp_prefix(strs[0], strs[i], minLen);
        if (currLen < minLen)
        {
            minLen = currLen;
        }

        if (minLen == 0)
        {
            return "";
        }
    }
    return build_str_prefix(strs[0], minLen);
}

char *build_str_prefix(const char *s, int len)
{
    char *res = (char *)malloc((len + 1) * sizeof(char));
    for (int i = 0; i < len; i++)
    {
        res[i] = s[i];
    }
    res[len] = '\0';
    return res;
}

int str_cmp_prefix(const char *s1, const char *s2, int maxLen)
{
    for (int i = 0; i < maxLen; i++)
    {
        if (s1[i] != s2[i])
        {
            return i;
        }
    }
    return maxLen;
}