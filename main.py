import streamlit as st


def calculator():

    while True:

        st.title("SimpleCalculator")

        num1 = st.number_input("Enter first number", key="num1")

        num2 = st.number_input("Enter second number", key="num2")




        operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])


        if st.button("Calculate"):

            if operation == "Addition":

                result = num1 + num2

            elif operation == "Subtraction":

                result = num1 - num2

            elif operation == "Multiplication":

                result = num1 * num2

            elif operation == "Division":

                if num2 != 0:

                    result = num1 / num2

                else:

                    result = "Error: Division by zero is not allowed"

            st.write("Result:", result)


        quit = st.selectbox("Do you want to quit?", ["N", "Y"])


        if quit == "Y":

            st.write("GOODBYE!")

            break  # exit the loop when user chooses to quit


if __name__ == "__main__":

    calculator()

