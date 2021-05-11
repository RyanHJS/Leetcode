# Given a string s, find the length of the longest substring without repeating characters.

s = "abcabcbb"

# Use a dictionary called seen to store values
# Store every letter and how many times they appear in the list

def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    answer = 0
    start_index = 0
    cutoff_index = 0
    
    if len(s) == 0:
        return 0
    
    for index, letter in enumerate(s):
        
        if letter in seen:
            if (seen.get(letter) < cutoff_index):
                pass
            else:
                start_index = seen.get(letter) + 1
                cutoff_index = start_index
                print(f'Found dup: {letter}, updating start: {start_index}')
        seen[letter] = index
        answer = max(answer, index - start_index + 1)
        print(f'{seen}, Current ans: {answer}')
        
    return answer           

sol = lengthOfLongestSubstring(s)
print(f'Length of longest substring is: {sol}')
