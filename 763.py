class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}

        for index, letter in enumerate(s):
            last_index[letter] = index

        start = end = 0
        
        ans = []

        for index, letter, in enumerate(s):

            end = max(end, last_index[letter])

            if index == end:
                ans.append(end - start + 1)
                start = end + 1

        return ans