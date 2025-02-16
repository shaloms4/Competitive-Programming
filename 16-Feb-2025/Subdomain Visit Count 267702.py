# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)
        for domain in cpdomains:
            splitted = domain.split(" ")
            split_dot = splitted[1].split(".")
            for i in range(len(split_dot)):
                joined = '.'.join(split_dot[i:])
                count[joined] += int(splitted[0])
        return [f"{value} {key}" for key, value in count.items()]      

        