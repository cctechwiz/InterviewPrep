# Problem: Is Scrambled Palindrome
Write a function that, given a string of letters, returns true or false for whether the letters in the
string could be arranged to form a palindrome.  

E.g. For “torro”, the answer is True, because the letters can be rearranged to spell “rotor”.


# Notes
A word (or collection of letters) can be a palindrom if every letter occurs an even number of times, 
with the exception that there can be either zero or one letter that occurs an odd number of times.

Using a dictionary to keep a count for each character give O(1) effeciency for counting.  
A dictionary is also sparse because entries are only made for letters that are present, this is memory efficient.  

Then iterating over the dictionary counting the number of odds, at worst is O(n).  
I suppose I could potentially break the loop by returning early or something if the odd count is ever > 1, 
that could potentialy prevent unneeded iterations. It would be minimal at best because the size of the 
dictionary can only ever be 26 (assuming English with no special characters). But in other use cases it
might be worth considering.
