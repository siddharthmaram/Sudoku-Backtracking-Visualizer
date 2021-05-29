import cx_Freeze
import sys


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base=base)]

cx_Freeze.setup(
    name="Sudoku",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["menus.py", "sudoku_solver.py", "OdibeeSans-Regular.ttf", 'image.png', "close.png"]}},
    executables=executables
)