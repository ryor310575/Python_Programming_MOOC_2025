# Write your solution here
def chessboard(side:int):
    high=0
    mem_pos=0
    mem_line=1
    while high<side:
        if mem_line==0:
            mem_line=1
        else:
            mem_line=0
        mem_pos = mem_line
        width = 0
        to_print = ""
        while width<side:
            if mem_pos==0:
                mem_pos=1
            else:
                mem_pos=0
            to_print=to_print+str(mem_pos)
            width+=1
        print(to_print)
        high+=1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
