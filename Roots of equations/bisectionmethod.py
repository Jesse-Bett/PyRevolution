# User enters the equation
equation = input('Enter your equation:\n')

# User enters tolerance
x0 = input("Please enter the value for tolerance:\n")
tol = float(x0)

# User enters the number of iterations
x1 = input("Please enter the number of iterations:\n")
iter = int(x1)

# User enters  the upper limit
x2 = input("Please enter your upper limit:\n")
xu = int(x2)

# User enters the lower limit
x3 = input("Please enter your lower limit:\n")
xl = int(x3)


def f(x):
    return eval(equation)


def bisection_method(xl, xu, iter, tol):
    if f(xl) * f(xu) > 0:

        # end function, no root.

        print("No root found.")

    else:

        while (xu - xl) / 2.0 > tol:

            midpoint = (xu + xl) / 2.0

            if f(midpoint) == 0:

                return (midpoint)  # The midpoint is the x-intercept/root.I

            elif f(xl) * f(midpoint) < 0:  # Increasing but below 0 case

                xu = midpoint

            else:

                xl = midpoint

        return (midpoint)


answer = bisection_method(xl, xu, iter, tol)

print("Answer:", round(answer, 4))
