nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [elem_third for elem_first in nice_list
            for elem_second in elem_first for elem_third in elem_second]

print(f"Ответ: {new_list}")
