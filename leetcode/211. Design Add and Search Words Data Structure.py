# 211. Design Add and Search Words Data Structure.py
"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
"""
"""
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""
class WordNode():
    def __init__(self):
        self.childword = {}
        self.endmark = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for s in word:
            if not s in cur.childword:
                cur.childword[s] = WordNode()
                cur = cur.childword[s]
            else:
                cur = cur.childword[s]
        cur.endmark = True
       

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                w = word[i]
                if w == '.':
                    for node in cur.childword.values():
                        if dfs(i+1,node):
                            return True
                    return False

                else:
                    if w not in cur.childword:
                        return False
                    else:
                        cur = cur.childword[w]
            
            return cur.endmark
        return dfs(0,self.root)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)