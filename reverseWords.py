'''
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples:
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

def reverse_words(text):
    textSplit = text.split(" ")
    reverse = []
    for i in textSplit:
        reverse.append(i[::-1])
    
    result = "  ".join(reverse)
    print(textSplit)
    return result
