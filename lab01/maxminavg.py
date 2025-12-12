import json
"""avg"""
def highest(lst):
    highval = lst[0]
    for num in lst:
        if num > highval:
            highval = num
    return highval

def lowest(lst):
    lowval = lst[0]
    for num in lst:
        if num < lowval:
            lowval = num
    return lowval

def main():
    """main"""
    num = json.loads(input())
    print((highest(num), lowest(num), round(sum(num) / len(num), 2)))


if __name__ == "__main__":
    main()
