#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    fulldir = dir(hidden_4)
    for i in range(0, len(fulldir)):
        if "__" not in fulldir[i]:
            print(fulldir[i])
