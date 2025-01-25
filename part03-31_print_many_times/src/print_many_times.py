# Write your solution here
def print_many_times(text:str, times:int):
    counter=0
    while counter <times:
        print(text)
        counter +=1
if __name__ == "__main__":  
    print_many_times("python", 5)