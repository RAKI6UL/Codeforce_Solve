
def main():
    R = input() 
    R = dict.fromkeys(R)  

    if len(R) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


if __name__ == "__main__":
    main()