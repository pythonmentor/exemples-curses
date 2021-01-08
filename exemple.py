import curses

# start an application
stdscr = curses.initscr() # Détermine le type de terminal, configure le terminal et crée diverses structures de données internes.
curses.noecho() # Désactive l'écho automatique des touches à l'écran
curses.cbreak() # Suppression du tampon
stdscr.keypad(True) # Activation de la gestion des touches spéciales
curses.start_color() # Active la gestion des couleurs

stdscr.addstr(0, 0, "Une première chaine de caractère avec curses.")
stdscr.getkey()

# stop an application
stdscr.keypad(False)
curses.nocbreak()
curses.echo()
curses.endwin()