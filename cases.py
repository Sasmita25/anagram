from anagram import anagram

def modthree(x):
   return x%3
def test_value():
   assert(modthree(4)==5)
def test_run_stuff():
        assert(anagram("EARTH", "HEART") == "Both strings form a Anagram.")
        assert(anagram("tom", "Mmot") == "Both strings do not form as a Anagram.")
        assert(anagram({1,3,5},{5,3,1}) == "Both strings form a Anagram.")
        assert(anagram("E$h*","*hE$") == "Both strings form a Anagram.")
        assert(anagram({'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6},{'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}) == "Both strings form a Anagram.")

