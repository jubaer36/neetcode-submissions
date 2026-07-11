class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_string = [None] * len(strs)
        output_dict = {}
        output = [[]]
        for s in strs:
            new_str = "".join(sorted(list(s)))
            output_dict.setdefault(new_str,[]).append(s)
        output = list(output_dict.values())
        

        
        return output

        