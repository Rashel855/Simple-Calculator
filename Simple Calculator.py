import streamlit as st

# ---------- Functions ----------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a % b


# ---------- UI ----------
st.title("🧮 Simple Calculator")

operation = st.selectbox(
    "Choose operation:",
    (
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Modulo",
    ),
)

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter a:", value=0.0)

with col2:
    num2 = st.number_input("Enter b:", value=0.0)


# ---------- Calculate ----------
if st.button("Calculate"):
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)
    else:
        result = modulo(num1, num2)

    st.success(f"Result: {result}")