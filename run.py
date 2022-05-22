import os
try:os.system('mkdir OK')
except:pass
try:os.system('mkdir CP')
except:pass
try:os.system('touch .prox.txt')
except:pass
try:os.system('mkdir result')
except:pass
if __name__ == "__main__":
        try:
                __import__("exploid").lisensi()
        except Exception as e:
                exit(str(e))
