#!/usr/bin/env python3

"""Enterprise SDN lab topology for Mininet.

8 hosts connected to one OpenFlow13 switch (single enforcement point).
"""

from mininet.topo import Topo


class RealEnterpriseTopo(Topo):
    """Single-switch enterprise segmentation lab."""

    def build(self):
        # Users zone
        # Use a shared /8 so hosts are L2/L3 reachable without a router.
        # Zone isolation is enforced by the SDN controller policy, not IP routing.
        h1 = self.addHost("h1", ip="10.1.0.1/8", mac="00:00:00:01:00:00")
        h2 = self.addHost("h2", ip="10.1.0.2/8", mac="00:00:00:02:00:00")

        # Apps zone
        h3 = self.addHost("h3", ip="10.2.0.1/8", mac="00:00:00:03:00:00")
        h4 = self.addHost("h4", ip="10.2.0.2/8", mac="00:00:00:04:00:00")

        # Database zone
        h5 = self.addHost("h5", ip="10.3.0.1/8", mac="00:00:00:05:00:00")

        # DMZ zone
        h6 = self.addHost("h6", ip="10.4.0.1/8", mac="00:00:00:06:00:00")
        h7 = self.addHost("h7", ip="10.4.0.2/8", mac="00:00:00:07:00:00")
        h8 = self.addHost("h8", ip="10.4.0.3/8", mac="00:00:00:08:00:00")

        s1 = self.addSwitch("s1")

        # Single enforcement point: all hosts connect to s1.
        for host in (h1, h2, h3, h4, h5, h6, h7, h8):
            self.addLink(host, s1)


topos = {"real": (lambda: RealEnterpriseTopo())}


