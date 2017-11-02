my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"}

new_list = []

def dictuple():
    for k,v in my_dict.iteritems():
        new_list.append((k,v))
    print new_list
    
dictuple()








