import time

f = open("f.txt", "r")
v = f.read().split("\n")
while v.count("") > 0:
    v.remove("")

def sequential_search(p):
    for i in range(len(v)):
        if v[i] == p:
            return i 
    return -1

def binary_search(p):
    if len(v) == 0:
        return -1
    lo = 0
    hi = len(v) - 1 
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        if v[mid] <= p:
            lo = mid
        else:
            hi = mid - 1
    if v[lo] == p:
        return lo 
    return -1

def bubble_sort():
    for i in range(len(v) - 2, 0, -1):
        joker = False
        for j in range(0, i + 1):
            if v[j] > v[j + 1]:
                v[j + 1], v[j] = v[j], v[j + 1]
                joker = True
        if not joker:
            break

def insertion_sort():
    for i in range(1, len(v)):
        j = i 
        while j > 0 and v[j] < v[j - 1]:
            v[j], v[j - 1] = v[j - 1], v[j]
            j -= 1

def shell_sort():
    interval = 1
    while interval * 3 + 1 < len(v):
        interval = interval * 3 + 1
    while interval > 0:
        for i in range(interval, len(v)):
            j = i 
            while j - interval >= 0 and v[j] < v[j - interval]:
                v[j], v[j - interval] = v[j - interval], v[j]
                j -= interval
        interval //= 3
    
while True:
    print(chr(27) + "[2J")
    print("Menu")
    print("1. Add")
    print("2. Remove")
    print("3. Search")
    print("4. Show Dex")
    print("5. Quit")
    vi = input()
    if (vi == "1" or vi == "2" or vi == "3" or vi == "4" or vi == "5"):
        if vi == "1":
            print("What pokemon do you want to add to the dex?")
            pokemon = input().lower()
            if binary_search(pokemon) == -1:
                v.append(pokemon)
                while True:
                    print("We need to sort the dex. How would you like to sort? Bubble Sort(1), Insertion Sort(2), or Shell Sort(3)?")
                    smet = input()
                    if smet == "1":
                        start = time.time()
                        bubble_sort()
                        end = time.time()
                        print("Done! The Bubble Sort took " + str((end - start) * 1000) + " milliseconds.")
                        break
                    elif smet == "2":
                        start = time.time()
                        insertion_sort()
                        end = time.time()
                        print("Done! The Insertion Sort took " + str((end - start) * 1000) + " milliseconds.")
                        break
                    elif smet == "3":
                        start = time.time()
                        shell_sort()
                        end = time.time()
                        print("Done! The Shell Sort took " + str((end - start) * 1000) + " milliseconds.")
                        break
                    else:
                        print("That is not a valid sorting method. Try again.")
                        dummy = input()
                with open("f.txt", "r+") as ff:
                    ff.truncate(0)
                f2 = open("f.txt", "w")
                for i in v:
                    f2.write(i + "\n")
                f2.close()
                print("added " + pokemon + " to the dex!")
            else:
                print("You already caught a " + pokemon + ".")
            dummy = input()
        elif vi == "2":
            print("Release which Pokemon?")
            pokemon = input().lower()
            if binary_search(pokemon) == -1:
                print("You never caught a " + pokemon + ".")
            else:
                v.remove(pokemon)
                with open("f.txt", "r+") as ff:
                    ff.truncate(0)
                f2 = open("f.txt", "w")
                for i in v:
                    f2.write(i + "\n")
                f2.close()
                print("Bye bye! " + pokemon + " was released")
            dummy = input()
        elif vi == "3":
            print("Which Pokemon do you want to find?")
            pokemon = input().lower()
            while True:
                print("Sequential Search(1) or Binary Search(2)?")
                met = input()
                if met == "1":  
                    start = time.time()
                    idx = sequential_search(pokemon)
                    end = time.time()
                    print("Search over! The sequential search took " + str((end - start) * 1000) + " milliseconds.")
                    if idx == -1:
                        print(pokemon + " is not in your dex.")
                    else:
                        print("lexicographically, " + pokemon + " is number " + str(idx + 1) + " in your dex.")
                    break
                elif met == "2":
                    start = time.time()
                    idx = binary_search(pokemon)
                    end = time.time()
                    print("Search over! The binary search took " + str((end - start) * 1000) + " milliseconds.")
                    if idx == -1:
                        print(pokemon + " is not in your dex.")
                    else:
                        print("lexicographically, " + pokemon + " is number " + str(idx + 1) + " in your dex.")
                    break
                else:
                    print("That is not a valid method. Try again.")
                    dummy = input()
            dummy = input()
        elif vi == "4":
            for i in v:
                print(i)
            dummy = input()
        else: 
            break
    else:
        print("Invalid command. Enter to continue")
        dummy = input()
