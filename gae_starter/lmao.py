def ay(word):
    if word[-3:] == "ife":
        words = word[:-3] + "ives"
    elif word[-2:] == "sh" or word[-2:] == "ch":
        words = word + "es"
    elif word[-2:] == "us": # 
        words = word[:-2] + "i"
    elif word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "uy": # for words such as toy, guy, and key
        words = word + "s"
    elif word[-1:] == "y": # for words such as fly
        words = word[:-1] + "ies"
    elif word == "goose" or word == "mouse": # for words such as moose or goose
        words = word[:-4] + "eese"
    else:
        words = word + "s"
    return words