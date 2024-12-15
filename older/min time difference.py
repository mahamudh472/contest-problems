class Solution:
    def findMinDifference(self, timePoints) -> int:
        def convert_to_min(s1, s2):
            h1, m1 = map(int, s1.split(":"))
            h2, m2 = map(int, s2.split(":"))
            mins1 = h1*60+m1
            mins2 = h2*60+m2
            dif1 = abs(mins1-mins2)
            dif2 = abs(abs(1440-mins2)) +mins1
            return dif1 if dif1<dif2 else dif2
        min_dif = None
        sorted_time_points = sorted(timePoints)
        
        for i in range(len(sorted_time_points)-1):
            dif = convert_to_min(sorted_time_points[i], sorted_time_points[i+1])
            if min_dif is None:
                min_dif = dif
            elif dif<min_dif:
                min_dif = dif
        last_to_first = convert_to_min(sorted_time_points[0], sorted_time_points[-1])
        if last_to_first < min_dif:
            return last_to_first
        return min_dif
    

sol = Solution()
print(sol.findMinDifference(["00:00","04:00","22:00"]))