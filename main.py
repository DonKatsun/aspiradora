import subprocess

print("Cantidad de aspiradoras: ")
mode=int(input())
if mode == 1:
    import aspiradora1
    exec(open("aspiradora1.py").read())
elif mode == 2:
    import aspiradora
    exec(open("aspiradora.py").read())
