class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = 0
        for i in range(len(flowerbed)):
            left = (i == 0) or (flowerbed[i - 1] == 0)
            right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
            if left and right and flowerbed[i] != 1:
                k += 1
                flowerbed[i] = 1
        return n <= k
