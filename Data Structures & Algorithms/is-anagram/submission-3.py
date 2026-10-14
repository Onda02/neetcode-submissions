class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        car_s = {}
        car_t = {}

        for car in s:
            if car in car_s:
                car_s[car] = car_s[car]+1
            else:
                car_s[car] = 1

        for car in t:
            if car in car_t:
                car_t[car] = car_t[car]+1
            else:
                car_t[car] = 1

        return car_s == car_t