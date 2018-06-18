from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.util import dumpNodeConnections
from mininet.node import CPULimitedHost
from mininet.link import TCLink
"""
Instructions to run the topo:
    1. Go to directory where this file is.
    2. run: sudo python redes.py

This topo represents the Department of Informatics at the Federal University of Parana
"""


class DinfTopo(Topo):
    """Dinf topology example."""
    def build(self):
        # Master switch
        s0 = self.addSwitch('s0')
        linkopts = dict(bw=1000, delay='5ms', loss=5, max_queue_size=1000, use_htb=True)

        # Creating Lab 12
        s1 = self.addSwitch('s1')
        for h in range(0, 60):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, s1, **linkopts)

        # Creating Lab 3
        s2 = self.addSwitch('s2')
        for h in range(60, 90):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, s2, **linkopts)

        # Creating Lab 4
        s3 = self.addSwitch('s3')
        for h in range(90, 120):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, s3, **linkopts)

        # Linking master switch with laboratories switches
        linkopts = dict(bw=10000, delay='1ms', loss=2, max_queue_size=10000, use_htb=True)
        self.addLink(s0, s1, **linkopts)
        self.addLink(s0, s2, **linkopts)
        self.addLink(s0, s3, **linkopts)


def run():
    net = Mininet(topo=DinfTopo(), host=CPULimitedHost, link=TCLink)
    net.start()
    # print "Dumping host connections"
    # dumpNodeConnections(net.hosts)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()