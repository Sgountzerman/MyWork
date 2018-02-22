keimeno = input('Give me a text:')

alfavhta = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

kod1 = [' ','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m',]

def rot13(text):
  kodikop= ""
  
  for ch in text:
    for i in range(len(alfavhta)):
      if ch==alfavhta[i]:
        c= kod1[i]
              
    kodikop += c
    
  return kodikop

print (rot13(keimeno))

