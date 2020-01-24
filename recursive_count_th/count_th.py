'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# We got:
# total count of "th" elements
# just recursion
# single parameter
# should look to "th" element, not "TH"

def count_th(word):

    if len(word) == 0 or len(word) < 2:
        print("Incorrect input")
        return 0
    
    count = 0
    th_search = word.find("th")
    print("Search", th_search)


    return count


count_th("ololotholol")