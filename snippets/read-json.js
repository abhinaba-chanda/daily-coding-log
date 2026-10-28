// Read and pretty-print a JSON file. Run: node snippets/read-json.js file.json
const fs = require("node:fs");

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, "utf8"));
}

module.exports = { readJson };

if (require.main === module && process.argv[2]) {
  console.log(JSON.stringify(readJson(process.argv[2]), null, 2));
}
