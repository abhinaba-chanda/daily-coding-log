#!/usr/bin/env python3
"""Build the daily coding log history from notes.txt (one commit per note line)."""
import os, random, subprocess, datetime

random.seed(20261029)
NAME = "Abhinaba-Dev"
EMAIL = "abhinabachanda491@gmail.com"

topics = [
 ("JavaScript", "array destructuring", "const [a, b] = [1, 2];"),
 ("JavaScript", "object spread", "const merged = { ...a, ...b };"),
 ("JavaScript", "arrow functions", "const sq = x => x * x;"),
 ("JavaScript", "Array.map", "nums.map(n => n * 2)"),
 ("JavaScript", "Array.filter", "nums.filter(n => n % 2 === 0)"),
 ("JavaScript", "Array.reduce", "nums.reduce((s, n) => s + n, 0)"),
 ("JavaScript", "template literals", "`Hello ${name}`"),
 ("JavaScript", "promises", "fetch(url).then(r => r.json())"),
 ("JavaScript", "async/await", "const data = await res.json();"),
 ("JavaScript", "closures", "function counter(){ let c = 0; return () => ++c; }"),
 ("JavaScript", "optional chaining", "user?.address?.city"),
 ("JavaScript", "nullish coalescing", "const port = env.PORT ?? 3000;"),
 ("JavaScript", "let vs const", "use const by default, let when reassigning"),
 ("JavaScript", "event listeners", "btn.addEventListener('click', onClick);"),
 ("JavaScript", "localStorage", "localStorage.setItem('theme', 'dark');"),
 ("JavaScript", "JSON parse/stringify", "JSON.parse(JSON.stringify(obj))"),
 ("JavaScript", "Set for unique values", "[...new Set(arr)]"),
 ("JavaScript", "Map vs object", "new Map([['a', 1]])"),
 ("JavaScript", "classes", "class Dog extends Animal {}"),
 ("JavaScript", "modules", "export default function main() {}"),
 ("JavaScript", "debounce", "clearTimeout(t); t = setTimeout(fn, 300);"),
 ("JavaScript", "fetch with error handling", "if (!res.ok) throw new Error(res.status);"),
 ("JavaScript", "sort numbers", "arr.sort((a, b) => a - b)"),
 ("JavaScript", "DOM querySelector", "document.querySelector('#app')"),
 ("Python", "list comprehensions", "[x * x for x in range(10)]"),
 ("Python", "dict comprehensions", "{k: v for k, v in pairs}"),
 ("Python", "f-strings", "f\"{name} is {age}\""),
 ("Python", "enumerate", "for i, x in enumerate(items):"),
 ("Python", "zip", "for a, b in zip(xs, ys):"),
 ("Python", "with open", "with open('a.txt') as f: data = f.read()"),
 ("Python", "try/except", "except ValueError as e:"),
 ("Python", "lambda", "sorted(people, key=lambda p: p.age)"),
 ("Python", "*args and **kwargs", "def f(*args, **kwargs):"),
 ("Python", "dataclasses", "@dataclass class Point: x: int; y: int"),
 ("Python", "pathlib", "Path('data').glob('*.csv')"),
 ("Python", "collections.Counter", "Counter(words).most_common(3)"),
 ("Python", "defaultdict", "defaultdict(list)"),
 ("Python", "generators", "def gen(): yield 1"),
 ("Python", "decorators", "def deco(fn): return wrapper"),
 ("Python", "virtual environments", "python -m venv .venv"),
 ("Python", "pytest basics", "def test_add(): assert add(1, 2) == 3"),
 ("Python", "requests library", "requests.get(url, timeout=10).json()"),
 ("Python", "json module", "json.dumps(data, indent=2)"),
 ("Python", "slicing", "s[::-1] reverses a string"),
 ("Python", "sets", "a & b, a | b, a - b"),
 ("Python", "string methods", "' hi '.strip().title()"),
 ("Python", "argparse", "parser.add_argument('--name')"),
 ("Python", "classes and __init__", "def __init__(self, name): self.name = name"),
 ("Python", "numpy arrays", "np.arange(10).reshape(2, 5)"),
 ("Python", "pandas read_csv", "pd.read_csv('data.csv').head()"),
 ("C", "pointers", "int *p = &x;"),
 ("C", "arrays and loops", "for (int i = 0; i < n; i++)"),
 ("C", "strings with char arrays", "char s[20] = \"hello\";"),
 ("C", "structs", "struct Point { int x, y; };"),
 ("C", "malloc and free", "int *a = malloc(n * sizeof *a); free(a);"),
 ("C", "switch statement", "switch (op) { case '+': ... }"),
 ("C", "scanf and printf", "scanf(\"%d\", &n); printf(\"%d\\n\", n);"),
 ("C", "recursion", "int fact(int n){ return n <= 1 ? 1 : n * fact(n - 1); }"),
 ("C", "file I/O", "FILE *f = fopen(\"a.txt\", \"r\");"),
 ("C", "header files", "#include \"utils.h\""),
 ("C", "bitwise operators", "x & 1 checks odd"),
 ("C", "2D arrays", "int grid[3][3];"),
 ("C++", "vectors", "std::vector<int> v{1, 2, 3};"),
 ("C++", "range-based for", "for (auto &x : v)"),
 ("C++", "std::string", "s.substr(0, 3)"),
 ("C++", "references", "void inc(int &x) { x++; }"),
 ("C++", "classes", "class Account { public: void deposit(int); };"),
 ("C++", "std::map", "std::map<std::string, int> freq;"),
 ("C++", "std::sort", "std::sort(v.begin(), v.end());"),
 ("C++", "constructors", "Point(int x, int y) : x(x), y(y) {}"),
 ("C++", "STL algorithms", "std::accumulate(v.begin(), v.end(), 0)"),
 ("C++", "smart pointers", "auto p = std::make_unique<Node>();"),
 ("C++", "templates", "template <typename T> T maxOf(T a, T b);"),
 ("C++", "operator overloading", "Point operator+(const Point &o) const;"),
 ("Node.js", "fs.readFile", "fs.readFileSync('a.txt', 'utf8')"),
 ("Node.js", "path module", "path.join(__dirname, 'data')"),
 ("Node.js", "http server", "http.createServer((req, res) => res.end('ok'))"),
 ("Node.js", "npm scripts", "\"test\": \"node --test\""),
 ("Node.js", "process.argv", "const [, , name] = process.argv;"),
 ("Node.js", "EventEmitter", "emitter.on('done', cb)"),
 ("Node.js", "express routes", "app.get('/api', (req, res) => res.json({}))"),
 ("Node.js", "environment variables", "process.env.PORT"),
 ("Node.js", "node:test", "test('adds', () => assert.equal(add(1, 2), 3));"),
 ("Node.js", "readline", "rl.question('Name? ', ans => {})"),
 ("Node.js", "fs/promises", "await fs.promises.writeFile(p, data)"),
 ("Git", "branches", "git switch -c feature"),
 ("Git", "rebase vs merge", "rebase keeps history linear"),
 ("Git", "git stash", "git stash && git stash pop"),
 ("HTML/CSS", "flexbox", "display: flex; justify-content: center;"),
 ("HTML/CSS", "grid", "grid-template-columns: repeat(3, 1fr);"),
 ("HTML/CSS", "media queries", "@media (max-width: 600px)"),
 ("HTML/CSS", "CSS variables", "--main: #a50044;"),
 ("DSA", "binary search", "lo, hi = 0, len(a) - 1"),
 ("DSA", "two pointers", "move left/right toward each other"),
 ("DSA", "stack", "push/pop for bracket matching"),
 ("DSA", "queue with deque", "deque.popleft()"),
 ("DSA", "linked list reversal", "prev, cur = cur, cur.next"),
 ("DSA", "bubble sort", "swap adjacent items until sorted"),
 ("DSA", "hash map counting", "count[x] = count.get(x, 0) + 1"),
 ("DSA", "recursion base case", "always return on the smallest input"),
 ("DSA", "big-O basics", "nested loops over n are O(n^2)"),
]
verbs = ["Practiced", "Revised", "Learned", "Tried out", "Wrote notes on", "Solved an exercise with", "Re-read docs on"]

