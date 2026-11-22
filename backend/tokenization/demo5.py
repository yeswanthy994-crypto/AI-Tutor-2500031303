corpus={"Play":5,
        "Playing":3,
        "Played":2,}

print("Corpus :",corpus)
print("Length of corpus :",len(corpus))
for k in corpus.keys():
    print(k)
    
for v in corpus.values():
    print(v)

for k,v in corpus.items():
    print(k,v)