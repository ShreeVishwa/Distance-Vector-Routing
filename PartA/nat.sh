r1 iptables -t nat -A POSTROUTING -o r1-eth0 -j MASQUERADE
r1 iptables -A FORWARD -i r1-eth0 -o r1-eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
r1 iptables -A FORWARD -i r1-eth0 -o r1-eth1 -j ACCEPT

r2 iptables -t nat -A POSTROUTING -o r2-eth1 -j MASQUERADE
r2 iptables -A FORWARD -i r2-eth0 -o r2-eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
r2 iptables -A FORWARD -i r2-eth0 -o r2-eth1 -j ACCEPT

r4 iptables -t nat -A POSTROUTING -o r4-eth1 -j MASQUERADE
r4 iptables -A FORWARD -i r4-eth1 -o r4-eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
r4 iptables -A FORWARD -i r4-eth1 -o r4-eth0 -j ACCEPT


r4 iptables -A FORWARD -i r4-eth0 -o r4-eth2 -j ACCEPT
r4 iptables -A FORWARD -i r4-eth0 -o r4-eth2 -m state --state RELATED,ESTABLISHED -j ACCEPT
r4 iptables -t nat -A POSTROUTING -o r4-eth2 -j MASQUERADE

r3 iptables -A FORWARD -i r3-eth1 -o r3-eth0 -j ACCEPT
r3 iptables -A FORWARD -i r3-eth1 -o r3-eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
r3 iptables -t nat -A POSTROUTING -o r3-eth0 -j MASQUERADE
