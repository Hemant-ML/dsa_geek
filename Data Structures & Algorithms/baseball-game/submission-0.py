class Solution:
    def calPoints(self, operations: List[str]) -> int:
        cal_point_arr = []
        for operation in operations:
            n = len(cal_point_arr)
            if operation not in ("+","C","D"):
                cal_point_arr.append(int(operation))
            elif operation == "+":
                sum_last_two_elmt = cal_point_arr[n-2] + cal_point_arr[n-1]
                cal_point_arr.append(sum_last_two_elmt)
            elif operation == "D":
                double_last_element = 2 * cal_point_arr[n-1]
                cal_point_arr.append(double_last_element)
            elif operation == "C":
                cal_point_arr.pop()
        return sum(cal_point_arr)
                


  
    

        