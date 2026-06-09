import os

def clearscreen():
    os.system('clear' if os.name == 'posix' else 'cls')

def printart():
    art = r"""
   ╔════════════════════════════════════╗
   ║       axomic instagram tool              ║
   ║            by axom                       ║
   ╚════════════════════════════════════╝
    """
    print(art)
