
def choose(col, row): # note no dependencies on any of the prior code
     if row in (0, col):
         return 1
     return choose(col-1, row-1) + choose(col-1, row)


if __name__ == "__main__":

    print("Pascal's Triangle")
    for myrow in range(0,3):
        for mycol in range(0,myrow+1):
            print (choose(myrow,mycol),end=" ",flush=True)
        print()


