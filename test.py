import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, tan, sqrt, exp, log, pi, e
import re


def plot_function():
    """
    Takes user input for a function and displays its graph.
    Supports standard mathematical expressions with x as the variable.
    Example: x, x^2, x**3, sin(x), 2*x+1, etc.
    """
    try:
        # Get user input
        function_str = input("Enter a function (use 'x' as variable, e.g., 'x', 'x^2', 'sin(x)', '2*x+1'): ")
        
        # Convert ^ to ** for exponentiation
        function_str = function_str.replace('^', '**')
        
        # Handle implicit multiplication (e.g., 2x -> 2*x, )x -> )*x)
        function_str = re.sub(r'(\d)([a-zA-Z(])', r'\1*\2', function_str)  # digit followed by letter or (
        function_str = re.sub(r'(\))(\d|[a-zA-Z(])', r'\1*\2', function_str)  # ) followed by digit, letter, or (

        # Get x-axis range from user (with defaults)
        try:
            x_range_input = input("Enter x-axis range (e.g., '-10,10', press Enter for default -10 to 10): ").strip()
            if x_range_input:
                x_min, x_max = map(float, x_range_input.split(','))
            else:
                x_min, x_max = -10, 10
        except ValueError:
            print("Invalid range format. Using default -10 to 10.")
            x_min, x_max = -10, 10

        # Create x values
        x = np.linspace(x_min, x_max, 1000)
        
        # Evaluate the function safely
        try:
            safe_dict = {
                "__builtins__": {},
                "x": x,
                "np": np,
                "sin": np.sin,
                "cos": np.cos,
                "tan": np.tan,
                "sqrt": np.sqrt,
                "exp": np.exp,
                "log": np.log,
                "abs": np.abs,
                "pi": np.pi,
                "e": np.e
            }
            y = eval(function_str, safe_dict)
        except Exception as e:
            print(f"Error evaluating function: {e}")
            return
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2)
        plt.grid(True, alpha=0.3)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.title(f'Graph of y = {function_str}', fontsize=14)
        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=0, color='k', linewidth=0.5)
        
        # Display the plot
        plt.show()
        
    except KeyboardInterrupt:
        print("\nPlotting cancelled.")
    except Exception as e:
        print(f"An error occurred: {e}")


def plot_multiple():
    """
    Allows plotting multiple functions until user quits.
    """
    while True:
        plot_function()
        again = input("\nPlot another function? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    plot_multiple()