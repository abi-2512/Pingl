import streamlit as st
from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

# Define the Streamlit app
def main():
    st.title("Pingl Interpreter")
    st.markdown("""
    **Pingl** is a custom programming language with simple syntax (in english), supporting:
    - **Arithmetic** (add, subtract, etc.)
    - **Loops** (repeat n times)
    - **Conditionals** (if-else)
    - **Object-Oriented Programming**
    """)

    # Text input area for AlphaLang code
    st.subheader("Write Your Pingl Code")
    code = st.text_area(
        "Type your Pingl code here:", 
        value="""
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
        """,
        height=300
    )

    if st.button("Run Code"):
        # Process the code using AlphaLang components
        try:
            st.subheader("Execution Results")
            # Step 1: Tokenize the code
            lexer = Lexer(code)
            tokens = lexer.tokenize()

            # Step 2: Parse the tokens
            parser = Parser(tokens)
            ast = parser.parse()

            # Step 3: Execute the code
            interpreter = Interpreter()
            output = []
            original_print = print  # Override print for capturing output

            def capture_print(*args, **kwargs):
                output.append(" ".join(map(str, args)))

            print = capture_print  # Redirect print
            interpreter.execute(ast)
            print = original_print  # Restore original print

            # Display the results
            st.code("\n".join(output))
        except Exception as e:
            st.error(f"Error: {str(e)}")

    # Debugging options
    with st.expander("Debugging"):
        if st.button("Tokenize"):
            lexer = Lexer(code)
            tokens = lexer.tokenize()
            st.write("Tokens:")
            st.json(tokens)

        if st.button("Parse"):
            lexer = Lexer(code)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            ast = parser.parse()
            st.write("Abstract Syntax Tree (AST):")
            st.json(ast)

if __name__ == "__main__":
    main()