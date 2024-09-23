def newtons_method(f, f_prime, x0, nmax, epsilon):
    # Initial setup
    x = x0
    fx = f(x)
    print(f"0 {x:.5f} {fx:.5f}")  # Output initial guess

    # Main iteration loop
    for n in range(1, nmax + 1):
        fp = f_prime(x)  # f'(x)
        d = fx / fp  # delta x
        x = x - d  # update x
        fx = f(x)  # f(x) with new x
        print(f"{n} {x:.5f} {fx:.5f}")  # Output current iteration

        # Check convergence
        if abs(d) < epsilon:
            print("convergence")
            return x

    return None  # Return None if no convergence within nmax iterations


# Example usage:
def f(x):
    return x**2 - 4  # Example function x^2 - 4

def f_prime(x):
    return 2*x  # Derivative of the example function

# Initial guess, max iterations, and tolerance
x0 = 1.0
nmax = 10
epsilon = 1e-5

# Call the Newton's method
newtons_method(f, f_prime, x0, nmax, epsilon)
