#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                num1 = my_list_1[i]
                num2 = my_list_2[i]

                if (isinstance(num1, (int, float)) and isinstance(num2, (int, float))) and num2 != 0:
                    division_result = num1 / num2
                else:
                    division_result = 0
                    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                        print("wrong type")
                    if num2 == 0:
                        print("division by 0")
            except IndexError:
                division_result = 0
                print("out of range")
            finally:
                result.append(division_result)
    except Exception as e:
        print(f"An error occurred: {e}")
    return result
