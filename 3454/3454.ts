// Cheers to the post online:
// https://robert1003.github.io/2020/02/10/sweep-line-and-segment-tree.html
// It helped me understand the sweep line algorithm better.
function separateSquares(squares: number[][]): number {
    const sqs: [number, number, number][] = new Array(squares.length);
    for (let i = 0; i < squares.length; i++) {
        const s = squares[i];
        sqs[i] = [s[0], s[1], s[2]];
    }
    return splitYAtHalfArea(sqs);
}

type Square = [number, number, number];

// Let's just have a nice type for sweeping stuff
// this is like the defaultdict from the BestSolution() in python yesterday! (with a twist)
type SweepEvent = {
    y: number;
    x1: number;
    x2: number;
    delta: number;
};

// Segment Tree for counting covered lengths
// It's similar to what I implemented earlier (which is lost forever)
// but it is "class"-ified for better structure and easier optimization.
class SegmentTree {
    private xs: number[];
    private nSeg: number;
    private count: Int32Array;
    private covered: Float64Array;

    constructor(xs: number[]) {
        this.xs = xs;
        this.nSeg = xs.length - 1;
        const size = Math.max(1, this.nSeg) * 4;
        this.count = new Int32Array(size);
        this.covered = new Float64Array(size);
    }

    public totalCovered(): number {
        return this.covered[1];
    }

    public update(ql: number, qr: number, delta: number): void {
        if (ql > qr || this.nSeg <= 0) return;
        this.updateRec(1, 0, this.nSeg - 1, ql, qr, delta);
    }

    // I essentially transcribed this from my previous implementation
    // + a little AI boost to help optimize just that tiny bit I really needed to go from
    // 94% to 100% performance on LeetCode.
    private updateRec(node: number, l: number, r: number, ql: number, qr: number, delta: number): void {
        if (ql <= l && r <= qr) {
            this.count[node] += delta;
            this.pushUp(node, l, r);
            return;
        }
        const mid = (l + r) >> 1;
        if (ql <= mid) this.updateRec(node << 1, l, mid, ql, qr, delta);
        if (qr > mid) this.updateRec((node << 1) | 1, mid + 1, r, ql, qr, delta);
        this.pushUp(node, l, r);
    }

    private pushUp(node: number, l: number, r: number): void {
        if (this.count[node] > 0) {
            this.covered[node] = this.xs[r + 1] - this.xs[l];
        } else if (l === r) {
            this.covered[node] = 0;
        } else {
            this.covered[node] = this.covered[node << 1] + this.covered[(node << 1) | 1];
        }
    }
}

function lowerBound(arr: number[], target: number): number {
    let lo = 0,
        hi = arr.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (arr[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

function splitYAtHalfArea(squares: Square[]): number {
    const { events, xs } = buildEventsAndXs(squares);
    events.sort((a, b) => a.y - b.y);
    const total = (() => {
        const seg = new SegmentTree(xs);
        let area = 0;
        let i = 0;
        let prevY = events.length ? events[0].y : 0;

        while (i < events.length) {
            const curY = events[i].y;
            const dy = curY - prevY;
            if (dy !== 0) area += seg.totalCovered() * dy;

            while (i < events.length && events[i].y === curY) {
                const e = events[i];
                const l = lowerBound(xs, e.x1);
                const r = lowerBound(xs, e.x2);
                seg.update(l, r - 1, e.delta);
                i++;
            }
            prevY = curY;
        }
        return area;
    })();

    const half = total / 2;

    // find minimum y where prefix union area >= half
    const seg = new SegmentTree(xs);
    let area = 0;
    let i = 0;
    let prevY = events.length ? events[0].y : 0;

    while (i < events.length) {
        const curY = events[i].y;
        const dy = curY - prevY;
        const width = seg.totalCovered();

        if (dy !== 0) {
            const gain = width * dy;
            if (area + gain >= half) {
                if (width === 0) return prevY;
                return prevY + (half - area) / width;
            }
            area += gain;
        }

        while (i < events.length && events[i].y === curY) {
            const e = events[i];
            const l = lowerBound(xs, e.x1);
            const r = lowerBound(xs, e.x2);
            seg.update(l, r - 1, e.delta);
            i++;
        }
        prevY = curY;
    }

    return events.length ? events[0].y : 0;
}

function buildEventsAndXs(squares: Square[]): { events: SweepEvent[]; xs: number[] } {
    const events: SweepEvent[] = [];
    const xsRaw: number[] = [];

    for (const [x, y, len] of squares) {
        const x1 = x;
        const x2 = x + len;
        const y1 = y;
        const y2 = y + len;

        events.push({ y: y1, x1, x2, delta: +1 });
        events.push({ y: y2, x1, x2, delta: -1 });

        xsRaw.push(x1, x2);
    }

    xsRaw.sort((a, b) => a - b);
    const xs: number[] = [];
    for (let i = 0; i < xsRaw.length; i++) {
        if (i === 0 || xsRaw[i] !== xsRaw[i - 1]) xs.push(xsRaw[i]);
    }

    return { events, xs };
}

console.log(
    separateSquares([
        [0, 0, 1],
        [2, 2, 1],
    ])
);

console.log(
    separateSquares([
        [0, 0, 2],
        [1, 1, 1],
    ])
);

console.log(
    separateSquares([
        [5, 18, 12],
        [7, 23, 3],
        [7, 25, 7],
    ])
);

console.log(
    separateSquares([
        [639, 968, 150],
        [724, 925, 23],
        [438, 868, 55],
        [354, 712, 92],
        [923, 973, 92],
        [810, 920, 45],
        [637, 898, 283],
        [149, 961, 263],
        [111, 727, 17],
        [471, 590, 162],
    ])
);
