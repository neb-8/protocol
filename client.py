import json
import sys

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    data = json.load(file)

def main():
    demands = data['simulation']['demands']
    circuits = data['possible-circuits']
    switches = data['switches']
    circuit_found = True
    all_avaliable = True
    switches_removed = []
    index_of_operation = 0
    used_circuits = []
    
    for i in range(1, data['simulation']['duration']+1):
        for j in demands:
            all_avaliable = True
            if i == j['start-time']:
                index_of_operation += 1
                for k in circuits:
                    circuit_found = ((k[0] == j['end-points'][0]) and (k[-1] == j['end-points'][-1]))
                    if circuit_found:
                        all_avaliable = True
                        for m in k[1:-1]:
                            all_avaliable = all_avaliable and (m in switches)
                        if all_avaliable:
                            for n in k[1:-1]:
                                switches_removed.append(n)
                                switches.remove(n)
                            used_circuits.append(k)
                            break
                print(index_of_operation,'. igény foglalás:',j['end-points'][0],'<->',j['end-points'][-1],'st:',i,' - ','sikeres' if all_avaliable else 'sikertelen')
            if i == j['end-time']:
                index_of_operation += 1
                for o in used_circuits:
                    circuit_found = ((o[0] == j['end-points'][0]) and (o[-1] == j['end-points'][-1]))
                    if circuit_found:
                        all_avaliable = True
                        for q in o[1:-1]:
                            all_avaliable = all_avaliable and (q in switches_removed)
                        if all_avaliable:
                            for p in o[1:-1]:
                                switches.append(p)
                                switches_removed.remove(p)
                            print(index_of_operation,'. igény felszabadítás: ',j['end-points'][0],'<->',j['end-points'][-1],' st:',i)
                            break

main()
