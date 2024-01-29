import threading
import os

def run_script(script_name):
    os.system(f'python3 {script_name}')

scripts = []

scripts.append('6984018573.py')#2024-01-29 09:13:21.011539

scripts.append('6806777357.py')#2024-01-29 09:13:21.011539

scripts.append('6360485034.py')#2024-01-29 09:13:21.011539

scripts.append('6718328653.py')#2024-01-29 09:13:21.011539

scripts.append('6438487904.py')#2024-01-29 08:56:15.521294

scripts.append('6919917961.py')#2024-01-29 08:56:15.521294

scripts.append('6593652391.py')#2024-01-29 08:56:15.521294

scripts.append('6956328431.py')#2024-01-29 08:56:15.521294

scripts.append('6891111027.py')#2024-01-29 08:56:15.521294

scripts.append('6703910335.py')#2024-01-29 08:56:15.521294

scripts.append('6820053974.py')#2024-01-29 08:56:15.521294

scripts.append('6435090908.py')#2024-01-29 08:56:15.521294

scripts.append('6876993025.py')#2024-01-29 08:56:15.521294

scripts.append('6827118394.py')#2024-01-29 08:56:15.521294

scripts.append('6536563561.py')#2024-01-29 08:56:15.521294

scripts.append('6400408299.py')#2024-01-29 08:56:15.521294

scripts.append('6539810940.py')#2024-01-29 08:56:15.521294

scripts.append('6766132071.py')#2024-01-29 08:56:15.521294

scripts.append('6165471578.py')#2024-01-29 08:56:15.521294

scripts.append('6961434161.py')#2024-01-29 08:56:15.521294

scripts.append('6392448170.py')#2024-01-29 08:56:15.521294

scripts.append('6723617312.py')#2024-01-29 08:56:15.521294

scripts.append('6542774009.py')#2024-01-29 08:56:15.521294

scripts.append('6863876191.py')#2024-01-29 08:41:12.301113

scripts.append('6650514196.py')#2024-01-29 08:41:12.301113

scripts.append('6984018573.py')#2024-01-29 08:41:12.301113

scripts.append('6298045783.py')#2024-01-29 08:41:12.301113

scripts.append('6707282299.py')#2024-01-29 08:41:12.301113

scripts.append('6855890807.py')#2024-01-29 08:41:12.301113

scripts.append('6580591400.py')#2024-01-29 08:41:12.301113

scripts.append('6411388055.py')#2024-01-29 08:41:12.301113

scripts.append('6797498431.py')#2024-01-28 23:07:12.968206

scripts.append('6756193070.py')#2024-01-28 23:07:12.968206

scripts.append('6815273079.py')#2024-01-28 23:07:12.968206

scripts.append('6984018573.py')#2024-01-28 22:26:53.121357

scripts.append('6574425251.py')#2024-01-28 22:26:53.121357

scripts.append('6765783402.py')#2024-01-28 22:26:53.121357

scripts.append('6596623551.py')#2024-01-28 22:26:53.121357

scripts.append('6845465895.py')#2023-12-23 02:07:08.257455

threads = []
for script in scripts:
    thread = threading.Thread(target=run_script, args=(script,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

