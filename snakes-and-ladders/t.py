

def main():
    current = 0
    while current <= 100:
        current = add(current)
        current += 30
        print(current)

        
def add(current):
    current += 30
    return current

main()