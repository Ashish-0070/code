class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        
        for numberOfBoxes, unitsPerBox in boxTypes:
            if truckSize == 0:
                break
                
            boxes_to_take = min(truckSize, numberOfBoxes)
            
            total_units += boxes_to_take * unitsPerBox
            
            truckSize -= boxes_to_take
        
        return total_units
