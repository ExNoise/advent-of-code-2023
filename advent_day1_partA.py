import os

# Ottieni il percorso completo del file nella stessa directory dello script
percorso_file = os.path.join(os.path.dirname(__file__), "inputs.txt")


        # Apri il file in modalità lettura
with open(percorso_file, 'r') as file:
            # Leggi e stampa il contenuto del file
    contenuto = file.readlines()

 
count =0
# Strips the newline character
for line in contenuto:
    pota=""
    #print("Line{}: {}".format(count, line.strip()))
    for char in line.strip():
        if char.isdigit():
            pota=char
            break
        
        
    for char in reversed(line.strip()):
        if char.isdigit():
            pota=pota+char
            break
        
    potaInt=0
    
    potaInt=int(pota)
    count+=potaInt
    
print(count)