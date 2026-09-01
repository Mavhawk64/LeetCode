function get_pairs(c1, c2) {
    const combos = [];

    for (let i = 0; i < c1.length; ++i) {
        for (let j = 0; j < c2.length; ++j) {
            combos.push(c1[i] + c2[j]);
        }
    }

    return combos;
}

var letterCombinations = function (digits) {
    const map = {
        // 1: ["1"],
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
        // 0: ["0"],
    };

    if (digits.length === 0) return [];

    let combos = map[digits[0]];

    for (let i = 1; i < digits.length; ++i) {
        combos = get_pairs(combos, map[digits[i]]);
    }

    return combos;
};

console.log(get_pairs("abc", "def"));
console.log(letterCombinations("3483"));
