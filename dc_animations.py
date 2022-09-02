import curses
import time



def attackEnderman(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
        
  stdscr.addstr(y - 2, x, "     ▄        ")
  stdscr.addstr(y - 1, x, "▄   ╱█╲       ")
  stdscr.addstr(y, x, "█╱ ▕  ▏      ")

  stdscr.refresh()
  time.sleep(1)

  stdscr.addstr(y - 2, x, "     ▄        ") 
  stdscr.addstr(y - 1, x, "▄   ╱█╲       ")
  stdscr.addstr(y, x, "█──▕  ▏         ")

  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 2, x, "     ▄        ")
  stdscr.addstr(y - 1, x, "▄   ╱█╲       ")
  stdscr.addstr(y, x, "█╱ ▕  ▏         ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()

def endermanAttack(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
       
  stdscr.addstr(y - 2, x, "     ▄        ")
  stdscr.addstr(y - 1, x, "▄   ╱█╲       ")
  stdscr.addstr(y, x,  "█╱ ▕  ▏       ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 2, x, "     ▄        ") 
  stdscr.addstr(y - 1, x, "▄  ▔▔█╲       ")
  stdscr.addstr(y, x, "█╱ ▕  ▏       ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 2, x, "     ▄        ")
  stdscr.addstr(y - 1, x, "▄   ╱█╲       ")
  stdscr.addstr(y, x, "█╱ ▕  ▏       ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()


def attackCreeper(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
        
  stdscr.addstr(y - 1, x, "▄    ▄         ")
  stdscr.addstr(y, x, "█╱   █         ")
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄    ▄         ") 
  stdscr.addstr(y, x, "█──  █         ")
  
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄    ▄          ")
  stdscr.addstr(y, x, "█╱   █         ")
  
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()

def creeperExplode(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
                   
  stdscr.addstr(y - 1, x, "▄    ▄          ")
  stdscr.addstr(y, x, "█╱   █         ")
  stdscr.refresh()
  time.sleep(0.5)
  
  stdscr.addstr(y - 1, x, "▄   ░▒░       ") 
  stdscr.addstr(y, x, "█╱  ░▒▓░          ")
  
  stdscr.refresh()
  time.sleep(0.5)
  
  stdscr.addstr(y - 1, x, "▄   ░░ ░      ")
  stdscr.addstr(y, x, "█╱  ░ ░  ░          ")
  
  stdscr.refresh()
  time.sleep(0.5)
  
  stdscr.addstr(y -1, x, "▄             ")
  stdscr.addstr(y, x, "█╱            ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()

def creeperEscape(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
            
  stdscr.addstr(y - 1, x, "▄    ▄          ")
  stdscr.addstr(y, x, "█╱   █         ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.addstr(y - 1, x - 1, "▄     ▄          ")
  stdscr.addstr(y, x - 1, "█╱    █         ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.addstr(y - 1, x - 2, "▄      ▄")
  stdscr.addstr(y, x - 2, "█╱     █")
  stdscr.refresh()
  time.sleep(1)
  stdscr.clear()

def attackWitch(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.addstr(y - 1, x, "▄   ▲         ")
  stdscr.addstr(y, x, "█╱  █          ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄   ▲         ")
  stdscr.addstr(y, x, "█── █          ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄   ▲         ")
  stdscr.addstr(y, x, "█╱  █          ")
  
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()

def witchAttack(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.addstr(y - 1, x, "▄         ▲   ")
  stdscr.addstr(y, x, "█╱        █    ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄       σ  ▲   ")
  stdscr.addstr(y, x, "█╱         █   ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄         ▲   ")
  stdscr.addstr(y, x, "█╱  σ     █     ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.addstr(y - 1, x, "▄   ░       ▲   ")
  stdscr.addstr(y, x, "█╱ ░ ░      █    ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄         ▲   ")
  stdscr.addstr(y, x, "█╱        █    ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()

def attackSpider(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
       
  stdscr.addstr(y - 1, x, "▄             ")
  stdscr.addstr(y, x, "█╱  ▄▅        ")
  stdscr.addstr(y + 1,  x,  "    ╵╵╵       ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄             ") 
  stdscr.addstr(y, x, "█── ▄▅       ")
  stdscr.addstr(y + 1, x, "    ╵╵╵       ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄             ")
  stdscr.addstr(y, x, "█╱  ▄▅        ")
  stdscr.addstr(y + 1, x, "    ╵╵╵       ")
  stdscr.refresh()
  time.sleep(0.5)

def spiderAttack(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
  stdscr.addstr(y - 1, x, "▄             ")
  stdscr.addstr(y, x, "█╱      ▄▅        ")
  stdscr.addstr(y + 1, x, "        ╵╵╵   ")
  stdscr.refresh()
  time.sleep(0.5)


  stdscr.addstr(y - 1, x, "▄     ▄▅      ") 
  stdscr.addstr(y, x, "█╱    ╵╵╵          ")
  stdscr.addstr(y + 1, x, "            ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 2, x, "    ▄▅        ")
  stdscr.addstr(y - 1, x, "▄   ╵╵╵       ")
  stdscr.addstr(y, x, "█╱                 ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 2, x, "                 ")
  stdscr.addstr(y - 1, x, "▄  ▄▅         ")
  stdscr.addstr(y, x, "█╱ ╵╵╵              ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄                ")
  stdscr.addstr(y, x, "█╱    ▄▅             ")
  stdscr.addstr(y + 1, x, "      ╵╵╵         ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()


def attackSkeleton(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
        
  curses.curs_set(0)
  stdscr.addstr(y - 1, x, "▄    ▄        ")
  stdscr.addstr(y, x, "█╱  (█        ")

  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄    ▄        ") 
  stdscr.addstr(y, x, "█── (█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄    ▄        ")
  stdscr.addstr(y, x, "█╱  (█        ")
  stdscr.refresh()
  time.sleep(0.5)

def skeletonAttack(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
  stdscr.addstr(y - 1, x, "▄          ▄    ")
  stdscr.addstr(y, x, "█╱        (█    ")
  
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄          ▄   ") 
  stdscr.addstr(y, x, "█╱       (>█   ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄          ▄   ")
  stdscr.addstr(y, x, "█╱  <-    (█   ")
  stdscr.refresh()
  time.sleep(0.5)
  
  stdscr.addstr(y - 1, x, "▄          ▄   ")
  stdscr.addstr(y, x,  "█╱        (█   ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()

def attackZombie(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
        
  stdscr.addstr(y -  1, x, "▄    ▄         ")
  stdscr.addstr(y, x, "█╱  ▔█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄    ▄         ") 
  stdscr.addstr(y, x, "█── ▔█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄    ▄         ")
  stdscr.addstr(y, x, "█╱  ▔█        ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()

def zombieAttack(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
        
  stdscr.addstr(y - 1, x, "▄       ▄      ")
  stdscr.addstr(y, x, "█╱     ▔█     ")

  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄    ▄         ")
  stdscr.addstr(y, x, "█╱  ▔█       ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄  ▄           ")
  stdscr.addstr(y, x, "█╱▔█         ")
  stdscr.refresh()
  time.sleep(0.5)
  
  stdscr.addstr(y - 1, x, "▄       ▄      ")
  stdscr.addstr(y, x, "█╱     ▔█     ")
  stdscr.refresh()
  time.sleep(0.5) 
  stdscr.clear()


def attackEndermanBow(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
        
  stdscr.addstr(y - 2, x, "               ▄        ")
  stdscr.addstr(y - 1, x, "▄             ╱█╲       ")
  stdscr.addstr(y, x,     "█)           ▕  ▏      ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 2, x, "               ▄        ")
  stdscr.addstr(y - 1, x, "▄             ╱█╲       ")
  stdscr.addstr(y, x,     "█<)          ▕  ▏      ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 2, x, "              ▄        ")
  stdscr.addstr(y - 1, x, "▄            ╱█╲       ")
  stdscr.addstr(y, x,     "█)      ->  ▕  ▏      ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 2, x, "      ▄            ")
  stdscr.addstr(y - 1, x, "▄    ╱█╲           ")
  stdscr.addstr(y, x,     "█)  ▕  ▏    ->  ")
  stdscr.refresh()
  time.sleep(0.5)
  
def endermanAttackBow(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
       
  stdscr.addstr(y - 2, x, "     ▄        ")
  stdscr.addstr(y - 1, x, "▄   ╱█╲       ")
  stdscr.addstr(y, x,  "█) ▕  ▏       ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 2, x, "     ▄        ") 
  stdscr.addstr(y - 1, x, "▄  ▔▔█╲       ")
  stdscr.addstr(y, x, "█) ▕  ▏       ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 2, x, "     ▄        ")
  stdscr.addstr(y - 1, x, "▄   ╱█╲       ")
  stdscr.addstr(y, x, "█) ▕  ▏       ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()
  
def attackCreeperBow(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
        
  stdscr.addstr(y - 1, x, "▄             ▄         ")
  stdscr.addstr(y, x,     "█)            █         ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄             ▄         ") 
  stdscr.addstr(y, x,     "█<)           █         ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄             ▄          ")
  stdscr.addstr(y, x,     "█)     ->     █         ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄             ▄          ")
  stdscr.addstr(y, x,     "█)        ->  █         ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄             ▄         ")
  stdscr.addstr(y, x,     "█)            █         ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()

def attackWitchBow(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.addstr(y - 1, x, "▄             ▲         ")
  stdscr.addstr(y, x,     "█)            █          ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄             ▲         ")
  stdscr.addstr(y, x,     "█<)           █          ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄             ▲         ")
  stdscr.addstr(y, x,     "█)  ->        █          ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄             ▲         ")
  stdscr.addstr(y, x,     "█)      ->    █          ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄             ▲         ")
  stdscr.addstr(y, x,     "█)            █          ")
  stdscr.refresh()
  time.sleep(0.5)
  stdscr.clear()

def attackSkeletonBow(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
        
  curses.curs_set(0)
  stdscr.addstr(y - 1, x, "▄               ▄        ")
  stdscr.addstr(y, x,     "█)             (█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄               ▄        ") 
  stdscr.addstr(y, x,     "█<)            (█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄               ▄        ")
  stdscr.addstr(y, x,     "█)  ->         (█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄               ▄        ")
  stdscr.addstr(y, x,     "█)        ->   (█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄               ▄        ")
  stdscr.addstr(y, x,     "█)             (█        ")
  stdscr.refresh()
  time.sleep(0.5)

def skeletonAttackBow(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
        
  curses.curs_set(0)
  stdscr.addstr(y - 1, x, "▄               ▄        ")
  stdscr.addstr(y, x,     "█)             (█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄               ▄        ") 
  stdscr.addstr(y, x,     "█)            (>█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄               ▄        ")
  stdscr.addstr(y, x,     "█)         <-  (█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄               ▄        ")
  stdscr.addstr(y, x,     "█)    <-       (█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄               ▄        ")
  stdscr.addstr(y, x,     "█) <-          (█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄               ▄        ")
  stdscr.addstr(y, x,     "█)             (█        ")
  stdscr.refresh()
  time.sleep(0.5)

def attackSpiderBow(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
       
  stdscr.addstr(y - 1, x, "▄                  ")
  stdscr.addstr(y, x,     "█)            ▄▅        ")
  stdscr.addstr(y + 1, x, "              ╵╵╵       ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄                ") 
  stdscr.addstr(y, x,     "█<)           ▄▅       ")
  stdscr.addstr(y + 1, x, "              ╵╵╵       ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄                  ")
  stdscr.addstr(y, x,     "█)  ->        ▄▅        ")
  stdscr.addstr(y + 1, x, "              ╵╵╵       ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄                  ")
  stdscr.addstr(y, x,     "█)      ->    ▄▅        ")
  stdscr.addstr(y + 1, x, "              ╵╵╵       ")
  stdscr.refresh()
  time.sleep(0.5)


  stdscr.addstr(y - 1, x, "▄                  ")
  stdscr.addstr(y, x,     "█)            ▄▅        ")
  stdscr.addstr(y + 1, x, "              ╵╵╵       ")
  stdscr.refresh()
  time.sleep(0.5)

def attackZombieBow(stdscr):
  h, w = stdscr.getmaxyx()
  y = h // 2
  x = w // 2
  stdscr.clear()
        
  stdscr.addstr(y -  1, x, "▄              ▄         ")
  stdscr.addstr(y, x,      "█)            ▔█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄              ▄         ") 
  stdscr.addstr(y, x,     "█<)           ▔█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄              ▄         ")
  stdscr.addstr(y, x,     "█)  ->        ▔█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y - 1, x, "▄              ▄         ")
  stdscr.addstr(y, x,     "█)       ->   ▔█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.addstr(y -  1, x, "▄             ▄         ")
  stdscr.addstr(y, x,      "█)           ▔█        ")
  stdscr.refresh()
  time.sleep(0.5)

  stdscr.clear()

