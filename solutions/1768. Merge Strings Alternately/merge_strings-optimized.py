class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # create indices to track each character index
        word1_pointer = 0
        word2_pointer = 0

        # Instantiate new word variable
        concatenated_word = ""

        # Loop through two words until both is exhausted
        while word1_pointer < len(word1) or word2_pointer < len(word2):
            if word1_pointer < len(word1):
                concatenated_word += word1[word1_pointer]
                word1_pointer += 1
            if word2_pointer < len(word2):
                concatenated_word += word2[word2_pointer]
                word2_pointer += 1

        # Return concatenated word
        return concatenated_word