import sys

def main():
    file_name = None

    try:
        file_name = sys.argv[1]
    except IndexError:
        print "defaulting to g1"
        file_name = 'g1'

    f = open('data/%s.txt' % file_name)
    a = f.readlines()
    f.close()

    print a[0]

if __name__ == '__main__':
    main()