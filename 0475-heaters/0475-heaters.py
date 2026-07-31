class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        last_heater_index = len(heaters) - 1
        l_h, r_h = 0, 0
        max_radius = 0

        for house in houses:
            while r_h < last_heater_index and house > heaters[r_h]:
                l_h, r_h = r_h, r_h + 1
            
            distance_left = abs(heaters[l_h] - house)
            distance_right = abs(heaters[r_h] - house)
            max_radius = max(max_radius, min(distance_left, distance_right))
        
        return max_radius
        