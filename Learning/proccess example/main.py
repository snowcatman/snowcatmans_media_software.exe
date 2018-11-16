import subprocess
print('--start')
subprocess.Popen('cmd /c python main01.py', shell=False)
print()
print('   what a big worl you are!')
print()
subprocess.Popen('python main02.py', shell=False)
print('--end')
