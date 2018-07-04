"""
Example topology of Quagga routers
"""

import inspect
import os
from mininext.topo import Topo
from mininext.services.quagga import QuaggaService

from collections import namedtuple

QuaggaHost = namedtuple("QuaggaHost", "name ip loIP")
net = None


class QuaggaTopo(Topo):

    "Creates a topology of Quagga routers"

    def __init__(self):
        """Initialize a Quagga topology with 5 routers, configure their IP
           addresses, loop back interfaces, and paths to their private
           configuration directories."""
        Topo.__init__(self)

        # Directory where this file / script is located"
        selfPath = os.path.dirname(os.path.abspath(
            inspect.getfile(inspect.currentframe())))  # script directory

        # Initialize a service helper for Quagga with default options
        quaggaSvc = QuaggaService(autoStop=False)

        # Path configurations for mounts
        quaggaBaseConfigPath = selfPath + '/configs/'

        # List of Quagga host configs
        quaggaHosts = []
        quaggaHosts.append(QuaggaHost(name='h1', ip='172.1.0.1/16',
                                      loIP='10.0.1.1/24'))
        quaggaHosts.append(QuaggaHost(name='r1', ip='172.1.0.2/16',
                                      loIP='10.0.2.1/24'))
        quaggaHosts.append(QuaggaHost(name='r2', ip='173.1.0.2/16',
                                      loIP='10.0.3.1/24'))
        quaggaHosts.append(QuaggaHost(name='r3', ip='174.1.0.2/16',
                                      loIP='10.0.3.1/24'))
        quaggaHosts.append(QuaggaHost(name='r4', ip='177.1.0.1/16',
                                      loIP='10.0.4.1/24'))
        quaggaHosts.append(QuaggaHost(name='h2', ip='177.1.0.2/16',
                                      loIP=None))
	topology = list()	
        # Setup each Quagga router, add a link between it and the IXP fabric
        for host in quaggaHosts:

            # Create an instance of a host, called a quaggaContainer
            qc = (self.addHost(name=host.name,
                                           ip=host.ip,
                                           hostname=host.name,
                                           privateLogDir=True,
                                           privateRunDir=True,
                                           inMountNamespace=True,
                                           inPIDNamespace=True,
                                           inUTSNamespace=True))
	    
            topology.append(qc)
            # Configure and setup the Quagga service for this node
            quaggaSvcConfig = \
                {'quaggaConfigPath': quaggaBaseConfigPath + host.name}
            self.addNodeService(node=host.name, service=quaggaSvc,
                                nodeConfig=quaggaSvcConfig)

	self.addLink(topology[0], topology[1])
	self.addLink(topology[1], topology[2])
	self.addLink(topology[1], topology[3])
	self.addLink(topology[5], topology[4])
	self.addLink(topology[2], topology[4])
	self.addLink(topology[3], topology[4])
