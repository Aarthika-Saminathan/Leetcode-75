class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = "aeiouAEIOU"

        vowel_positions = []
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                vowel_positions.append(i)

        vowel_letters = []
        for j in range(len(vowel_positions)):
            vowel_letters.append(s_list[vowel_positions[j]])

        vowel_letters = vowel_letters[::-1]

        for i in range(len(vowel_positions)):
            s_list[vowel_positions[i]] = vowel_letters[i]

        return ''.join(s_list)
sol = Solution()
print(sol.reverseVowels("IceCreAm"))  # Output: "AceCreIm"

