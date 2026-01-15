This is a code developed by Iagmla for encrypting codes

A = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def conv_to_num(chars):
    n = []
    for char in chars:
        n.append(A.index(char))
    return n
   
def conv_to_letters(A, nums):
    l = []
    for n in nums:
        l.append(A[n])
    return "".join(l)
   
def add_two_words(worda, wordb):
    word = []
    for x in range(len(worda)):
        word.append(((worda[x] + wordb[x]) % 26))
    return word
   
def main():
    worda = "NACIREMA"
    wordb = "ARAIIUMA"
    na = conv_to_num(worda)
    nb = conv_to_num(wordb)
    word = add_two_words(na, nb)
    word_letters = conv_to_letters(A, word)
    print(word_letters)
   
main()

The letters that should show up in Python are NRCQZYYA
*use worda and wordb with the same number of letters to produce a coded word
