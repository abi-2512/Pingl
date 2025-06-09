
---

# 🧠 Pingl: English-like Programming Language & Interpreter

**Pingl** is a simple, expressive, and beginner-friendly programming language with **English-like syntax**. This project features an interpreter for Pingl, complete with a web-based IDE built using **Streamlit**.

---

## 💡 What is Pingl?

Pingl is a toy programming language designed for readability and accessibility, especially for newcomers. Think of it as Python meets pseudocode — you write programs in plain English, and Pingl interprets them into real logic. For now, it supports basic statements, but I plan to add more.

### ✅ Supported Features:

* **Arithmetic**: `add`, `subtract`, `set`, etc.
* **Conditionals**: `if`, `else`, `is greater than`, etc.
* **Loops**: `repeat n times`
* **OOP**: Classes, properties, and method calls (WIP)

---

## 🧪 Example Pingl Code

```text
set x to 5
repeat 3 times:
  display x
  add 2 to x

if x is greater than 15:
  display "x is big"
else:
  display "x is small"

class Person:
  set name to "John"
  define greet:
    display "Hello, my name is " + name

set p to new Person
call greet on p
```

---

## 🚀 Running the App

### 🧰 Requirements

* Python 3.7+
* `streamlit`
* Your custom modules:

  * `Lexer.py`
  * `Parser.py`
  * `Interpreter.py`

### 🔧 Setup

```bash
git clone https://github.com/yourusername/pingl-interpreter.git
cd pingl-interpreter
pip install -r requirements.txt
streamlit run app.py
```

### 🖥️ Usage

* Type your Pingl code in the editor.
* Click **"Run Code"** to interpret and execute it.
* Use the **Debugging** panel to:

  * Tokenize your code
  * View the AST

---

## 🧱 Project Structure

```
.
├── pingl_app.py               # Streamlit frontend
├── Lexer.py                   # Converts Pingl code into tokens
├── Parser.py                  # Converts tokens into AST
├── Interpreter.py             # Executes AST logic
├── README.md                  # You're reading this
└── requirements.txt           # Streamlit and any future deps
```

---

## 🧠 Internals

* **Lexer**: Converts English-like commands into token streams.
* **Parser**: Transforms tokens into an Abstract Syntax Tree.
* **Interpreter**: Walks the AST and evaluates Pingl logic.
* **Streamlit UI**: Web interface for code input, execution, and debugging.

---


## 🌱 Future Improvements

This is an early prototype of the Pingl language. Here are a few realistic improvements that would make it more stable and usable:

### 🔧 Core Fixes

* [ ] **Fix interpreter bugs** — Clean up inconsistent behavior in loops, conditionals, and class methods
* [ ] **Better error messages** — Show user-friendly messages instead of crashing on invalid syntax
* [ ] **Support basic expressions** — Enable arithmetic inside conditionals and assignments (e.g., `set x to 5 + 3`)

### 🛠 Language Features

* [ ] **Allow nested blocks** — Right now, nested loops/conditionals are flaky or unsupported
* [ ] **Add support for simple booleans** — `true`, `false`, and boolean comparisons
* [ ] **Improve method calling** — Make object method definitions and calls more reliable

### 🖥 Frontend & Usability

* [ ] **Live output panel** — Display results immediately below the editor instead of just on click
* [ ] **Editor improvements** — Allow better formatting or syntax help in the code input box

### 🧪 Development Support

* [ ] **Basic test cases** — Write a few tests for the lexer, parser, and interpreter to avoid regressions
* [ ] **Logging/debug mode** — Output the AST or execution steps to help debug complex behavior


---

## 👨‍💻 Author

Created by a developer passionate about **programming languages**, **interpreters**, and making coding more accessible through creative language design.

---

## 📜 License

MIT License — use freely, remix wildly.

---

