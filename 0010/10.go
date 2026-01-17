// Accepted: 01/17/2026
package main

func isMatch(s string, p string) bool {
	// . -> any single character
	// * -> zero or more of the preceding element
	// .* -> zero or more of any character
	i, j := 0, 0
	for i < len(s) && j < len(p) {
		if j+1 < len(p) && p[j+1] == '*' {
			// we have a wildcard in the next slot
			if p[j] == '.' {
				// Let's just separate this case, since it's so COOL.
				// recall that .* is the super wildcard that can match anything
				for k := i; k <= len(s); k++ {
					// try all possible lengths for .*
					if isMatch(s[k:], p[j+2:]) {
						// found a match
						return true
					}
				}
				// no match found -> exit / recurse up
				return false
			} else {
				// ok now in the last character, we had a normal character
				// e.g., a*
				// similar to before, but we don't have to recurse, we can just check the same character
				for k := i; k <= len(s); k++ {
					if k > i && s[k-1] != p[j] {
						break
					}
					if isMatch(s[k:], p[j+2:]) {
						return true
					}
				}
				return false
			}
		} else if p[j] == '.' || s[i] == p[j] {
			// Finally, we just check if we have a single character
			// or an exact match (a = a -> ok, a != b -> bad, . = any -> ok)
			i++
			j++
		} else {
			// no match -> exit / recurse up
			return false
		}
	}
	// Check for remaining characters in pattern
	// silly edge case (well really just end* case instead!)
	for j+1 < len(p) && p[j+1] == '*' {
		j += 2
	}
	return i == len(s) && j == len(p)
}

// Call the function with some test cases
// "aa"
// "a"
// "aa"
// "a*"
// "ab"
// ".*"

func main() {
	println(isMatch("aa", "a"))
	println(isMatch("aa", "a*"))
	println(isMatch("ab", ".*"))
}
