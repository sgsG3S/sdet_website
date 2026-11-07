import json

# Comprehensive 84-Day Dataset: From Absolute Python Basics to Senior Remote SDET (₹20 LPA)
days_data = [
    # =========================================================================
    # MODULE 1: PYTHON FROM SCRATCH TO ADVANCED OOP (DAYS 1 - 14)
    # =========================================================================
    {
        "day": 1, "week": 1, "month": 1, "category": "Python Basics",
        "title": "Python Setup, Environment & Primitive Types",
        "concepts": ["Python runtime & bytecode (.pyc)", "Virtual environments (venv)", "Primitive types: int, float, str, bool, NoneType", "Type conversion & dynamic typing"],
        "assignment": "Set up a Python 3.12+ project with a virtual environment. Write a script demonstrating type casting, memory id checks (id()), and type inspection using type() and isinstance().",
        "deliverable": "python-foundations/day01_types_and_env.py",
        "interviewQ": "Why is Python described as dynamically typed yet strongly typed, and how does this affect test assertions?",
        "interviewAns": "Python is dynamically typed because variable types are determined at runtime without explicit declaration, but strongly typed because it will not implicitly coerce incompatible types (e.g., '5' + 5 raises a TypeError).",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 2, "week": 1, "month": 1, "category": "Python Basics",
        "title": "Control Flow, Conditionals & Truthiness",
        "concepts": ["if / elif / else branching", "Truthy & Falsy values in Python", "Short-circuit evaluation (and / or)", "Pattern matching (match / case) introduced in Python 3.10"],
        "assignment": "Build a CLI evaluation script that checks HTTP status code ranges (2xx, 3xx, 4xx, 5xx) using structural pattern matching (match/case) and truthiness validation.",
        "deliverable": "python-foundations/day02_control_flow.py",
        "interviewQ": "What values in Python evaluate to Falsy, and how can testing for 'if response:' lead to subtle assertion bugs?",
        "interviewAns": "Falsy values include None, False, 0, 0.0, empty sequences/collections ('', [], (), {}, set()). Checking 'if response:' fails if a valid API returns an empty list [] or 0 count, mistaking a valid empty payload for failure.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 3, "week": 1, "month": 1, "category": "Python Basics",
        "title": "Loops, Iterations & Loop Controls",
        "concepts": ["for in loops and iterables", "while loops & condition bounds", "break, continue, and loop else clauses", "range() generator mechanics"],
        "assignment": "Implement a retry polling simulation with a while loop that retries an operation up to 5 times with incrementing delays, utilizing the 'else' block for successful completion.",
        "deliverable": "python-foundations/day03_loops_and_polling.py",
        "interviewQ": "When does the 'else' block of a Python for or while loop execute?",
        "interviewAns": "The 'else' block executes ONLY when the loop terminates naturally without hitting a 'break' statement. It is ideal for search or retry loops where no early exit occurred.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 4, "week": 1, "month": 1, "category": "Python Basics",
        "title": "Strings Mastery, Slicing & Formatting",
        "concepts": ["String slicing syntax [start:stop:step]", "String methods: split, join, strip, replace, startswith", "f-strings & format specs", "Regex basics (re module) for pattern extraction"],
        "assignment": "Write a string utility that parses complex error log lines, extracts timestamps, log levels (INFO/WARN/ERROR), and extracts UUID correlation IDs using regex.",
        "deliverable": "python-foundations/day04_strings_and_regex.py",
        "interviewQ": "How does string immutability in Python impact memory performance, and why is ''.join(list) preferred over string concatenation (+)?",
        "interviewAns": "Strings are immutable; using '+' in a loop creates a new string object and copies memory every iteration, resulting in O(N^2) complexity. ''.join(list) calculates total memory upfront and copies once in O(N).",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 5, "week": 1, "month": 1, "category": "Python Basics",
        "title": "Lists, Tuples & Memory Immutability",
        "concepts": ["Lists (dynamic arrays, append, extend, pop, insert)", "Tuples (immutability, packing/unpacking)", "Shallow copy vs Deep copy (copy module)", "Pass-by-object-reference"],
        "assignment": "Create a data manipulation module demonstrating list operations, in-place sorting vs sorted(), tuple unpacking for test parameters, and deep copying of nested structures.",
        "deliverable": "python-foundations/day05_lists_and_tuples.py",
        "interviewQ": "What is the difference between shallow copy (copy.copy) and deep copy (copy.deepcopy), and how can a shallow copy contaminate Pytest fixture data?",
        "interviewAns": "Shallow copy duplicates the outer container but keeps references to nested mutable objects. If multiple tests share a shallow-copied fixture with nested dicts, mutating a nested dict in Test A contaminates Test B.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 6, "week": 1, "month": 1, "category": "Python Basics",
        "title": "Dictionaries & Sets: Hashing & Fast Lookups",
        "concepts": ["Dictionary hashing (O(1) lookups)", "dict methods: get, setdefault, items, values", "collections.defaultdict & Counter", "Sets and set theory (union, intersection, difference)"],
        "assignment": "Write a test result reconciliation tool using Sets and Dictionaries to compare Expected vs Actual test IDs, instantly finding missing, unexpected, and duplicate tests.",
        "deliverable": "python-foundations/day06_dicts_and_sets.py",
        "interviewQ": "Why must dictionary keys and set elements be hashable, and why can a list not be used as a dictionary key?",
        "interviewAns": "Dicts and sets use hash tables for O(1) lookups. Keys must be immutable so their hash value remains constant. Lists are mutable and can change, which would corrupt hash table lookups.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 7, "week": 1, "month": 1, "category": "Python Basics",
        "title": "Comprehensions & Built-In Power Functions",
        "concepts": ["List, dict, and set comprehensions", "Filtering with comprehensions", "enumerate() and zip()", "any(), all(), sorted() with key lambda"],
        "assignment": "Refactor nested parsing loops into clean, idiomatic list and dictionary comprehensions. Use all() and any() to build a health-check assertion function for multiple microservices.",
        "deliverable": "python-foundations/day07_comprehensions.py",
        "interviewQ": "How do all() and any() utilize short-circuit evaluation, and how can they optimize test assertion pipelines?",
        "interviewAns": "all() halts and returns False at the first falsy item without checking the rest; any() halts and returns True at the first truthy item. This saves execution time when validating large collections of assertions.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 8, "week": 2, "month": 1, "category": "Python Intermediate",
        "title": "Functions, Scopes & Parameter Packing (*args, **kwargs)",
        "concepts": ["def syntax, return values, type hints", "Positional, keyword-only, and default arguments", "*args and **kwargs parameter packing", "LEGB variable scope (Local, Enclosing, Global, Built-in)"],
        "assignment": "Build a universal assertion logger function that accepts variable arguments (*args) and keyword parameters (**kwargs) to dynamically inspect and log test metadata.",
        "deliverable": "python-foundations/day08_functions_and_scope.py",
        "interviewQ": "Why is using a mutable default argument like 'def add_test(test_id, tags=[])' a catastrophic bug in Python?",
        "interviewAns": "Default arguments are evaluated once at function definition time, NOT at runtime call time. The same list instance persists across all calls, accumulating state between invocations.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 9, "week": 2, "month": 1, "category": "Python Intermediate",
        "title": "File Handling, JSON Serialization & Pathlib",
        "concepts": ["with open() context manager", "Reading & writing text, CSV, and JSON files", "json.loads(), json.dumps(), json.load(), json.dump()", "pathlib.Path for cross-platform OS paths"],
        "assignment": "Build a dynamic test configuration loader that reads from both JSON and CSV test-data files using pathlib.Path, validating data structures before returning them.",
        "deliverable": "python-foundations/day09_file_io_and_json.py",
        "interviewQ": "Why is pathlib.Path strongly preferred over os.path in modern cross-platform test automation frameworks?",
        "interviewAns": "pathlib provides an object-oriented API that automatically handles forward and backward slash path separators correctly across Windows, Linux, and macOS, preventing CI path-resolution bugs.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 10, "week": 2, "month": 1, "category": "Python Intermediate",
        "title": "Exception Handling & Custom Error Hierarchies",
        "concepts": ["try, except, else, finally blocks", "Handling multiple exception types", "Exception chaining (raise ... from ...)", "Building custom FrameworkException hierarchies"],
        "assignment": "Design a complete test framework exception hierarchy: BaseFrameworkError -> APIError, UIElementTimeoutError, DatabaseConnectionError, complete with contextual error attributes.",
        "deliverable": "python-foundations/day10_exceptions.py",
        "interviewQ": "What is the purpose of 'raise NewException from original_exception' and why is it vital for CI debugging?",
        "interviewAns": "It chains exceptions by attaching the original exception to the __cause__ attribute, preserving the original stack trace so engineers can see both the framework failure and the underlying system crash in CI logs.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 11, "week": 2, "month": 1, "category": "Python OOP",
        "title": "OOP Fundamentals: Classes, Instances & Attributes",
        "concepts": ["class keyword, __init__ constructor, self reference", "Instance attributes vs Class attributes", "Methods vs Functions", "Instantiating test objects"],
        "assignment": "Implement a TestCase and TestSuite class from scratch that tracks execution status, execution duration, and failure logs without using external libraries.",
        "deliverable": "python-foundations/day11_oop_classes.py",
        "interviewQ": "What is the difference between an instance attribute and a class attribute, and how can an accidental class attribute cause race conditions in parallel tests?",
        "interviewAns": "Class attributes are shared across all instances of that class. If multiple parallel test threads or processes modify a class attribute, they overwrite each other's data causing flaky tests. Instance attributes remain strictly bound to self.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 12, "week": 2, "month": 1, "category": "Python OOP",
        "title": "OOP Inheritance, Polymorphism & Encapsulation",
        "concepts": ["Single and multi-level inheritance", "super() method resolution", "Encapsulation: public, protected (_), and private (__) with name mangling", "Polymorphism through shared interfaces"],
        "assignment": "Create a BasePage class with common interactions (click, type, wait_for_element) inherited by LoginPage and DashboardPage, demonstrating clean encapsulation and method overriding.",
        "deliverable": "python-foundations/day12_oop_inheritance.py",
        "interviewQ": "Why is composition favored over deep inheritance hierarchies in enterprise test framework design?",
        "interviewAns": "Deep inheritance creates rigid coupling where base class changes break child classes. Composition allows assembling small, independent components (e.g. injecting DBClient, APIClient, Logger) flexibly without fragile hierarchies.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 13, "week": 2, "month": 1, "category": "Python OOP",
        "title": "Advanced OOP: Dunder Methods, @property & Classmethods",
        "concepts": ["Magic/dunder methods: __repr__, __str__, __len__, __eq__", "@property getters & setters for data validation", "@classmethod and @staticmethod use cases", "Abstract Base Classes (abc.ABC, @abstractmethod)"],
        "assignment": "Build an AbstractBaseClient using abc.ABC with abstract methods (authenticate, get, post). Implement concrete RestClient and GraphqlClient with custom __str__ and __eq__ logic.",
        "deliverable": "python-foundations/day13_oop_dunders.py",
        "interviewQ": "When should you use @classmethod vs @staticmethod in an automation framework utility class?",
        "interviewAns": "@classmethod receives the class 'cls' and is ideal for alternative factory constructors (e.g. from_json or from_env). @staticmethod does not receive self or cls and serves as a pure helper function namespace.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 14, "week": 2, "month": 1, "category": "Python Advanced",
        "title": "Custom Decorators & Python Packaging",
        "concepts": ["Function closures & higher-order functions", "Writing parameterized decorators with @functools.wraps", "Writing a production @retry decorator with exponential backoff", "pyproject.toml basics"],
        "assignment": "Write a production-grade @retry decorator with exponential backoff, jitter, and selective exception handling. Write comprehensive unit tests proving it retries N times and bubbles the original error.",
        "deliverable": "python-foundations/day14_decorators_and_packaging.py",
        "interviewQ": "What happens if you omit @functools.wraps inside a decorator used on test functions?",
        "interviewAns": "The wrapped function loses its identity (__name__, __doc__, __module__), causing pytest to report wrapper function names in test outputs and breaking introspection plugins.",
        "timebox": "Theory: 1.0h | Coding: 3.5h | Katas: 1.5h"
    },

    # =========================================================================
    # MODULE 2: TESTING FUNDAMENTALS & PYTEST ENGINE (DAYS 15 - 26)
    # =========================================================================
    {
        "day": 15, "week": 3, "month": 1, "category": "Testing Fundamentals",
        "title": "Testing Theory, SDLC/STLC & Test Pyramid",
        "concepts": ["SDLC vs STLC phases", "The Test Pyramid: Unit vs Integration vs Contract vs E2E UI", "Defect Lifecycle, Severity vs Priority", "Root Cause Analysis (RCA) 5-Whys methodology"],
        "assignment": "Draft a formal Root Cause Analysis (RCA) document for a simulated production outage, identifying why automated regression missed the bug and defining actionable prevention steps.",
        "deliverable": "testing-fundamentals/rca_production_leakage.md",
        "interviewQ": "Explain why an inverted test pyramid (ice cream cone anti-pattern) causes CI failure rates to skyrocket.",
        "interviewAns": "Over-relying on UI tests results in high execution time, expensive maintenance, and high flakiness due to DOM/network jitter. Shifting checks down to unit, API, and contract layers provides faster, deterministic feedback.",
        "timebox": "Theory: 2.5h | Coding: 2.0h | Katas: 1.0h"
    },
    {
        "day": 16, "week": 3, "month": 1, "category": "Testing Fundamentals",
        "title": "Test Design Techniques: BVA, ECP & Decision Tables",
        "concepts": ["Equivalence Class Partitioning (ECP)", "Boundary Value Analysis (BVA: 2-value vs 3-value)", "Decision Table testing for business rules", "State Transition Testing"],
        "assignment": "Design a complete test matrix for a complex discount & loan eligibility engine using Equivalence Partitioning, 3-value BVA, and a Decision Table.",
        "deliverable": "testing-fundamentals/test_design_matrix.xlsx",
        "interviewQ": "What is the difference between 2-value and 3-value Boundary Value Analysis?",
        "interviewAns": "2-value BVA tests the exact boundary and the immediate invalid value outside (e.g. for max 100: 100, 101). 3-value BVA tests below the boundary, the boundary, and above the boundary (e.g. 99, 100, 101), catching off-by-one errors.",
        "timebox": "Theory: 2.5h | Coding: 2.0h | Katas: 1.0h"
    },
    {
        "day": 17, "week": 3, "month": 1, "category": "Testing Fundamentals",
        "title": "Test Planning, RTM & Risk-Based Testing",
        "concepts": ["Drafting an SDET Master Test Plan", "Requirements Traceability Matrix (RTM)", "Risk-Based Testing (Likelihood vs Impact scoring)", "Test Estimation techniques"],
        "assignment": "Create a comprehensive Master Test Plan and Risk Matrix for an e-commerce checkout microservice, mapping user stories to automated test types.",
        "deliverable": "testing-fundamentals/master_test_plan.md",
        "interviewQ": "How do you apply Risk-Based Testing when an engineering manager cuts regression execution time by 50% before a release?",
        "interviewAns": "Calculate Risk Priority Numbers (Likelihood x Impact). Execute P0 critical revenue-impacting tests and high-frequency defect paths first, deferring low-impact edge cases and cosmetic checks to post-release.",
        "timebox": "Theory: 2.5h | Coding: 2.0h | Katas: 1.0h"
    },
    {
        "day": 18, "week": 3, "month": 1, "category": "Pytest Engine",
        "title": "Pytest Essentials: Discovery, Assertions & Flags",
        "concepts": ["Pytest test discovery conventions (test_*.py, Test*, test_*)", "Python native assert statement & assertion introspection", "CLI options: -v, -s, -k, -m, -x, --maxfail", "Exit codes interpretation"],
        "assignment": "Write a suite of 15 tests verifying mathematical, string, and collection properties. Run tests with varying CLI flags and analyze Pytest's rich assertion difference outputs.",
        "deliverable": "pytest-blueprint/tests/test_pytest_essentials.py",
        "interviewQ": "How does Pytest's assertion rewriting work under the hood without requiring custom assert helper functions like unittest?",
        "interviewAns": "Pytest intercepts Python's abstract syntax tree (AST) during module import, rewriting standard 'assert' statements to capture sub-expression values, providing detailed failure diffs without boilerplate assert methods.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 19, "week": 3, "month": 1, "category": "Pytest Engine",
        "title": "Pytest Fixtures: Setup, Teardown & Yield",
        "concepts": ["@pytest.fixture anatomy", "Setup and teardown execution with yield", "Passing fixtures to tests & other fixtures", "request fixture & introspection"],
        "assignment": "Create a temporary directory fixture that creates mock config files before tests and guarantees cleanup in the teardown phase even when assertions fail.",
        "deliverable": "pytest-blueprint/tests/test_fixtures_basic.py",
        "interviewQ": "What guarantees that fixture code after the 'yield' statement will execute even if the test fails?",
        "interviewAns": "Pytest wraps the fixture execution in an internal try/finally block. When a test raises an AssertionError or exception, Pytest still enters the finally block to execute post-yield teardown.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 20, "week": 3, "month": 1, "category": "Pytest Engine",
        "title": "Fixture Scopes in Depth & Autouse",
        "concepts": ["Fixture scopes: function, class, module, package, session", "autouse=True fixtures and their hidden risks", "Fixture execution ordering", "Parameterized fixtures"],
        "assignment": "Design a multi-tier fixture system: session scope boots a mock server, module scope opens database connections, function scope creates clean isolated test records.",
        "deliverable": "pytest-blueprint/tests/test_fixture_scopes.py",
        "interviewQ": "Why is using session-scoped fixtures with mutable state across parallel test processes dangerous?",
        "interviewAns": "In parallel execution (pytest-xdist), tests in different workers run concurrently. Mutating shared session data leads to non-deterministic race conditions and test order dependencies.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 21, "week": 3, "month": 1, "category": "Pytest Engine",
        "title": "conftest.py Hierarchies & Fixture Overriding",
        "concepts": ["Root conftest.py vs sub-directory conftest.py", "Nearest-scope fixture discovery rules", "Fixture overriding for specific microservices", "Sharing fixtures cleanly"],
        "assignment": "Build a test folder hierarchy with root and nested conftest.py files demonstrating how staging vs production environment settings override cleanly without code duplication.",
        "deliverable": "pytest-blueprint/services/billing/conftest.py",
        "interviewQ": "How does Pytest resolve fixture discovery when two conftest.py files define a fixture with the exact same name?",
        "interviewAns": "Pytest follows nearest-scope discovery: it starts in the test file's directory, checking local conftest.py first, then traverses up parent directories to the root conftest.py.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 22, "week": 4, "month": 1, "category": "Pytest Engine",
        "title": "Advanced Parametrization & Dynamic Test IDs",
        "concepts": ["@pytest.mark.parametrize on functions & classes", "Indirect parametrization (indirect=True)", "Custom test naming with ids=callable", "pytest_generate_tests hook"],
        "assignment": "Create a boundary test suite reading test vectors dynamically from external JSON/CSV, generating 25 parametrized tests with human-readable test names in CLI reports.",
        "deliverable": "pytest-blueprint/tests/test_advanced_parametrization.py",
        "interviewQ": "When and why should you use indirect parametrization over standard direct parametrization?",
        "interviewAns": "Indirect parametrization passes parameters into a fixture first instead of directly to the test. This allows fixtures to perform dynamic setup logic (like DB seeding or browser configuration) conditioned on the parameter value.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 23, "week": 4, "month": 1, "category": "Pytest Engine",
        "title": "Pytest Markers, CLI Switches & pytest.ini",
        "concepts": ["Custom markers registration in pytest.ini", "Enforcing --strict-markers", "Filtering tests with -m 'smoke and not slow'", "Adding custom CLI options via pytest_addoption"],
        "assignment": "Configure pytest.ini with custom markers (smoke, regression, flakiness_quarantine) and write a custom conftest hook adding --env and --headless CLI switches.",
        "deliverable": "pytest-blueprint/pytest.ini",
        "interviewQ": "Why is enforcing --strict-markers critical in enterprise test pipelines?",
        "interviewAns": "Without --strict-markers, typos in marker decorators (e.g. @pytest.mark.smokke) are silently ignored as warnings by Pytest, causing critical tests to be skipped in CI runs without alerting anyone.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 24, "week": 4, "month": 1, "category": "Pytest Engine",
        "title": "Pytest Hooks & Failure Telemetry",
        "concepts": ["pytest_runtest_makereport hook", "Inspecting CallInfo execution outcomes", "Measuring test run duration", "Extracting local stack variables on failure"],
        "assignment": "Implement a custom hook in conftest.py that captures failing test frames, calculates exact execution duration, and logs local variables of the failing line for CI triage.",
        "deliverable": "pytest-blueprint/plugins/failure_capture.py",
        "interviewQ": "How do you access the test outcome (pass/fail/skip) inside a pytest fixture's teardown phase?",
        "interviewAns": "Implement the pytest_runtest_makereport hook in conftest.py to attach the execution report to the request.node object, which fixtures can inspect via request.node.rep_call.failed.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 25, "week": 4, "month": 1, "category": "Pytest Engine",
        "title": "Mocking, Patching & Side Effects with pytest-mock",
        "concepts": ["unittest.mock fundamentals", "pytest-mock (mocker fixture)", "patch.object vs patch()", "Simulating API network timeouts, HTTP 500 errors, and return values"],
        "assignment": "Write integration tests for a payment-processing client where third-party Stripe API calls and database connections are strictly mocked with realistic latencies and failure responses.",
        "deliverable": "pytest-blueprint/tests/test_mocking.py",
        "interviewQ": "What is the critical rule regarding WHERE to patch an object when writing unit/integration mocks in Python?",
        "interviewAns": "Always patch where the object is LOOKED UP and USED, not where it was originally defined. If module_b imports function_a from module_a, you must patch 'module_b.function_a'.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 26, "week": 4, "month": 1, "category": "Pytest Engine",
        "title": "Parallel Runs (pytest-xdist) & Module Deliverable",
        "concepts": ["pytest-xdist architecture (-n auto, -n 4)", "Test distribution algorithms (--dist=loadfile, --dist=load)", "Worker process isolation", "Packaging pytest-advanced-blueprint"],
        "assignment": "Configure pytest-xdist across 4 workers. Prove tests execute in parallel with zero shared state conflicts. Push repo with README and passing CI checks.",
        "deliverable": "GitHub Repo: pytest-advanced-blueprint (Release v1.0.0)",
        "interviewQ": "How does pytest-xdist distribute tests across worker processes and how do you ensure isolation between them?",
        "interviewAns": "pytest-xdist spawns separate Python worker subprocesses and uses load scheduling (--dist=load). State isolation is ensured by scoping fixtures per worker and provisioning unique data per worker.",
        "timebox": "Theory: 1.0h | Coding: 3.5h | Katas: 1.5h"
    },

    # =========================================================================
    # MODULE 3: API AUTOMATION, HTTP & SQL DATA RECONCILIATION (DAYS 27 - 40)
    # =========================================================================
    {
        "day": 27, "week": 4, "month": 1, "category": "API Testing",
        "title": "HTTP Protocol & REST Architecture",
        "concepts": ["HTTP Request/Response lifecycle", "HTTP Methods: GET, POST, PUT, PATCH, DELETE", "Idempotency & Safety principles", "Status Codes: 2xx Success, 3xx Redirect, 4xx Client, 5xx Server"],
        "assignment": "Build an HTTP testing script that asserts idempotency guarantees across repeated PUT and DELETE requests against a REST mock service.",
        "deliverable": "api-validator/tests/test_http_semantics.py",
        "interviewQ": "Why is PUT considered idempotent while POST is not, and how do you write an automated test verifying idempotency?",
        "interviewAns": "PUT replaces the resource state entirely; dispatching N identical PUT requests results in the exact same state. POST creates child resources and may append duplicates. Test by sending identical requests and asserting identical DB/response states.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 28, "week": 4, "month": 1, "category": "API Testing",
        "title": "API Automation Engine with Requests & HTTPX",
        "concepts": ["requests vs httpx (sync vs async)", "Sessions & connection pooling", "Query parameters, custom headers, request bodies", "Response parsing: .json(), .text, .status_code, latency"],
        "assignment": "Implement a reusable RestClient class wrapping httpx.Client with base URLs, default timeouts, automatic logging of curl commands, and response validation.",
        "deliverable": "api-validator/client/rest_client.py",
        "interviewQ": "Why should enterprise API frameworks use httpx.Client() / requests.Session() instead of raw requests.get() calls?",
        "interviewAns": "Sessions maintain an underlying TCP connection pool (keep-alive), eliminating the overhead of repeated TCP/TLS handshakes for every test, speeding up API suites by 3x.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 29, "week": 5, "month": 2, "category": "API Testing",
        "title": "Authentication: API Keys, Bearer & Dynamic OAuth2",
        "concepts": ["Basic Auth vs API Key in header/query", "Bearer Token format (JWT header, payload, signature)", "OAuth2 Client Credentials & Refresh flows", "Token caching in memory with expiry checks"],
        "assignment": "Build an AuthSession manager that fetches OAuth2 tokens, caches them in memory, and automatically refreshes tokens 30 seconds before expiration.",
        "deliverable": "api-validator/client/auth_manager.py",
        "interviewQ": "How do you architect token authentication in an API test suite to avoid logging in before every single test while preventing expired token failures?",
        "interviewAns": "Implement a singleton or session-scoped AuthManager that caches the token and its expiration timestamp. Before dispatching any request, check if (expiry - now) < 30s; if true, trigger a refresh call seamlessly.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 30, "week": 5, "month": 2, "category": "API Testing",
        "title": "Contract Testing & JSON Schema Validation",
        "concepts": ["JSON Schema Draft-07 specification", "Validating types, enums, regex patterns, required keys", "jsonschema.validate() vs FormatChecker", "Detecting breaking API contract changes"],
        "assignment": "Create strict JSON schemas for complex User, Order, and Product entities. Write automated tests validating production response schemas with descriptive error logs.",
        "deliverable": "api-validator/schemas/order_schema.py",
        "interviewQ": "Why is JSON schema validation superior to checking individual response dictionary keys?",
        "interviewAns": "Individual key asserts only check specific fields you remembered to write. JSON schema validates the entire payload structure (types, nullability, missing fields, unexpected extra fields) in a single assertion.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 31, "week": 5, "month": 2, "category": "API Testing",
        "title": "Pydantic v2 for API Response Deserialization",
        "concepts": ["Pydantic BaseModel & Field validation", "model_validate() for API responses", "Strict type coercion", "Handling optional fields and nested models"],
        "assignment": "Define Pydantic v2 models for an e-commerce checkout API. Parse raw API responses into typed models, asserting business logic on typed attributes with autocomplete.",
        "deliverable": "api-validator/models/order_models.py",
        "interviewQ": "How does using Pydantic response models improve test suite maintainability compared to raw dictionary access?",
        "interviewAns": "Pydantic converts raw dictionaries into strongly typed Python objects with IDE autocomplete, catch schema drifts immediately at deserialization time, and prevents KeyError exceptions.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 32, "week": 5, "month": 2, "category": "API Testing",
        "title": "Negative, Boundary & Security Payload Fuzzing",
        "concepts": ["Boundary Value Analysis applied to API fields", "Testing HTTP 400, 401, 403, 404, 422, 429", "SQL injection strings, XSS payloads, Unicode edge cases", "Rate-limit handling"],
        "assignment": "Write a 35-case parametrized negative test suite injecting invalid boundary payloads, malformed headers, and SQL injection strings, asserting proper HTTP 4xx error schemas.",
        "deliverable": "api-validator/tests/test_negative_boundaries.py",
        "interviewQ": "What should an SDET assert when an API endpoint receives an invalid boundary payload?",
        "interviewAns": "Assert: (1) Correct 4xx status code (e.g. 400/422, never 500), (2) Consistent error schema, (3) Meaningful error message pointing to the invalid field, (4) Zero state mutation in the database.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 33, "week": 5, "month": 2, "category": "API Testing",
        "title": "Postman & Newman Headless CI Integration",
        "concepts": ["Postman Collections, Folders, Environments", "Pre-request and Test scripts in JavaScript", "Running collections headless via Newman CLI", "Exporting JUnit XML reports for CI"],
        "assignment": "Build a multi-step user onboarding collection in Postman with chained variables, and write a shell script to run it via Newman in headless CI mode generating JUnit reports.",
        "deliverable": "api-validator/newman/run_collections.sh",
        "interviewQ": "When should an SDET team use Postman/Newman versus a native Python pytest/httpx test framework?",
        "interviewAns": "Postman/Newman is ideal for quick exploratory testing, manual-to-automation handoffs, and basic API smoke checks. Python frameworks are required for complex logic, DB reconciliation, and hybrid E2E flows.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 34, "week": 5, "month": 2, "category": "API Testing",
        "title": "Asynchronous Concurrency & Latency Benchmarking",
        "concepts": ["asyncio event loop basics", "httpx.AsyncClient for concurrent dispatch", "asyncio.gather() for load simulation", "Calculating p50, p95, p99 response times"],
        "assignment": "Build an async API benchmark script that fires 50 concurrent requests against a target endpoint, asserting zero 5xx server errors and p95 latency under 350ms.",
        "deliverable": "api-validator/benchmarks/concurrency_check.py",
        "interviewQ": "What is the difference between p50, p95, and p99 latency in API testing, and why do SDETs focus on p95/p99?",
        "interviewAns": "p50 is the median experience, hiding outliers. p95 and p99 reflect the slowest 5% and 1% of user requests—where connection pooling, GC pauses, or DB locks reveal system bottlenecks.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 35, "week": 5, "month": 2, "category": "SQL & Data",
        "title": "Relational SQL Fundamentals for SDETs",
        "concepts": ["Relational DB concepts (Tables, Primary Keys, Foreign Keys)", "SELECT, WHERE, LIKE, IN, BETWEEN, ORDER BY", "NULL vs Empty string handling", "psycopg2 and SQLAlchemy basics"],
        "assignment": "Connect to a PostgreSQL test database using Python SQLAlchemy. Write queries to fetch and verify user accounts based on complex multi-column filter criteria.",
        "deliverable": "api-validator/sql/basic_queries.py",
        "interviewQ": "Why is handling NULL values correctly in SQL assertions critical, and how does 'WHERE column = NULL' fail?",
        "interviewAns": "In SQL, NULL represents an unknown value; comparing 'column = NULL' always evaluates to UNKNOWN/False. You must use 'IS NULL' or 'IS NOT NULL' to assert missing values.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 36, "week": 6, "month": 2, "category": "SQL & Data",
        "title": "SQL Multi-Table Joins for Data Validation",
        "concepts": ["INNER JOIN semantics", "LEFT JOIN vs RIGHT JOIN", "FULL OUTER JOIN for delta detection", "Self joins for hierarchical data"],
        "assignment": "Write complex SQL queries joining Orders, OrderItems, Customers, and Payments to identify unfulfilled orders and orphaned records.",
        "deliverable": "api-validator/sql/multi_table_joins.sql",
        "interviewQ": "How do you write a query using a LEFT JOIN to find orphaned records in a child table with no parent record?",
        "interviewAns": "SELECT c.* FROM child_table c LEFT JOIN parent_table p ON c.parent_id = p.id WHERE p.id IS NULL; This returns all child rows where the parent lookup failed.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 37, "week": 6, "month": 2, "category": "SQL & Data",
        "title": "SQL Aggregations, GROUP BY & Duplicate Hunting",
        "concepts": ["GROUP BY and HAVING clauses", "COUNT, SUM, AVG, MIN, MAX", "Finding duplicate records across composite keys", "Eliminating duplicates"],
        "assignment": "Write queries that detect duplicate user accounts created by concurrent API registration calls, grouping by email and tenant_id with HAVING COUNT(*) > 1.",
        "deliverable": "api-validator/sql/duplicate_detection.sql",
        "interviewQ": "What is the difference between WHERE and HAVING in an SQL aggregation query?",
        "interviewAns": "WHERE filters individual rows BEFORE grouping/aggregation; HAVING filters the aggregated group summaries AFTER GROUP BY calculations.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 38, "week": 6, "month": 2, "category": "SQL & Data",
        "title": "SQL Window Functions & Source-to-Target Reconciliation",
        "concepts": ["ROW_NUMBER(), RANK(), DENSE_RANK()", "PARTITION BY and ORDER BY within windows", "Source-to-Target (S2T) verification", "Reconciling JSON payloads against database tables"],
        "assignment": "Build a Python Source-to-Target reconciliation utility that takes an API order response and executes SQL window queries to assert that the latest status transition matches the DB.",
        "deliverable": "api-validator/reconciliation/s2t_reconciler.py",
        "interviewQ": "How do you reconcile floating-point currencies and timestamps between JSON API responses and SQL databases without false mismatches?",
        "interviewAns": "Normalize timestamps to UTC ISO-8601 strings or epoch seconds before comparing. For currencies, compare using Decimal or integer cents to prevent IEEE-754 floating-point inaccuracies.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 39, "week": 6, "month": 2, "category": "Git & CI/CD",
        "title": "Git Mastery: Branches, PRs & Merge Conflicts",
        "concepts": ["Git architecture (Working directory, Staging, Local Repo, Remote)", "Branching strategies (Git Flow, Trunk-based)", "git merge vs git rebase", "Resolving merge conflicts like a senior engineer"],
        "assignment": "Simulate a merge conflict between two local feature branches modifying the same test file. Resolve the conflict cleanly using git rebase and push a clean commit history.",
        "deliverable": "git-practice/conflict_resolution_notes.md",
        "interviewQ": "When should an SDET use 'git rebase' versus 'git merge', and what is the golden rule of rebasing?",
        "interviewAns": "Use rebase on local, unshared feature branches to maintain a clean linear commit history. Golden rule: NEVER rebase a public shared branch (like main or staging) as it rewrites commit SHAs.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 40, "week": 6, "month": 2, "category": "Portfolio Milestone",
        "title": "Portfolio Repo 2 Complete: api-reliability-data-validator",
        "concepts": ["Packaging the full API & DB validator", "Adding Allure reporting with curl attachments", "Writing a comprehensive README with architecture diagrams", "Tagging Release v1.0.0"],
        "assignment": "Finalize and publish Repo 2 on GitHub: api-reliability-data-validator. Verify 40+ API and SQL reconciliation tests execute cleanly in parallel.",
        "deliverable": "GitHub Repo: api-reliability-data-validator (Release v1.0.0)",
        "interviewQ": "Walk me through how your API test suite verifies end-to-end data integrity from request payload to database persistence.",
        "interviewAns": "Explain the 3-step pipeline: (1) Dispatch typed HTTP request via httpx client, (2) Validate HTTP status and JSON response schema, (3) Execute S2T reconciler querying PostgreSQL to verify atomic persistence.",
        "timebox": "Theory: 1.0h | Coding: 3.5h | Katas: 1.5h"
    },

    # =========================================================================
    # MODULE 4: MODERN WEB AUTOMATION (PLAYWRIGHT) & POM (DAYS 41 - 56)
    # =========================================================================
    {
        "day": 41, "week": 6, "month": 2, "category": "Playwright Core",
        "title": "Playwright Architecture vs Selenium",
        "concepts": ["Chrome DevTools Protocol (CDP) & WebSockets", "No WebDriver HTTP middleman", "Auto-waiting actionability checks", "Sync vs Async Python API"],
        "assignment": "Set up Playwright Python, inspect WebSocket traffic in Chrome DevTools, and write benchmark comparisons showing execution speed vs traditional HTTP drivers.",
        "deliverable": "playwright-engine/benchmarks/playwright_speed.py",
        "interviewQ": "What architectural differences make Playwright significantly faster and less flaky than Selenium 3/4?",
        "interviewAns": "Playwright communicates over a single persistent WebSocket connection directly with browser processes via CDP, whereas Selenium dispatches individual HTTP REST commands to an intermediary driver executable.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 42, "week": 6, "month": 2, "category": "Playwright Core",
        "title": "Modern User-Facing Locators",
        "concepts": ["get_by_role, get_by_text, get_by_label", "get_by_test_id (custom test attributes)", "Chaining and filtering locators", "Why XPath is an anti-pattern"],
        "assignment": "Automate a dynamic dashboard using exclusively get_by_role, get_by_label, and get_by_test_id. Zero raw XPath or brittle CSS selectors.",
        "deliverable": "playwright-engine/tests/test_modern_locators.py",
        "interviewQ": "Why does Playwright encourage user-facing locators over XPath and CSS selectors?",
        "interviewAns": "User-facing locators (e.g. get_by_role('button', name='Submit')) test accessibility trees matching how real users interact with the app, making tests resilient to internal DOM refactorings.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 43, "week": 7, "month": 2, "category": "Playwright Core",
        "title": "Dynamic Content, Hydration & Auto-Waiting",
        "concepts": ["Playwright auto-waiting algorithm", "expect(locator).to_be_visible()", "Avoiding time.sleep()", "Handling React hydration lag"],
        "assignment": "Automate an asynchronous UI with simulated 2-second AJAX loaders; ensure all state checks pass cleanly with zero hardcoded sleeps.",
        "deliverable": "playwright-engine/tests/test_async_hydration.py",
        "interviewQ": "Why does locator.click() succeed even when elements take 3 seconds to appear, but time.sleep() must still be avoided?",
        "interviewAns": "Playwright's actionability checks automatically poll the DOM up to the timeout limit, verifying visibility, stability, and enablement before clicking. Hardcoded sleep causes either brittle timing bugs or bloated suite duration.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 44, "week": 7, "month": 2, "category": "Playwright Core",
        "title": "Multi-Page Tabs, Dialogs & Nested Iframes",
        "concepts": ["page.expect_popup()", "page.on('dialog') event handlers", "frame_locator for nested iframes", "Shadow DOM piercing"],
        "assignment": "Automate a complex multi-window workflow: clicking a link opening a new tab, accepting a JavaScript confirm alert, and filling an input inside an iframe.",
        "deliverable": "playwright-engine/tests/test_tabs_dialogs_frames.py",
        "interviewQ": "How does Playwright pierce Shadow DOM boundaries compared to Selenium?",
        "interviewAns": "Playwright locators pierce open Shadow DOM roots automatically by default without requiring special JavaScript execution or shadowRoot traversal commands.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 45, "week": 7, "month": 2, "category": "Playwright Core",
        "title": "File Uploads, Downloads & Clipboard Handling",
        "concepts": ["set_input_files()", "page.expect_download()", "Inspecting downloaded file streams in Python", "Granting clipboard permissions"],
        "assignment": "Automate downloading a dynamic report, verifying the downloaded file's SHA-256 hash in memory, and testing a multi-file drag-and-drop upload.",
        "deliverable": "playwright-engine/tests/test_uploads_downloads.py",
        "interviewQ": "How do you test file downloads in headless browser environments running on remote Linux CI nodes?",
        "interviewAns": "Use with page.expect_download() as download_info: locator.click(). Then save the downloaded artifact stream to an ephemeral path via download.save_as() and assert contents.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 46, "week": 7, "month": 2, "category": "Playwright Core",
        "title": "Mouse Gestures, Keyboard Actions & Canvas",
        "concepts": ["page.mouse and page.keyboard low-level APIs", "Drag and drop interactions", "Keyboard shortcuts and modifiers", "HTML5 Canvas interaction"],
        "assignment": "Automate a drag-and-drop Kanban task board, moving items across status columns and verifying column item count updates.",
        "deliverable": "playwright-engine/tests/test_drag_and_drop.py",
        "interviewQ": "When should you use locator.drag_to() versus low-level mouse.down() and mouse.move()?",
        "interviewAns": "locator.drag_to() handles standard DOM elements with automated coordinate resolution. Low-level mouse commands are necessary for custom Canvas, map controls, or complex multi-step drawing gestures.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 47, "week": 7, "month": 2, "category": "Playwright Advanced",
        "title": "Browser Contexts & State Reuse (storage_state)",
        "concepts": ["Browser vs BrowserContext vs Page", "storage_state JSON format", "Bypassing UI login per test", "Multi-role test setups"],
        "assignment": "Implement a login fixture that performs an API/UI login once, saves session tokens to auth.json, and initializes subsequent tests authenticated in <200ms.",
        "deliverable": "playwright-engine/fixtures/auth_fixtures.py",
        "interviewQ": "How does storage_state provide 10x speedups in large end-to-end test suites?",
        "interviewAns": "It bypasses UI authentication pages entirely for 95% of tests, directly injecting valid session cookies, JWT tokens, and localStorage items into ephemeral browser contexts.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 48, "week": 7, "month": 2, "category": "Playwright Advanced",
        "title": "Network Interception & API Route Mocking",
        "concepts": ["page.route() API", "Fulfilling custom mock responses", "Modifying real API payloads on the fly", "Aborting third-party tracking scripts"],
        "assignment": "Write a test that intercepts user profile API responses, injects an expired subscription payload, and asserts the UI displays the renewal banner.",
        "deliverable": "playwright-engine/tests/test_network_mocking.py",
        "interviewQ": "Why would an SDET mock network calls in UI tests instead of always hitting live staging environments?",
        "interviewAns": "Mocking isolates UI component testing from backend outages, allows testing rare edge cases (e.g. 500 errors, rate limits, corrupt schemas), and removes network latency.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 49, "week": 7, "month": 2, "category": "Playwright Advanced",
        "title": "HAR Recording & Offline Replay Testing",
        "concepts": ["HTTP Archive (HAR) format", "record_har_path context option", "Replaying HAR for deterministic UI testing", "Network isolation"],
        "assignment": "Record a complete e-commerce checkout flow into a HAR archive, then write an automated test running with all outbound network traffic routed from the HAR.",
        "deliverable": "playwright-engine/tests/test_har_replay.py",
        "interviewQ": "What are the trade-offs of using HAR replay testing versus live end-to-end integration testing?",
        "interviewAns": "HAR replay gives deterministic, blisteringly fast, offline-capable UI testing. The trade-off is contract drift: if the backend API changes, the HAR becomes stale unless regenerated.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 50, "week": 8, "month": 2, "category": "Playwright Advanced",
        "title": "Playwright Tracing & Failure Diagnostics",
        "concepts": ["tracing.start() and tracing.stop()", "Inspecting trace.zip", "Action filmstrips, DOM snapshots, network waterfall", "Trace on failure fixture"],
        "assignment": "Configure pytest fixtures to automatically record and package a Playwright trace archive only when a test fails, attaching it to test reports.",
        "deliverable": "playwright-engine/fixtures/trace_fixtures.py",
        "interviewQ": "Why is a Playwright trace infinitely more valuable than a simple screenshot for remote debugging?",
        "interviewAns": "A screenshot captures only the final static pixel state. A trace provides an interactive timeline replay with full DOM snapshots, exact mouse coordinates, console logs, and network waterfalls.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 51, "week": 8, "month": 2, "category": "Playwright Advanced",
        "title": "Visual Regression & Snapshot Masking",
        "concepts": ["expect(page).to_have_screenshot()", "Pixel comparison thresholds (max_diff_pixels)", "Masking dynamic dates/avatars", "Cross-platform anti-aliasing"],
        "assignment": "Create a visual regression test for a dashboard page that masks dynamic timestamps and avatar images, asserting layout consistency within a 2% threshold.",
        "deliverable": "playwright-engine/tests/test_visual_regression.py",
        "interviewQ": "Why do visual regression tests frequently fail when moving from macOS local environments to Linux CI containers?",
        "interviewAns": "Different operating systems render fonts, anti-aliasing curves, and GPU shadows differently. Visual baselines must be captured and evaluated inside identical Docker containers.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 52, "week": 8, "month": 2, "category": "Framework Design",
        "title": "Scalable Page Component Model Design",
        "concepts": ["Page Object Model vs Component Model", "Encapsulating locators", "Fluent interface pattern", "Avoiding monolithic page classes"],
        "assignment": "Refactor raw test scripts into clean Page Components (NavigationBar, CheckoutForm, OrderSummary) returning new page instances on transitions.",
        "deliverable": "playwright-engine/pages/checkout_page.py",
        "interviewQ": "How does the Page Component Model improve upon traditional Page Object Model architectures?",
        "interviewAns": "Traditional POM creates massive monolithic classes for complex pages. Component models break pages into modular, reusable UI widgets (e.g. Header, Table, Modal) shared across views.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 53, "week": 8, "month": 2, "category": "Framework Design",
        "title": "Centralized Config with Pydantic BaseSettings",
        "concepts": ["Pydantic BaseSettings", "Dynamic environment switching (dev/qa/staging/prod)", "Base URLs and credentials", "CLI override parsing"],
        "assignment": "Implement a config engine that reads from .env and pytest CLI arguments, providing typed configuration objects across the entire test suite.",
        "deliverable": "playwright-engine/config/settings.py",
        "interviewQ": "How do you design configuration handling so secrets are never committed to git or printed in CI logs?",
        "interviewAns": "Use Pydantic BaseSettings to read from environment variables injected by CI secret vaults, with custom str representations that mask sensitive fields as [SECRET].",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 54, "week": 8, "month": 2, "category": "Framework Design",
        "title": "Hermetic Test Data Management & Cleanup",
        "concepts": ["Dynamic test user provisioning", "Fast API seeding before UI execution", "Teardown cleanup hooks", "Idempotent test runners"],
        "assignment": "Create a test fixture that provisions a fresh tenant account via API in 150ms, launches the UI test with that tenant, and deletes the tenant in teardown.",
        "deliverable": "playwright-engine/fixtures/tenant_fixtures.py",
        "interviewQ": "Why is dynamic test data generation superior to relying on pre-existing static test accounts in staging?",
        "interviewAns": "Static accounts accumulate dirty state, suffer from concurrent login conflicts, and cause cascade failures when password or state changes occur.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 55, "week": 8, "month": 2, "category": "Framework Design",
        "title": "Structured Masked Logging & Allure Reporting",
        "concepts": ["Contextual loggers with secret redacting", "Allure-pytest reporting hooks", "Attaching traces, screenshots, videos on failure", "Environment properties metadata"],
        "assignment": "Integrate Allure and structured JSON logging into the framework. Verify reports contain execution timelines, environment properties, and attached failure traces.",
        "deliverable": "playwright-engine/reporting/allure_hooks.py",
        "interviewQ": "How do you configure Allure to attach environment metadata (OS, browser version, commit SHA) to test reports?",
        "interviewAns": "Write an environment.properties file into the allure-results folder during pytest session teardown containing dynamic CI variables.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 56, "week": 8, "month": 2, "category": "Portfolio Milestone",
        "title": "Portfolio Repo 1 Complete: playwright-python-enterprise-engine",
        "concepts": ["Full test engine review", "Packaging Repo 1: playwright-python-enterprise-engine", "Verification of parallel test runs", "Tagging Release v1.0.0"],
        "assignment": "Deliver Repo 1 on GitHub: verify 30+ hybrid and UI tests pass in parallel across Chromium and Firefox with rich Allure reports. Tag v1.0.0.",
        "deliverable": "GitHub Repo: playwright-python-enterprise-engine (v1.0.0)",
        "interviewQ": "Walk me through the architecture of your hybrid test framework and why you chose Playwright over Cypress or Selenium.",
        "interviewAns": "Highlight: Playwright Python provides true multi-browser context isolation, native async support, DevTools protocol speed, auto-waiting, and seamless storage_state auth bypassing.",
        "timebox": "Theory: 1.0h | Coding: 3.5h | Katas: 1.5h"
    },

    # =========================================================================
    # MODULE 5: HYBRID TESTING, LINUX, DOCKER & CI/CD PIPELINES (DAYS 57 - 70)
    # =========================================================================
    {
        "day": 57, "week": 9, "month": 3, "category": "Hybrid Testing",
        "title": "The Hybrid Test Pattern (API + UI + SQL)",
        "concepts": ["Fast-forwarding state via API", "Targeted UI user actions", "Direct database assertion", "Test pyramid optimization"],
        "assignment": "Write a complete hybrid test: create an order via API in 200ms, use Playwright to cancel the order on UI, assert cancellation status in SQL.",
        "deliverable": "playwright-engine/tests/test_hybrid_e2e.py",
        "interviewQ": "Why is the hybrid testing pattern essential for keeping large end-to-end regression suites under 20 minutes?",
        "interviewAns": "It eliminates redundant UI steps (logging in, creating prerequisite data via forms), executing setup via fast API/DB calls and reserving UI execution strictly for the feature under test.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 58, "week": 9, "month": 3, "category": "Framework Quality",
        "title": "Strict Code Quality: Ruff & Mypy Strict Mode",
        "concepts": ["ruff linter and code formatter", "mypy --strict type checking", "Pre-commit hook pipelines", "Eliminating false positives and type ignores"],
        "assignment": "Configure ruff and mypy strict mode on Repo 1. Fix all type annotations across all fixtures and page helpers with zero errors.",
        "deliverable": "playwright-engine/.ruff.toml",
        "interviewQ": "Why do top-tier tech companies require strict type hints even in test automation codebases?",
        "interviewAns": "Strict typing catches API changes, invalid attribute accesses, and None-pointer bugs during IDE authoring and static analysis, preventing false-positive test crashes.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 59, "week": 9, "month": 3, "category": "Framework Quality",
        "title": "Packaging with pyproject.toml & Dependency Locking",
        "concepts": ["Modern pyproject.toml packaging", "Editable installs (pip install -e .)", "Locking exact dependency hashes with uv or poetry", "Dependency groups (dev, test, ci)"],
        "assignment": "Package the automation engine using pyproject.toml, locking dependencies with uv, guaranteeing deterministic reproducible installs in CI.",
        "deliverable": "playwright-engine/pyproject.toml",
        "interviewQ": "Why is pinning test package dependencies with tools like uv or poetry critical for CI/CD stability?",
        "interviewAns": "Unpinned dependencies risk pulling breaking minor or patch releases from third-party libraries overnight, causing sudden test suite failures unrelated to application code.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 60, "week": 9, "month": 3, "category": "Linux & DevOps",
        "title": "Linux Fundamentals & Shell Scripting for SDETs",
        "concepts": ["Process management (ps, kill)", "Bash conditionals, loops, exit codes ($?)", "sed, awk, grep text processing", "Healthcheck polling scripts"],
        "assignment": "Write a robust bash entrypoint script that polls an application healthcheck endpoint until HTTP 200 before launching pytest suites.",
        "deliverable": "playwright-engine/docker/entrypoint.sh",
        "interviewQ": "Why is checking exit codes ($?) critical in CI shell scripts?",
        "interviewAns": "CI runners rely on command exit codes to determine success (0) or failure (>0). Without proper exit code propagation (or set -e), failed commands may be masked as passing jobs.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 61, "week": 9, "month": 3, "category": "Docker & Containers",
        "title": "Docker Deep Dive for Headless Browsers",
        "concepts": ["Official Playwright Docker images", "Multi-stage Docker builds", "Handling shared memory (/dev/shm) issues", "Layer caching optimization"],
        "assignment": "Write a multi-stage Dockerfile that installs dependencies cleanly, copies test code, sets appropriate SHM limits, and runs headless tests.",
        "deliverable": "playwright-engine/Dockerfile",
        "interviewQ": "Why do Chromium browsers crash with 'Target closed' inside default Docker containers, and how do you fix it?",
        "interviewAns": "Chromium exhausts the default 64MB /dev/shm shared memory partition in Docker. Fix by launching containers with --ipc=host or --shm-size=2gb in Docker/CI configurations.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 62, "week": 9, "month": 3, "category": "Docker & Containers",
        "title": "Docker Compose Multi-Service Test Environments",
        "concepts": ["docker-compose.yml", "Orchestrating mock API, Postgres, and test container", "Healthcheck dependencies (depends_on condition)", "Volume mounts"],
        "assignment": "Create a docker-compose.yml file that launches a mock backend, boots PostgreSQL, seeds schema, executes the test suite, and saves Allure reports.",
        "deliverable": "playwright-engine/docker-compose.yml",
        "interviewQ": "How does depends_on with service_healthy ensure reliable integration testing in Docker Compose?",
        "interviewAns": "Simple depends_on only waits for container creation; service_healthy waits until the service's internal healthcheck command succeeds, preventing tests from hitting unready ports.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 63, "week": 9, "month": 3, "category": "CI/CD & Pipelines",
        "title": "GitHub Actions CI Workflow Architecture",
        "concepts": [".github/workflows syntax", "Triggers (push, pull_request, workflow_dispatch)", "Step caching (pip, Playwright binaries)", "Parallel matrix jobs"],
        "assignment": "Create a GitHub Actions workflow that triggers on every pull request, caches dependencies, and executes the smoke test suite in <3 minutes.",
        "deliverable": "playwright-engine/.github/workflows/pr_smoke.yml",
        "interviewQ": "How do you cache Playwright browser binaries in GitHub Actions to avoid re-downloading 300MB on every build?",
        "interviewAns": "Use actions/cache with a key based on the runner OS and Playwright version from pyproject.toml targeting ~/.cache/ms-playwright.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 64, "week": 10, "month": 3, "category": "CI/CD & Pipelines",
        "title": "CI Matrix Sharding & Distributed Runs",
        "concepts": ["Matrix strategy: shard [1/4, 2/4, 3/4, 4/4]", "pytest-shard vs Playwright --shard", "Merging distributed test reports into one Allure view", "Reducing CI cycle time"],
        "assignment": "Configure a matrix workflow that shards 100 tests across 4 parallel GitHub Actions runner VMs, merging results into a unified Allure report.",
        "deliverable": "playwright-engine/.github/workflows/sharded_regression.yml",
        "interviewQ": "How does test sharding differ from multi-threading (pytest-xdist) and when should you combine both?",
        "interviewAns": "pytest-xdist parallelizes across CPU cores on a single machine. Sharding distributes tests across entirely separate virtual machines. Combine both for massive suites.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 65, "week": 10, "month": 3, "category": "CI/CD & Pipelines",
        "title": "Quality Gates, Failure Alerts & Artifact Archival",
        "concepts": ["Branch protection rules", "actions/upload-artifact for traces", "Automated PR comment summaries", "Slack/Webhook failure alerts"],
        "assignment": "Configure GitHub Actions to automatically post a markdown summary comment on failing PRs with links to downloaded traces and test duration stats.",
        "deliverable": "playwright-engine/.github/workflows/publish_report.yml",
        "interviewQ": "What criteria should define an automated CI quality gate before allowing code merges to production?",
        "interviewAns": "Zero test failures in critical smoke suites, <1% flakiness rate in regression suites, zero security/vulnerability alerts, and adherence to performance/p95 thresholds.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 66, "week": 10, "month": 3, "category": "CI/CD & Pipelines",
        "title": "Jenkins Pipelines Basics for Enterprise Teams",
        "concepts": ["Jenkins architecture (Controller vs Agents)", "Declarative Jenkinsfile syntax", "Stages: Checkout -> Build -> Test -> QualityGate -> Archive", "Post-build actions"],
        "assignment": "Write a declarative Jenkinsfile defining stages for dependency installation, headless test execution inside Docker, and Allure report archiving.",
        "deliverable": "playwright-engine/Jenkinsfile",
        "interviewQ": "How do declarative Jenkins pipelines differ from scripted pipelines, and which is preferred for modern SDET teams?",
        "interviewAns": "Declarative pipelines offer a simpler, structured, opinionated syntax with built-in stage, post-action, and agent blocks. They are easier to maintain, audit, and standardize across teams.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 67, "week": 10, "month": 3, "category": "Observability & Ops",
        "title": "Taxonomy of Test Failures: Root Cause Analysis",
        "concepts": ["Categorizing failures: Product Bug vs Environment Bug vs Test Bug", "Failure triage flowchart", "Root Cause Analysis (RCA) reporting", "MTTR metrics"],
        "assignment": "Review 5 complex test failure logs and draft structured RCA incident tickets identifying whether the root cause was product regression, network drop, or selector race.",
        "deliverable": "playwright-engine/docs/flaky_rca_templates.md",
        "interviewQ": "How do you distinguish between an application bug and a flaky test race condition from CI log output?",
        "interviewAns": "Examine the trace: if the network call returned 500 or UI state rendered an error banner, it is an application bug. If element actionability timed out while the DOM was mid-render, it is a race condition.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 68, "week": 10, "month": 3, "category": "Observability & Ops",
        "title": "Quarantine Pipelines vs Retry Anti-Patterns",
        "concepts": ["Why unconditional retries (--reruns 3) mask bugs", "Quarantine test markers (@pytest.mark.quarantine)", "Non-blocking quarantine CI runs", "Flaky burn-down SLAs"],
        "assignment": "Implement a quarantine workflow where tests marked as flaky run in an informational CI lane without blocking PR merges, alerting owners if failure rate exceeds 20%.",
        "deliverable": "playwright-engine/.github/workflows/quarantine.yml",
        "interviewQ": "Why is relying on automatic test retries (--reruns) considered an engineering anti-pattern?",
        "interviewAns": "Retries hide intermittent race conditions, deadlocks, and memory leaks from developers. They increase CI duration and cost while allowing unstable code into production.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 69, "week": 10, "month": 3, "category": "Observability & Ops",
        "title": "Cloud Basics (AWS S3 & CloudWatch Logs)",
        "concepts": ["AWS S3 for test artifact and report hosting", "AWS CloudWatch log querying", "IAM roles and least privilege", "boto3 Python SDK"],
        "assignment": "Write a Python script using boto3 that uploads Allure HTML report directories to an AWS S3 bucket and generates secure shareable links.",
        "deliverable": "playwright-engine/scripts/upload_to_s3.py",
        "interviewQ": "How do you securely configure test runner VMs in AWS to access S3 without embedding AWS access keys?",
        "interviewAns": "Attach an IAM Instance Profile / Role to the EC2 or ECS task with S3:PutObject permissions, allowing the AWS SDK to retrieve temporary STS credentials automatically.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 70, "week": 10, "month": 3, "category": "Observability & Ops",
        "title": "Correlation IDs & Distributed Tracing in Microservices",
        "concepts": ["X-Correlation-ID / X-Request-ID propagation", "Tracing test failures into backend microservices", "CloudWatch Logs Insights queries", "Log correlation"],
        "assignment": "Build an API test client hook that injects unique correlation UUIDs into request headers and dumps corresponding backend server logs on failure.",
        "deliverable": "api-validator/client/correlation_hook.py",
        "interviewQ": "What is a Correlation ID and why is it vital for SDETs testing microservice architectures?",
        "interviewAns": "A unique identifier passed through all microservice calls for a single user transaction. When a test fails, the correlation ID allows instant querying of all related distributed logs.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },

    # =========================================================================
    # MODULE 6: AI-ASSISTED TESTING, PLAYWRIGHT MCP & INTERVIEWS (DAYS 71 - 84)
    # =========================================================================
    {
        "day": 71, "week": 11, "month": 3, "category": "AI Testing & MCP",
        "title": "AI-Assisted Testing with Copilot, Claude & Cursor",
        "concepts": ["AI-assisted test generation workflows", "Prompt patterns for generating boundary test vectors", "Context windows & providing OpenAPI schemas to LLMs", "IDE test agent loops"],
        "assignment": "Use an AI coding assistant (Cursor/Copilot) with structured prompt templates to scaffold 20 boundary tests from an OpenAPI schema, documenting productivity gains.",
        "deliverable": "mcp-agent/prompts/openapi_prompt_templates.md",
        "interviewQ": "How do you leverage AI tools like Cursor or Copilot without compromising code quality or introducing security vulnerabilities?",
        "interviewAns": "Use AI strictly as an acceleration copilot for boilerplate, never commit AI code without line-by-line review, verify all assertions with mutation testing, and redact confidential tokens before sending context.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 72, "week": 11, "month": 3, "category": "AI Testing & MCP",
        "title": "Auditing AI Hallucinations in Test Code",
        "concepts": ["Weak assertions (assert response is not None)", "Brittle hallucinated locators (xpath=//div[3]/span)", "Non-deterministic mocks", "Audit methodology"],
        "assignment": "Conduct a red team code review on 5 AI-generated test scripts, documenting 10 specific vulnerabilities/hallucinations and refactoring them to production standards.",
        "deliverable": "mcp-agent/audit/ai_code_review_report.md",
        "interviewQ": "How do you detect and prevent AI-generated 'tautological assertions' in automated tests?",
        "interviewAns": "Conduct code reviews verifying that assertions validate specific expected business state values rather than trivial existence checks (e.g. asserting specific user ID vs assert user is not None).",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 73, "week": 11, "month": 3, "category": "AI Testing & MCP",
        "title": "Model Context Protocol (MCP) Demystified",
        "concepts": ["What MCP is (open protocol for LLMs and tools)", "JSON-RPC communication model", "MCP Client vs MCP Server architecture", "Exposing tools to AI"],
        "assignment": "Study the official MCP specification; build a basic Python MCP server exposing custom testing tools to an LLM host.",
        "deliverable": "mcp-agent/server/basic_mcp_server.py",
        "interviewQ": "What is Model Context Protocol (MCP) and how does it fundamentally change AI test automation?",
        "interviewAns": "MCP standardizes how LLM agents interact with external tools and environments over JSON-RPC. Instead of brittle custom prompts, LLMs can call standardized testing tools directly.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 74, "week": 11, "month": 3, "category": "AI Testing & MCP",
        "title": "Deploying the Playwright MCP Server",
        "concepts": ["Running Playwright MCP server", "Connecting Claude Desktop / Cursor IDE", "Tool primitives: navigate, click, fill, evaluate", "Permissions"],
        "assignment": "Configure the Playwright MCP server locally, connect it to an LLM client, and prompt the AI to navigate a shopping site and take verified screenshots.",
        "deliverable": "mcp-agent/config/claude_desktop_config.json",
        "interviewQ": "How does the Playwright MCP server communicate with the browser compared to standard Playwright scripts?",
        "interviewAns": "The Playwright MCP server exposes browser actions as JSON-RPC tool endpoints. The LLM decides which tools to invoke based on user prompts, and the server executes them via CDP.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 75, "week": 11, "month": 3, "category": "AI Testing & MCP",
        "title": "Autonomous Exploratory Testing with MCP Agents",
        "concepts": ["Directing AI agents for exploratory testing", "Finding broken links and unhandled exceptions", "Probing forms for boundary validation errors", "Logging anomalies"],
        "assignment": "Execute an agentic exploratory testing session using Playwright MCP to probe a user onboarding flow, capturing console errors and UI layout shifts.",
        "deliverable": "mcp-agent/reports/exploratory_findings.md",
        "interviewQ": "What are the limitations of using autonomous AI agents for software testing today?",
        "interviewAns": "Agents suffer from non-deterministic execution paths, lack business domain context, struggle with complex multi-stage data setup, and can produce false positives.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 76, "week": 11, "month": 3, "category": "AI Testing & MCP",
        "title": "Building a Test Failure Diagnostic Agent (Repo 3)",
        "concepts": ["Parsing Playwright trace.zip programmatically", "Extracting failed network requests and console errors", "Prompting LLM with structured trace context", "Generating RCA markdown"],
        "assignment": "Build a Python CLI tool: 'diagnose-failure trace.zip' that parses failure logs, calls Claude/OpenAI API, and outputs an actionable bug report with reproduction steps.",
        "deliverable": "testops-mcp-diagnostic-agent/diagnose.py",
        "interviewQ": "Walk me through how your diagnostic agent extracts failure context from a zipped Playwright trace file.",
        "interviewAns": "The script unzips trace.zip, parses the trace.stacks and trace.network JSON streams, filters for HTTP 4xx/5xx or action timeouts, and bundles the exact failure frame for AI analysis.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 77, "week": 11, "month": 3, "category": "Portfolio Milestone",
        "title": "Portfolio Repo 3 Complete: testops-mcp-diagnostic-agent",
        "concepts": ["Packaging testops-mcp-diagnostic-agent", "Writing README with demo GIF/video", "Adding CLI installation commands", "Publishing release v1.0.0"],
        "assignment": "Finalize Repo 3 on GitHub with a demo video/GIF showing the agent diagnosing a real failed Playwright test trace and tagging v1.0.0.",
        "deliverable": "GitHub Repo: testops-mcp-diagnostic-agent (v1.0.0)",
        "interviewQ": "Why is an AI diagnostic tool like Repo 3 a high-impact engineering contribution in an enterprise SDET team?",
        "interviewAns": "It reduces Mean Time To Resolution (MTTR) for CI test failures from 30 minutes of manual log digging to 10 seconds of automated diagnostic summary.",
        "timebox": "Theory: 1.0h | Coding: 3.5h | Katas: 1.5h"
    },
    {
        "day": 78, "week": 12, "month": 3, "category": "Interview Prep",
        "title": "Round 1 Prep: Python Live Coding Katas",
        "concepts": ["Timed coding without IDE auto-complete", "String manipulation & anagrams", "Dictionary nesting & flattening", "Two-pointer algorithms"],
        "assignment": "Complete 15 high-frequency SDET coding katas under 45-minute timed exam conditions on a blank text editor.",
        "deliverable": "interview-vault/python_live_coding_katas.py",
        "interviewQ": "Write an in-place algorithm to remove duplicate characters from a string while preserving original order in O(N) time.",
        "interviewAns": "Use a set to track seen characters and a list comprehension or generator to rebuild the string: seen = set(); ''.join(c for c in s if not (c in seen or seen.add(c))).",
        "timebox": "Theory: 1.0h | Coding: 3.5h | Katas: 1.5h"
    },
    {
        "day": 79, "week": 12, "month": 3, "category": "Interview Prep",
        "title": "Round 1 Prep: Advanced Python (Decorators & Generators)",
        "concepts": ["Writing custom decorators with variable arguments", "Generator state machines", "Context managers with contextlib", "Memory profiling"],
        "assignment": "Implement a custom memory-profiling context manager and an API caching decorator from memory in under 20 minutes.",
        "deliverable": "interview-vault/advanced_python_drills.py",
        "interviewQ": "How do Python generators maintain state across yields, and how does this enable processing multi-gigabyte log files?",
        "interviewAns": "Generators suspend execution frame state (local variables and instruction pointer) on 'yield' and resume on next(), evaluating lazily without loading the entire dataset into RAM.",
        "timebox": "Theory: 1.0h | Coding: 3.5h | Katas: 1.5h"
    },
    {
        "day": 80, "week": 12, "month": 3, "category": "Interview Prep",
        "title": "Round 2 Prep: Live Framework Construction (45-Min Challenge)",
        "concepts": ["Building framework skeleton from memory", "Base page setup", "conftest.py fixtures", "Config loader and first test execution"],
        "assignment": "Practice building the complete core skeleton of a Playwright/Pytest framework from scratch in 30 minutes without copy-pasting.",
        "deliverable": "interview-vault/speed_framework_skeleton.py",
        "interviewQ": "If given 45 minutes in a live interview to automate a login and dashboard checkout, how do you prioritize your time?",
        "interviewAns": "Minutes 0-10: Set up clean conftest and config. Minutes 10-25: Write 2 modular page components with locators. Minutes 25-35: Write test with assertions. Minutes 35-45: Refactor and run.",
        "timebox": "Theory: 1.0h | Coding: 3.5h | Katas: 1.5h"
    },
    {
        "day": 81, "week": 12, "month": 3, "category": "Interview Prep",
        "title": "Round 3 Prep: System Design for Distributed Test Platforms",
        "concepts": ["Designing test platforms running 5,000 tests in 15 mins", "Sharding across Docker micro-clusters", "S3 report archival", "Celery/SQS queueing"],
        "assignment": "Draw and document an architectural diagram for a distributed test execution engine capable of running 5,000 Playwright tests across multiple PRs.",
        "deliverable": "interview-vault/system_design_test_platform.md",
        "interviewQ": "How do you scale an automated test suite from 100 tests to 10,000 tests without ballooning CI runtimes?",
        "interviewAns": "Apply the test pyramid (pushing checks to API/unit), implement selective test execution (running only impacted tests via git diff), and shard across autoscaling container clusters.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 82, "week": 12, "month": 3, "category": "Interview Prep",
        "title": "Round 4 Prep: Live Debugging & Flaky Scenario Triage",
        "concepts": ["Troubleshooting tree articulation", "Container vs local macOS differences", "DOM hydration races", "Network jitter isolation"],
        "assignment": "Conduct a recorded 60-minute mock debugging interview explaining troubleshooting trees for 5 classic flaky scenarios.",
        "deliverable": "interview-vault/mock_debugging_recordings.md",
        "interviewQ": "A test fails 1 out of 10 times in CI due to locator timeout, but passes every time locally. Explain your exact troubleshooting steps.",
        "interviewAns": "Walk through: (1) Pull Playwright trace artifact, (2) Inspect CPU/RAM load on CI runner, (3) Check font/viewport differences, (4) Inspect network tab for delayed hydration responses.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 83, "week": 12, "month": 3, "category": "Career Strategy",
        "title": "Resume & Remote Portfolio Engineering",
        "concepts": ["Quantifying engineering impact", "Removing task-based descriptions", "Pinning the 3 flagship repos", "Formatting for ATS scanners"],
        "assignment": "Rewrite resume bullet points to emphasize business metrics (reduced CI runtime from 3.5h to 18m, 1.2% flakiness, 300+ parallel tests) and link GitHub repos.",
        "deliverable": "portfolio/resume_sdet_20lpa_remote.pdf",
        "interviewQ": "How do you present 1-3 years of manual/junior QA experience when targeting a 20 LPA Senior SDET role?",
        "interviewAns": "Highlight your deep understanding of defect lifecycles and business edge cases, while showcasing your 3 enterprise GitHub repositories as concrete proof of advanced coding ability.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 84, "week": 12, "month": 3, "category": "Career Strategy",
        "title": "Day 84 Milestone: Application Launch & 20 LPA Offer Closure",
        "concepts": ["Targeting 30 remote-first product companies", "Cold outreach to SDET engineering managers", "Tracking application pipeline", "Closing 20 LPA fixed offers"],
        "assignment": "Launch targeted applications to 30 remote product companies with personalized cover letters linking directly to your GitHub portfolio and Allure live demos.",
        "deliverable": "portfolio/applications_pipeline_tracker.xlsx",
        "interviewQ": "Why are you looking for a remote-first product company and what is your fixed compensation expectation?",
        "interviewAns": "State clearly: 'I thrive in autonomous, documentation-first asynchronous engineering cultures. Based on my ability to architect scalable test systems and CI pipelines, my target is 20 LPA fixed in hand.'",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 85, "week": 13, "month": 3, "category": "Remote Career & Finance",
        "title": "Remote Contract Architecture, Global Invoicing & Tax Mechanics",
        "concepts": ["W-8BEN form for US clients", "Contractor vs FTE agreements", "Invoicing via Deel / Remote / Wise", "Section 44ADA 50% presumptive taxation"],
        "assignment": "Set up a mock contractor invoice template with SWIFT/BIC codes, LUT registration checklist, and Section 44ADA tax calculation sheet.",
        "deliverable": "portfolio/day85_remote_contractor_tax_pack.pdf",
        "interviewQ": "How do you handle independent contractor agreements, currency conversion risks, and export compliance when working remotely for US/EU firms?",
        "interviewAns": "I operate under standard B2B contractor agreements with payment via Deel/Wise in USD/EUR. In India, software services exported qualify as zero-rated under GST LUT, with income tax efficiently filed under Section 44ADA (50% presumptive expense allowance).",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 86, "week": 13, "month": 3, "category": "Asynchronous Workflows",
        "title": "Asynchronous Engineering & Loom/PR Communication Mastery",
        "concepts": ["RFC framework design process", "Asynchronous PR descriptions", "Loom video walkthrough blueprints", "Cross-timezone handoffs (US/EU to IST)"],
        "assignment": "Write a production RFC document proposing a migration from Selenium to Playwright with cost/benefit analysis, and record a 4-minute mock Loom script.",
        "deliverable": "portfolio/day86_architecture_rfc_playwright_migration.md",
        "interviewQ": "How do you ensure rapid engineering velocity and prevent communication bottlenecks in a remote team spanning 12-hour timezone differences?",
        "interviewAns": "By practicing strict asynchronous hygiene: self-contained PRs with context, video reproduction traces for bugs, clear Definition of Done, and daily thread updates before signing off, eliminating meeting dependencies.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 87, "week": 13, "month": 3, "category": "Interview Gauntlet",
        "title": "Take-Home Assignment Speedrun: 24-Hour Production Test Harness",
        "concepts": ["Take-home evaluation rubrics", "Time allocation: skeleton in 2h, core tests in 4h, CI/CD in 2h", "The 1-line Docker rule", "Defensive README writing"],
        "assignment": "Complete a full take-home assignment simulation: build a Dockerized Playwright + API test harness with GitHub Actions, Allure report, and custom fixtures under a 6-hour time limit.",
        "deliverable": "take-home-simulations/fintech-payment-harness/",
        "interviewQ": "What do you prioritize when given a 48-hour take-home automation assignment by a hiring team?",
        "interviewAns": "I prioritize: (1) 1-line reproducible execution via Docker, (2) rock-solid test design with clean assertions over superficial count, (3) CI pipeline with green badge, and (4) an exceptional README with architecture diagram, design trade-offs, and assumptions.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 88, "week": 13, "month": 3, "category": "System Design",
        "title": "Test Architecture System Design: Distributed Execution on K8s & AWS",
        "concepts": ["High-scale test infrastructure design", "Dynamic browser provisioning with KEDA on K8s", "AWS Spot instance cost optimization", "S3 test artifact offloading"],
        "assignment": "Draw and document the end-to-end system design for an enterprise QA platform handling 100 microservices, sharded test runners, Redis task queues, and Grafana quality dashboards.",
        "deliverable": "portfolio/day88_system_design_test_infrastructure.png",
        "interviewQ": "How would you design a test automation infrastructure that runs 20,000 E2E tests on every pull request within a 10-minute SLA?",
        "interviewAns": "I would implement: (1) Test Impact Analysis (TIA) via git diff, (2) Sharding suites across dynamic container runners on K8s spot instances with KEDA, (3) API-seeded state and storage_state caching, and (4) Headless execution with network interception blocking heavy non-essential assets.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 89, "week": 13, "month": 3, "category": "Career Strategy",
        "title": "Live Behavioral & Counter-Offer Negotiation Gauntlet",
        "concepts": ["STAR storytelling for Senior SDETs", "Defending 20 LPA fixed in-hand floor", "Handling down-leveling attempts", "Counter-offer navigation"],
        "assignment": "Write out 5 complete STAR stories for: (1) Critical production bug prevented, (2) Resolving developer pushback on quality gates, (3) Eradicating flaky tests, (4) Mentoring engineers on Playwright/MCP, (5) Automating a high-risk security/auth flow.",
        "deliverable": "portfolio/day89_behavioral_star_playbook.md",
        "interviewQ": "Your current salary is 6 LPA. How do you justify asking for 20 LPA fixed with only 2.5 years of experience?",
        "interviewAns": "I evaluate compensation based on the market value of the engineering outcomes I deliver, not historical pay. I design production frameworks from scratch, manage CI/CD pipelines, eliminate flakiness, and integrate AI/MCP capabilities. Companies paying 20 LPA do so because I operate autonomously without needing senior oversight.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    },
    {
        "day": 90, "week": 13, "month": 3, "category": "Career Strategy",
        "title": "Day 90 Milestone: Final Offer Acceptance & Day 1 Remote Onboarding Protocol",
        "concepts": ["Offer letter due diligence", "Background verification (BGV) checklist for remote workers", "Home workstation ergonomics", "First 30-60-90 days game plan in remote PBC"],
        "assignment": "Build your complete 'First 30 Days Remote SDET Onboarding Blueprint' outlining how you will audit the existing test suite, identify top 5 flakes, set up local environments, and ship your first automated PR in Week 1.",
        "deliverable": "portfolio/day90_first_30_days_sdet_blueprint.md",
        "interviewQ": "What will your first 30 days look like if we hire you as our SDET?",
        "interviewAns": "Week 1: Set up local environments, review architecture docs, and ship a low-risk PR to validate CI pipelines. Week 2: Map the test pyramid, audit flaky tests, and shadow developers to identify test data bottlenecks. Weeks 3-4: Build reusable fixtures, automate high-risk P0 regressions, and introduce CI quality gates with clear documentation.",
        "timebox": "Theory: 2.0h | Coding: 2.5h | Katas: 1.0h"
    }
]

try:
    from build_dataset import DAILY_ACTIVITIES
    for d in days_data:
        if d["day"] in DAILY_ACTIVITIES:
            act = DAILY_ACTIVITIES[d["day"]]
            d["theory_topics"] = act["theory_topics"]
            d["coding_topics"] = act["coding_topics"]
            d["katas_topics"] = act["katas_topics"]
            d["kata_challenge"] = act["kata_challenge"]
except ImportError:
    pass

with open("days_dataset.json", "w", encoding="utf-8") as f:
    json.dump(days_data, f, indent=2)

print(f"Successfully generated comprehensive {len(days_data)} days dataset with Theory, Coding, and Katas.")
