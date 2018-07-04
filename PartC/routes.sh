h1 ip route add 173.1.0.0/16 via 172.1.0.2 dev h1-eth0
h1 ip route add 174.1.0.0/16 via 172.1.0.2 dev h1-eth0
h1 ip route add 175.1.0.0/16 via 172.1.0.2 dev h1-eth0
h1 ip route add 176.1.0.0/16 via 172.1.0.2 dev h1-eth0
h1 ip route add 177.1.0.0/16 via 172.1.0.2 dev h1-eth0

r1 ip route add 175.1.0.0/16 via 173.1.0.2 dev r1-eth1
r1 ip route add 176.1.0.0/16 via 174.1.0.2 dev r1-eth2
r1 ip route add 177.1.0.0/16 via 173.1.0.2 dev r1-eth1
r1 ip route add 177.1.0.0/16 via 174.1.0.2 dev r1-eth2

r2 ip route add 172.1.0.0/16 via 173.1.0.1 dev r2-eth0
r2 ip route add 174.1.0.0/16 via 173.1.0.1 dev r2-eth0
r2 ip route add 176.1.0.0/16 via 175.1.0.2 dev r2-eth1
r2 ip route add 177.1.0.0/16 via 175.1.0.2 dev r2-eth1

r3 ip route add 172.1.0.0/16 via 174.1.0.1 dev r3-eth0
r3 ip route add 173.1.0.0/16 via 174.1.0.1 dev r3-eth0
r3 ip route add 175.1.0.0/16 via 176.1.0.2 dev r3-eth1
r3 ip route add 177.1.0.0/16 via 176.1.0.2 dev r3-eth1

r4 ip route add 172.1.0.0/16 via 176.1.0.1 dev r4-eth2
r4 ip route add 173.1.0.0/16 via 175.1.0.1 dev r4-eth1
r4 ip route add 174.1.0.0/16 via 176.1.0.1 dev r4-eth2
r4 ip route add 172.1.0.0/16 via 176.1.0.1 dev r4-eth2

h2 ip route add 172.1.0.0/16 via 177.1.0.1 dev h2-eth0
h2 ip route add 173.1.0.0/16 via 177.1.0.1 dev h2-eth0
h2 ip route add 174.1.0.0/16 via 177.1.0.1 dev h2-eth0
h2 ip route add 175.1.0.0/16 via 177.1.0.1 dev h2-eth0
h2 ip route add 176.1.0.0/16 via 177.1.0.1 dev h2-eth0

