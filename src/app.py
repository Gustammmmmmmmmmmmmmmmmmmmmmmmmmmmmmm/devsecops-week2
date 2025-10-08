import subprocess

def add(a, b):
   return a + b

def divide(a, b):
   if b == 0:
     raise ValueError("Tidak boleh bagi nol")
   return a / b

#menambahkan bug security pada app.py
def run_command(cmd):
   result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
   return result.stdout
