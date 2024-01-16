# command line arguments are those values that are passed during calling of program along with the calling statement
import sys

def my_program_name():
    program = sys.argv[0]
    print(program)

def simple_argv():
    if len(sys.argv) < 2:
        print("You need to pass one argument")
        print(sys.argv) # list data type 
        sys.exit(1)

    print(f"Welcome, this your argument: {sys.argv[1]}")

# example real case
def simple_calc():
    if len(sys.argv) < 2:
        print("You need to pass one argument")
        sys.exit(1)

    x = sys.argv[1]
    y = sys.argv[3]
    z = int(x) + int(y)
    print(f"{x} + {y} = {z}")

if __name__ == "__main":
    my_program_name()
    simple_argv()
    simple_calc()
