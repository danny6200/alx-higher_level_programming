#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                num1 = my_list_1[i]
                num2 = my_list_2[i]
                is_num1 = isinstance(num1, (int, float))
                is_num2 = isinstance(num2, (int, float))

                if (is_num1 and is_num2) and num2 != 0:
                    division_result = num1 / num2
                else:
                    division_result = 0
                    if not is_num1 or not is_num2:
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
