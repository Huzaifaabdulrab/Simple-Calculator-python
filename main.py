# Importing Streamlit for building the UI
import streamlit as st

# Function to create a simple calculator app
def calculator():
    # Title of the Calculator application
    st.title("Simple Calculator")
    st.write("Enter two numbers and choose an operation")

    # Creating two columns for user input
    col1, col2 = st.columns(2)

    # Taking the first number input in the first column
    with col1:
        num1 = st.number_input("Enter first number", value=0)

    # Taking the second number input in the second column
    with col2:
        num2 = st.number_input("Enter second number", value=0)

    # Selecting the operation
    operation = st.radio("Choose operator", ["Addition (+)", "Subtraction (-)", "Multiplication (x)", "Division (/)"])

    # Button to trigger the calculation
    if st.button("Calculate"):
        try:
            # Perform calculation based on selected operation
        #Addition (+)
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
        #Subtraction (-)
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
        #Multiplication (x)
            elif operation == "Multiplication (x)":
                result = num1 * num2
                symbol = "x"
        # Division (/)
            elif operation == "Division (/)":
                # Handling division by zero error
                if num2 == 0:
                    st.error("Error: Division by zero is not allowed!")
                    result = None  # Avoid performing division
                else:
                    result = num1 / num2
                    symbol = "/"

            # Display the result only if it is valid
            if result is not None:
                st.success(f"Result: {num1} {symbol} {num2} = {result}")

        # Handling any unexpected errors
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Ensure the function runs when executing the script
if __name__ == "__main__":
    calculator()
