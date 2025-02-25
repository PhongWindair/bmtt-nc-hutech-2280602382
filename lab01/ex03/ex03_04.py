def truycap(tuple_data):
    f_element = tuple_data[0]
    l_element = tuple_data[-1]
    return f_element, l_element

input_tuple = (eval(input("Nhập vào một tuple: ")))
first, last = truycap(input_tuple)

print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)