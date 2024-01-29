from subprocess import Popen

filename = "app.py"
while True:
    print("\nStarting " + filename)
    p = Popen("python3 " + filename, shell=True)
    p.wait()
