class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])-1
        t, b = 0, len(matrix)-1

        while t <= b:
            midc = t + (b-t)//2
            if matrix[midc][-1] < target:
                t = midc + 1
            elif matrix[midc][0] > target:
                b = midc - 1
            elif matrix[midc][0] < target < matrix[midc][-1]:
                while l <= r: 
                    midr = l + (r-l)//2
                    if matrix[midc][midr] < target:
                        l = midr +1
                    elif matrix[midc][midr] > target:
                        r = midr - 1
                    else: 
                        return True
                return False
            elif target == matrix[midc][0]: return True
            elif target == matrix[midc][-1]: return True
            else: return False

        return False
            