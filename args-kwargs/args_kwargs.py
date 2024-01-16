# *args (non keyword arguments) / magic variable is used as a parameter to the function  (tuple data type)
# this argument is good to use when programmer doesn't know the number of arguments of function
# *kwargs is collection data type

class ArgsKwargs():

    def __init__(self):
        self.description = "Args is tuple data type and used when user doesn't know specific arguments as well as Kwargs but it is collection data type"

    def call_name(*names):
        for name in names:
            print(f"Hi, {name}")
    
    def book_lists(**booklists):
        print("I have book lists below:")
        print(booklists)
    
if __name__ == "__main__":
    args_object = ArgsKwargs()
    args_object.call_name("Tedi", "Rudi", "Sendi")

    data = 4,5,3,2,1

    def average(*data):
        data_length = len(data)
        data_sum = 0
        for i in data:
            data_sum = data_sum + i
        average     = data_sum / data_length
        print(average)
    
    average(1,1,1,1,1)
