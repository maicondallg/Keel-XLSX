def fix_arff(aux):
    i = 1
    while ('@attribute' in aux[i]) or ('@Attribute' in aux[i]):
#         print(i)
        if 'integer [' in aux[i]:
            pos = aux[i].find("integer [")
            aux[i] = aux[i][:pos] + 'integer'
            
        if 'real [' in aux[i]:
            pos = aux[i].find("real [")
            aux[i] = aux[i][:pos] + 'real'
            
        if 'real[' in aux[i]:
            pos = aux[i].find("real[")
            aux[i] = aux[i][:pos] + 'real'
                
        
        if 'integer[' in aux[i]:
            pos = aux[i].find("integer[")
            aux[i] = aux[i][:pos] + 'integer'
            
        if '{' in aux[i]:
            pos = aux[i].find("{")
            aux[i] = aux[i][:pos] + ' ' + aux[i][pos:]
            
        i+=1