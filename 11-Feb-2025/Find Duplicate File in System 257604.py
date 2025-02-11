# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        count_file = defaultdict(list)
        duplicates = []

        for path in paths:
            separate = path.split(" ")
            for i in range(1, len(separate)):
                file_separate = separate[i].split("(")
                count_file[file_separate[1]].append('/'.join([separate[0], file_separate[0]]))
        for key, value in count_file.items():
            if len(value) > 1:
                duplicates.append(value)
        return duplicates

        