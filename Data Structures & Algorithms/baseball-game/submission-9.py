class Solution:
    def calPoints(self, operations: List[str]) -> int:
        cal_point_arr = []
        for operation in operations:    
            if operation == "+":
                sum_last_two_elmt = cal_point_arr[-2] + cal_point_arr[-1]
                cal_point_arr.append(sum_last_two_elmt)
            elif operation == "D":
                double_last_element = 2 * cal_point_arr[-1]
                cal_point_arr.append(double_last_element)
            elif operation == "C":
                cal_point_arr.pop()
            else:
                cal_point_arr.append(int(operation))
        return sum(cal_point_arr)
                


  
    

        