# How-Cpython-Works

## 0. Define an evaluand
We're going to define the function printing out "Hello, world!" and set it to an evaluand for the sake of simplicity.

## 1. Lexical Analysys
Lexical analysis is the first phase in the compiler designing which groups a stream of letters or sounds into sets of units that represent meaningful syntax.
```
❯ python lexical_analysis.py
```
<details><summary>Output</summary>

```rb
[TokenInfo(type=62 (ENCODING), string='utf-8', start=(0, 0), end=(0, 0), line=''),
TokenInfo(type=1 (NAME), string='print', start=(1, 0), end=(1, 5), line='print("Hello, world!")'),
TokenInfo(type=54 (OP), string='(', start=(1, 5), end=(1, 6), line='print("Hello, world!")'),
TokenInfo(type=3 (STRING), string='"Hello, world!"', start=(1, 6), end=(1, 21), line='print("Hello, world!")'),
TokenInfo(type=54 (OP), string=')', start=(1, 21), end=(1, 22), line='print("Hello, world!")'),
TokenInfo(type=4 (NEWLINE), string='', start=(1, 22), end=(1, 23), line=''),
TokenInfo(type=0 (ENDMARKER), string='', start=(2, 0), end=(2, 0), line='')]
```
</details>
<br>

## 2. Syntax Analysis
Syntax analysis is the second phase in compiler designing in which the given input string is checked for the confirmation of rules and structure of the formal grammar.
```
❯ python syntax_analysis_readable.py
```
<details><summary>Output</summary>

```rb
<class 'ast.Module'>
    <class 'ast.Expr'>: 1
        <class 'ast.Call'>: 1
            <class 'ast.Name'>: 1
                <class 'ast.Load'>
            <class 'ast.Constant'>: 1
```
</details>
<br>
If you want it to be visualized, you can try the following.

```
❯ brew install graphviz
❯ pip install graphviz
❯ python syntax_analysis_visualizable.py
```
You'll see ast.png saved.

![AST](ast.png "AST")

<br>

## 3. Bytecode
Bytecode is computer object code that an interpreter converts into binary machine code which is created based on the result of syntax analysis.
```
❯ python bytecode.py
```
<details><summary>Output</summary>

```rb
              0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ('Hello, world!')
              4 CALL_FUNCTION            1
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
```
</details>
<br>

## 4. Interpretation and execution by PVM
Bytecode is interpreted and executed by PVM.
If you want to know how interpretation performs, look through <a href="https://github.com/python/cpython/blob/main/Python/ceval.c">ceval.c</a>. During a Python function call, Python will call an evaluating C function to interpret that function's code, according to <a href="https://docs.python.org/ja/3.11/whatsnew/3.11.html#inlined-python-function-calls">the official documentation</a>.


## Your Python code runs fast?
Bytecode helps think about an effect on runtime. In this case, we compare two functions calculating seconds in a year. 
```
def yearByLocalName():
    seconds_per_day = 86400
    return seconds_per_day * 365

def yearByGlobalName():
    return 86400 * 365
```

```
❯ python comparison.py
```
<details><summary>Output</summary>

```rb
              0 LOAD_CONST               1 (86400)
              2 STORE_FAST               0 (seconds_per_day)
              4 LOAD_FAST                0 (seconds_per_day)
              6 LOAD_CONST               2 (365)
              8 BINARY_MULTIPLY
             10 RETURN_VALUE

              elapsed time: 0.000005007 [sec]

              0 LOAD_CONST               1 (31536000)
              2 RETURN_VALUE            

              elapsed time: 0.000002861 [sec]
```
</details>
<br>
As you can see, local names are faster than global ones. Wanna try your own code?