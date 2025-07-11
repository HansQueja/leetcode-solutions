class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # create indices to track each character index
        word1_pointer = 0
        word2_pointer = 0

        # Instantiate new word variable
        concatenated_word = ""

        while word1_pointer < len(word1) and word2_pointer < len(word2):
            concatenated_word += word1[word1_pointer] + word2[word2_pointer]
            word1_pointer += 1
            word2_pointer += 1
        
        if word1_pointer < len(word1):
            concatenated_word += word1[word1_pointer:]
        else:
            concatenated_word += word2[word2_pointer:]

        return concatenated_word