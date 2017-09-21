import cx_Freeze
import humanize
import pycallgraph

exe = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup( name = "who-dis", version = "1.0", options = {"build_exe": {"packages": ["errno", "os", "re", "stat", "subprocess","collections", "pprint","shutil", "humanize","pycallgraph"], "include_files": []}}, executables = exe )
