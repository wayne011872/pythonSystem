import psutil
import time
import pythonGeneral.email.sendEmail as pes

def printSystemStatus(systemMonitor):
    cpu_usage,memory_usage,swap_memory_usage,diskC_usage,diskD_usage = systemMonitor
    systemMonitorStr = "CPU :{0}\nMemory :{1}\nSwap :{2}\nDiskC :{3}\nDiskD :{4}".format(
        cpu_usage, memory_usage, swap_memory_usage, diskC_usage, diskD_usage)
    print(systemMonitorStr)
    print("-----------------per 5 seconds-------------------")
        
def detectError(systemMonitor):
    emailTitle = "主機異常通知"
    cpu_usage, memory_usage, swap_memory_usage, diskC_usage, diskD_usage = systemMonitor
    cpu_usage = 85
    if int(cpu_usage)>=85:
        cpuMailContent = "<h3>警告!!! 主機CPU使用率大於85%</h3>"
        myMail = pes.MyMail(emailTitle,cpuMailContent)
        myMail.sendMessage()

while(True):
    cpu_all = 0
    cpu_percent = psutil.cpu_percent(interval=1, percpu=1)
    for per_cpu in cpu_percent:
        cpu_all = cpu_all + per_cpu
    cpu_usage = cpu_all/len(cpu_percent)
    memory_usage = psutil.virtual_memory().percent
    swap_memory_usage = psutil.swap_memory().percent
    diskC_usage = psutil.disk_usage('C:\\').percent
    diskD_usage = psutil.disk_usage('D:\\').percent
    systemMonitor = []
    systemMonitor.append(cpu_usage)
    systemMonitor.append(memory_usage)
    systemMonitor.append(swap_memory_usage)
    systemMonitor.append(diskC_usage)
    systemMonitor.append(diskD_usage)
    printSystemStatus(systemMonitor)
    detectError(systemMonitor)
    time.sleep(5)