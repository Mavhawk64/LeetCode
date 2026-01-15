// Accepted: 01/14/2026

var cantor = (a, b) => {
    return Math.floor(((a + b + 1) * (a + b)) / 2) + b;
};

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
    if (numRows === 1 || s.length <= numRows) return s;
    // my original attempt was to try and map/encode the 2D coordinates
    // into a 1D index using the Cantor pairing function, but it didn't quite
    // work out as I hoped. Leaving the code here for the year 2030.
    // for (var i = 0; i < s.length; ++i) {
    //     var x = i % numRows;
    //     var y = Math.floor(i / numRows);
    //     var c = cantor(y, x);
    //     console.log(s[i], x, y, c);
    // }

    // Ok let's just go column by column (I think... or maybe it's row by row... idk)
    const grid = Array.from({ length: numRows }, () => []); // Just make a blank 2D array
    // After playing around in my notebook for a while, I found a pattern:
    let pattern = 2 * numRows - 2; // The length of one full zigzag pattern
    for (let i = 0; i < s.length; ++i) {
        let pointer = i % pattern;
        let gridPoint = pointer < numRows ? pointer : pattern - pointer;
        grid[gridPoint].push(s[i]);
    }
    // so in rust, I think I would do something like:
    // grid.iter().map(|r| r.iter().collect::<String>()).collect::<String>() and just return that
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map
    // ok so basically the same thing... join everything inside as a string, then join all that as a big string.
    return grid.map((row) => row.join("")).join("");
};

console.log(convert("PAYPALISHIRING", 3));
