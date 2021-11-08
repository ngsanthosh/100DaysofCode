# https://leetcode.com/problems/reorder-data-in-log-files/submissions/


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letlogs,digilogs=[],[] 
        
        for log in logs:
            stuff =  log.split()[1]
            if(stuff.isdigit()):
                digilogs.append(log)
            else:
                letlogs.append(log)
                
        letlogs.sort(key=lambda c:c.split()[0])
        letlogs.sort(key=lambda c:c.split()[1:])
        
        return letlogs+digilogs