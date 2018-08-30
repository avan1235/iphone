def delete_spaces(str):
    where_space = str.find(" ")
    while where_space > -1:
        temp1 = str[0:where_space]
        temp2 = str[where_space+1:len(str)]
        str = temp1 + temp2
        where_space = str.find(" ")
    return str