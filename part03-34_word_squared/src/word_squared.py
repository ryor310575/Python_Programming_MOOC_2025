# Write your solution here
def squared(word:str, side:int):
    high=0
    memory=0
    while high<side:
        width=0
        to_print = ""
        while width<side:
            if memory > len(word) - 1:
                memory = 0
            to_print= to_print + word[memory]
            memory+=1
            width+=1
        print(to_print)
        high+=1
if __name__ == "__main__":
    squared("ab", 3)
