import curses

def main(stdscr):
    stdscr.addstr(0, 0, "Une première chaine de caractère avec curses.")
    stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(main)