def find_missing_letter(chars):
    values = []
    for i in chars:
        values.append(ord(i))
    counter = values[0] - 1

    for i in values:
        counter += 1
        if(i != counter):
            break
        
    return chr(counter)
