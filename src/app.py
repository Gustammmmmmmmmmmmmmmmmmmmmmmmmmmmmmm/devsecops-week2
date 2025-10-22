import subprocess
# shlex adalah library untuk memecah string perintah dengan aman
import shlex

def add(a, b):
   return a + b

def divide(a, b):
   if b == 0:
     raise ValueError("Tidak boleh bagi nol")
   return a / b

# Fungsi yang sudah diperbaiki
def run_command(cmd):
 # FIX: Pecah command string menjadi list dan HINDARI shell=True
 args = shlex.split(cmd)
 result = subprocess.run(args, capture_output=True, text=True)
 return result.stdout
