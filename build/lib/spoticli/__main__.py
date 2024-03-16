from blessed import Terminal

def main():
    term = Terminal()
    with term.location(0, term.height - 1):
        print('This is ' + term.underline('underlined') + '!', end='')

if __name__ == '__main__':
    main()