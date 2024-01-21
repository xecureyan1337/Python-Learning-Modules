from time import sleep

class RemoveDuplicates():
    def __init__(self, range=int(input("Enter range: "))):
        self.range = range

    def get_range(self):
        return self.range
    
    def run(self):

        the_range = self.get_range()
        num_list = []

        for num in range(the_range):
            num = int(input("Enter number: "))
            num_list.append(num)
        
        print(f"List with its duplicates: {num_list}")

        num_list = list(dict.fromkeys(num_list))

        print(f"List without its duplicates: {num_list}")


if __name__ == "__main__":
    mynum = RemoveDuplicates(5)
    mynum.run()