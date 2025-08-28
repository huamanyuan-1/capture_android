import time
import argparse
from multiprocessing import Process
import subprocess
import psutil
import os
import random
import string

class ProcessApp:
    def __init__(self) -> None:
        pass
    
    def generate_random_string(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))  
    
    def run_adb_tcpdump(self, name):
        # 启动 adb shell tcpdump 命令
        adb_proc = subprocess.Popen(
            f'adb shell tcpdump -i wlan0 -w /data/local/tmp/pcap/{name}.pcap',
            shell=True
        )
        return adb_proc.pid

    def run_mitmdump(self, name):
        # 启动 mitmdump 命令
        env = os.environ.copy()
        env["SSLKEYLOGFILE"] = f"C:/Users/nstl/Downloads/extract/key/{name}.log"
        mitmdump_proc = subprocess.Popen(
            'mitmdump -p 8888 --mode upstream:http://127.0.0.1:7897',
            shell=True,
            env=env
        )
        return mitmdump_proc.pid

    def terminate_process_tree(self, pid):
        try:
            parent = psutil.Process(pid)
            for child in parent.children(recursive=True):
                child.terminate()
            parent.terminate()
        except psutil.NoSuchProcess:
            pass

    def process_all(self, class_app, app_func, app_name, num):
        
        
        method = getattr(class_app, app_func)
        p1 = Process(target=method)
        
        pid1, pid2 = self.bat_get_flow(app_func, app_name, str(num))

        p1.start()
        p1.join()
        p1.terminate()
        
        self.terminate_process_tree(pid1)
        self.terminate_process_tree(pid2)
        
  

        

    def bat_get_flow(self, func, app_name, num):
        name = app_name + "_" + func + "_" + num
        tcpdump_pid = self.run_adb_tcpdump(name)
        mitmdump_pid = self.run_mitmdump(name)
        return tcpdump_pid, mitmdump_pid    
