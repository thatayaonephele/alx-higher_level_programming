#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    x = 0
    z = sorted(dir(hidden_4))
    y = len(z)
    while x < y:
        if z[x][0] != '_':
            print(z[x])
        x = x + 1