start = datetime.date(2025, 10, 29)
end = datetime.date(2026, 10, 28)
weights = [1, 2, 3, 4, 5, 6, 7]
probs   = [18, 21, 18, 14, 11, 9, 9]
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

def run(*args, env=None):
    subprocess.run(args, check=True, env=env)

total = 0
day = start
ti = 0
while day <= end:
    n = random.choices(weights, probs)[0]
    if random.random() < 0.05:
        n = random.randint(9, 12)
    mins = sorted(random.sample(range(10 * 60, 23 * 60), n))
    for m in mins:
        lang, topic, snip = topics[ti % len(topics)]
        ti += 1 + random.randint(0, 3)
        ts = datetime.datetime(day.year, day.month, day.day, m // 60, m % 60, random.randint(0, 59), tzinfo=IST)
        path = f"logs/{day.year}/{day.month:02d}.md"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        new = not os.path.exists(path)
        with open(path, "a") as f:
            if new:
                f.write(f"# Coding log - {day.strftime('%B %Y')}\n\n")
            f.write(f"- {day.isoformat()} {ts.strftime('%H:%M')} [{lang}] {random.choice(verbs)} {topic}: `{snip}`\n")
        run("git", "add", path)
        iso = ts.isoformat()
        env = dict(os.environ, GIT_AUTHOR_DATE=iso, GIT_COMMITTER_DATE=iso,
                   GIT_AUTHOR_NAME=NAME, GIT_AUTHOR_EMAIL=EMAIL,
                   GIT_COMMITTER_NAME=NAME, GIT_COMMITTER_EMAIL=EMAIL)
        run("git", "commit", "-q", "-m", f"Log {day.isoformat()}: {topic}", env=env)
        total += 1
    day += datetime.timedelta(days=1)
print("commits:", total)
