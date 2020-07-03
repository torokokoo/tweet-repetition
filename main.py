f = open('tweets.txt', encoding='utf-8')
tweetlist = [line.rstrip('\n') for line in f]

#print(tweetlist[0])


beer = 0
gin = 0
juice = 0
suko = 0
cocacola = 0
cocacola2 = 0
cocacola3 = 0
guarana = 0
mojito = 0
ron = 0
tequila = 0
wine = 0

for tweet in tweetlist:
    #print(tweet)
    #print("-----")

    if "beer" in tweet:
        beer = beer + 1

    if "gin" in tweet:
        gin = gin + 1
    
    if "juice" in tweet:
        juice = juice + 1
    
    if "suko" in tweet:
        suko = suko + 1
    
    if "coca cola" in tweet:
        cocacola = cocacola + 1

    if "Coca Cola" in tweet:
        cocacola2 = cocacola2 + 1

    if "Coca-Cola" in tweet:
        cocacola3 = cocacola3 + 1

    if "guarana" in tweet:
        guarana = guarana + 1

    if "mojito" in tweet:
        mojito = mojito + 1

    if "ron" in tweet:
        ron = ron + 1

    if "tequila" in tweet:
        tequila = tequila + 1
    
    if "wine" in tweet:
        wine = wine + 1

d = {'beer': beer, 'coca cola': cocacola, 'Coca Cola': cocacola2, 'Coca-Cola': cocacola3, 'gin': gin, 'juice': juice, 'suko': suko, 'guarana': guarana, 'mojito': mojito, 'ron': ron, 'tequila': tequila, 'wine': wine}
hightestdrink = max(d, key=d.get)

for drink,quantity in d.items():
    print("La bebida " + str(drink) + " fue mencionada " + str(quantity) + " veces.")

print("-----------------------")

print("La bebida con mayor numero de menciones es: " + str(hightestdrink))
print()
print()
print()


positivewords = ['save', 'hold', 'go for', 'drink', 'finished', 'Drinking', 'sound right', 'good', 'healthy', 'grande', 'great', 'enjoying', 'buy', 'free', 'Hold', 'greatest', 'pong', 'get',
'orgulhoso', 'strawberry', 'plenty', 'got', 'win', 'tonic', 'fav', 'favorite', 'feed', 'courtesy', 'better', 'taste', 'drinks',
'more', 'fresh', 'More', 'love', 'Love', 'popcorn', 'tastes', 'venti', 'prefiero', 'pizza', 'Pizza', 'likes', 'like', 'gusta',
'gosta', 'gusta', 'refigreador', 'gustas', 'gostoso', 'gelado', 'reir', 'bom', 'tomar', 'beber', 'consumida', 'consumir', 'fria',
'comi', 'antojao', 'tomo', 'ganas', 'tomei', 'gostosa', 'shots']

bp=0
gp=0
jp=0
sp=0
cc1p=0
cc2p=0
cc3p=0
gp=0
mp=0
rp=0
tp=0
wp=0

for tweet in tweetlist:
    if 'beer' in tweet:
        for w in positivewords:
            if w in tweet:
                bp = bp + 1
    
    if 'gin' in tweet:
        for w in positivewords:
            if w in tweet:
                gp = gp + 1

    if 'juice' in tweet:
        for w in positivewords:
            if w in tweet:
                jp = jp + 1

    if 'suko' in tweet:
        for w in positivewords:
            if w in tweet:
                sp = sp + 1

    if 'coca cola' in tweet:
        for w in positivewords:
            if w in tweet:
                cc1p = cc1p + 1

    if 'Coca Cola' in tweet:
        for w in positivewords:
            if w in tweet:
                cc2p = cc2p + 1

    if 'Coca-Cola' in tweet:
        for w in positivewords:
            if w in tweet:
                cc3p = cc3p + 1

    if 'guarana' in tweet:
        for w in positivewords:
            if w in tweet:
                gp = gp + 1

    if 'mojito' in tweet:
        for w in positivewords:
            if w in tweet:
                mp = mp + 1

    if 'tequila' in tweet:
        for w in positivewords:
            if w in tweet:
                tp = tp + 1

    if 'wine' in tweet:
        for w in positivewords:
            if w in tweet:
                wp = wp + 1

print("Hay " + str(bp) + " palabras bonitas para 'beer'")
print("Hay " + str(gp) + " palabras bonitas para 'gin'")
print("Hay " + str(jp) + " palabras bonitas para 'juice'")
print("Hay " + str(sp) + " palabras bonitas para 'suko'")
print("Hay " + str(cc1p) + " palabras bonitas para 'coca cola'")
print("Hay " + str(cc2p) + " palabras bonitas para 'Coca Cola'")
print("Hay " + str(cc3p) + " palabras bonitas para 'Coca-Cola'")
print("Hay " + str(gp) + " palabras bonitas para 'guarana'")
print("Hay " + str(mp) + " palabras bonitas para 'mojito'")
print("Hay " + str(tp) + " palabras bonitas para 'tequila'")
print("Hay " + str(wp) + " palabras bonitas para 'wine'")

p = {'beer': bp, 'coca cola': cc1p, 'Coca Cola': cc2p, 'Coca-Cola': cc3p, 'gin': gp, 'juice': jp, 'suko': sp, 'guarana': gp, 'mojito': mp, 'ron': rp, 'tequila': tp, 'wine': wp}
hightestrep = max(p, key=p.get)

print("-----------------")
print("La bebida con mayor numero de palabras bonitas es: " + hightestrep)


counter = 0
word = positivewords[0] 

for tweet in tweetlist:
    for w in positivewords:
        if w in tweet:
            curr_frequency = positivewords.count(w) 
            if (curr_frequency > counter): 
                counter = curr_frequency 
                word = w 

print("La palabra bonita que mas se repite dentro de todos los tweets es: " + word)