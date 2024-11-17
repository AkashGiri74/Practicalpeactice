def create_f():
    filename=input("enter file name")
    with open(filename,"w") as file:
        print(f"{file} created successfullly")
    return filename
def writee(filename):
    with open(filename,"w") as file:
      str=input("enter content to write")
      file.write(str)
def readdd(filename):
        with open(filename,"r") as file:
            content=file.read()
            print(content)

def closee():
    print("file close")

        
        
def main():
    filename=""
    while True:
        print("1.crate")
        print("2.write")
        print("3.read")
        print("4.close")
        print("5.exit")

        ch=int(input("enter your choice:"))
        if ch==1:
            filename=create_f()
        elif ch==2:
            writee(filename)
        elif ch==3:
            readdd(filename)
        elif ch==4:
            closee()
        elif ch==5:
            print("exiting the program!!!!!!!")
            break
            
if __name__=="__main__":
    main()
