import csv

def main():
    file = open('res/generated.csv')
    csv.reader(file)
    file.close()

if __name__ == '__main__':
    main()