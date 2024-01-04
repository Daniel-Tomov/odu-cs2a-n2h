log = open("iptable.log", "r").readlines()

srcIPs = {}
dstPorts = {}


for entry in log:
    srcip = entry.split("SRC=")[1].split(" ")[0]

    try:
        srcIPs[srcip] += 1
    except Exception:
        srcIPs[srcip] = 1

    dstport = entry.split("SPT=")[1].split(" ")[0]

    try:
        dstPorts[dstport] += 1
    except Exception:
        dstPorts[dstport] = 1

srcIPs = dict((v,k) for k,v in srcIPs.items()) # https://stackoverflow.com/questions/1031851/how-do-i-exchange-keys-with-values-in-a-dictionary

print(srcIPs)

dstPorts = dict((v,k) for k,v in dstPorts.items()) # https://stackoverflow.com/questions/1031851/how-do-i-exchange-keys-with-values-in-a-dictionary

print(dstPorts)