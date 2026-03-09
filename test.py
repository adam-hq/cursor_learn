import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

        # Create x values
        x = np.linspace(-10, 10, 1000)
        
        # Evaluate the function safely
        try:
            y = eval(function_str, {"__builtins__": {}}, {"x": x, "np": np})
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


if __name__ == "__main__":
    plot_function()