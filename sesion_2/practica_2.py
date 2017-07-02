###########################################################################################################
#
#
###########################################################################################################

signals = [0.81, -2, -2.5, -0.3, 0.4, 2.1, 3, 2.9, -1]
newSignals = []
ind = []

def signo(x):
    if x >= 0:
        return 1
    else:
        return -1

for signal in signals:
    newSignals.append(signo(signal))    

print newSignals

for i in range(len(signals)-1):
    if newSignals[i]*newSignals[i+1] < 0:
        ind.append(i)

print ind