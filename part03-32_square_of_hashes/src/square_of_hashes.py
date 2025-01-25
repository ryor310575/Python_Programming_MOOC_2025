# Write your solution here
# You can test your function by calling it within the following block
def hash_square(side:int):
    high=0
    width=0
    to_print=""
    while high<side:
        while width<side:
            to_print=to_print +"#"
            width+=1
        print(to_print)
        high+=1

if __name__ == "__main__":
    hash_square(5)