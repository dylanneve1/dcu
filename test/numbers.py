def main(args):
    return 0

if __name__ == '__main__':
    import sys
    
    a = 20
    b = 10
    c = 15
    d = 5
    answer = 0
    
    answer = c * b
    print "Value of c * b is", answer
    
    answer = (c + d) / b
    print "Value of (c + b) / b is", answer
    
    sys.exit(main(sys.argv))
