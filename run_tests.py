import subprocess,sys
sys.exit(subprocess.run([sys.executable,"-m","pytest","-q"]).returncode)
