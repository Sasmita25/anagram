def anagram(string1, string2):
    print("Before Sort",string1,string2)
    print("After Sort",sorted(string1),sorted(string2))
# Strings are sorted and verified
    if(sorted(string1) == sorted(string2)):
        
        print("Both strings form a Anagram.")
    else:
      
       print("Both strings do not form as a Anagram.")
        
def test_run_stuff():
        assert anagram("EARTH", "HEART") == "Both strings form a Anagram."
        assert anagram({1,3,5},{5,3,1}) == "Both strings form a Anagram."
        assert anagram("E$h*","*hE$") == "Both strings form a Anagram."
        assert anagram({'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6},{'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}) == "Both strings form a Anagram."
        
        

