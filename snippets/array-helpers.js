// Small JavaScript helpers collected while keeping the daily log.
// Run: node snippets/array-helpers.js

const unique = (arr) => [...new Set(arr)];
const chunk = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (_, i) => arr.slice(i * size, i * size + size));
const sum = (arr) => arr.reduce((total, n) => total + n, 0);
const countBy = (arr, fn) =>
  arr.reduce((acc, x) => {
    const key = fn(x);
    acc[key] = (acc[key] || 0) + 1;
    return acc;
  }, {});

module.exports = { unique, chunk, sum, countBy };

if (require.main === module) {
  console.log(unique([1, 2, 2, 3]));            // [ 1, 2, 3 ]
  console.log(chunk([1, 2, 3, 4, 5], 2));       // [ [ 1, 2 ], [ 3, 4 ], [ 5 ] ]
  console.log(sum([1, 2, 3]));                  // 6
  console.log(countBy(['a', 'bb', 'cc'], (s) => s.length)); // { '1': 1, '2': 2 }
}
