IDT1=[]
WT1=[]
TT1=[]
ST1=[]
AT=[]
IDT2=[]
WT2=[]
TT2=[]
ST2=[]
IDT3=[]
WT3=[]
TT3=[]
ST3=[]
IDT4=[]
WT4=[]
TT4=[]
ST4=[]
for i in range(20):
    # Estación 1
    if i == 0:
        IDT1[i] = 0
        WT1[i] = 0
        TT1[i] = ST1[i]
    else:
        IDT1[i] = max(0, TT1[i-1] - sum(AT[:i+1]))
        WT1[i] = max(0, sum(AT[:i+1]) - TT1[i-1])
        TT1[i] = sum(AT[:i+1]) + WT1[i] + ST1[i]

    # Estación 2
    if i == 0:
        IDT2[i] = 0
        WT2[i] = 0
        TT2[i] = TT1[i] + ST2[i]
    else:
        IDT2[i] = max(0, TT2[i-1] - TT1[i])
        WT2[i] = max(0, TT1[i] - TT2[i-1])
        TT2[i] = TT1[i] + WT2[i] + ST2[i]

    # Estación 3
    IDT3[i] = max(0, TT3[i-1] - TT2[i])
    WT3[i] = max(0, TT2[i] - TT3[i-1])
    TT3[i] = TT2[i] + WT3[i] + ST3[i]
# Estación 4
    IDT4[i] = max(0, TT4[i-1] - TT3[i])
    WT4[i] = max(0, TT3[i] - TT4[i-1])
    TT4[i] = TT3[i] + WT4[i] + ST4[i]

# Resultados
print("Tiempos finales en E1:", TT1)
print("Tiempos finales en E2:", TT2)
print("Tiempos finales en E3:", TT3)
print("Tiempos finales en E4:", TT4)
print("Tiempos de espera E1:", WT1)
print("Tiempos de ocio E1:", IDT1)