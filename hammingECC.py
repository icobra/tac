#!/usr/bin/python3

"""
Код хемминга 16-5. Кодер/декодер + коррекция ошибки
"""

ECC_POS =([0,1,3,4,6,8,10,11,13,15], [0,2,3,5,6,9,10,12,13],
          [1,2,3,7,8,9,10,14,15], [4,5,6,7,8,9,10], [11,12,13,14,15])
POSITION16_5 = (11,4,1,0,0)
ECC_POS21 = ([2,4,6,8,10,12,14,16,18,20], [2,5,6,9,10,13,14,17,18],
             [4,5,6,12,13,14,19,20], [8,9,10,11,12,13,14], [16,17,18,19,20])
POSITION21 = (0,1,3,7,15)

def is_bool(variable):
    old_bool = variable
    new_bool = [x for x in old_bool if x in ["0","1"]]
    if len(old_bool) != len(new_bool):
        return False
    else:
        return True
    
def counter(position, variable):
    list_bool = list(str(variable))    
    ecc_value = []

    for item_on_place in position:
        new_list = item_on_place
        y = 0
        for x in new_list:
            if int(list_bool[int(x)]) == 1:
                y += 1
        if y % 2 == 0:
            ecc_value.append(0)
        else:
            ecc_value.append(1)
    return ecc_value
  
def to_hemming(variable, position = POSITION16_5):
    bit16 = str(variable)
    
    if len(bit16) != 16:
        return ("Error кооличество разрядов не равно 16")
    elif is_bool(bit16) != True:
        return ("Число не двоичное")

    ecc_date = counter(ECC_POS, bit16)
    print(ecc_date)
    bit16 = list(bit16)

    for x in position:
        bit16.insert(int(x), str(ecc_date.pop()))

    bit21 = ''.join(bit16)
    return(bit21)

def to_16bit(variable):
    def checker(variable, ecc21_date):
        list_21 = list(str(variable))
        ecc_old = []
        for x in POSITION21:
            a = list_21[x]
            ecc_old.append(int(a))
        error_list = []
        for x in range(0,5):
            if ecc21_date[x] == ecc_old[x]:
                pass
            else:    
                error_list.append(x)
        return error_list


    bit21ecc = str(variable)
    
    if len(bit21ecc) != 21:
        return ("Error число разрядов не 21")
    elif is_bool(bit21ecc) != True:
        return ("Число не двоичное")

    ecc21_date = counter(ECC_POS21, bit21ecc)
    err_list = checker(bit21ecc, ecc21_date)

    bit21ecc = list(bit21ecc)
    if err_list:
        print("1 error found")
        err_pos = 0
        for x in err_list:
            err_pos += (POSITION21[x] + 1)
        err_pos -= 1    
        print("Error fix. Позиция ошибки:", err_pos)
        if bit21ecc[err_pos] == 0:
            del bit21ecc[err_pos]
            bit21ecc.insert(err_pos, '1')
        else:
            del bit21ecc[err_pos]
            bit21ecc.insert(err_pos, '0')
    
    #Преобразуем число, убирая контроль четности
    for x in [15, 7, 3, 1, 0]:
        del bit21ecc[x]
    bit16_len = ''.join(bit21ecc)    
    return bit16_len



def test():

    a = "0123456789ABCDEF"
    num1 = 1010101010101010
    num2 = 3459010101018101
    num3 = "1011111011111010"
    num4 = "iiojijfrelkfjreklfjerklfjreklfjrkegfj"
    habra_word = "0100010000111101"

    ecc1 = "111001001010101001010"
    ecc2 = "fdfhjkdhfjdshfjkdshfljksdhfjk"
    ecc3 = "101001101110111111110"
    ecc4 = "0110111111101111101000000"
    habra_word_21_test = "100110000100001011101"

    print("\nCoder test")
    k = to_hemming(a)
    print(k)
    k = to_hemming(num1)
    print(k)
    k = to_hemming(num2)
    print(k)
    k = to_hemming(num3)
    print(k)
    k = to_hemming(num4)
    print(k)
    print("habra_word ", habra_word)
    habra_word_21 = to_hemming(habra_word)
    print(habra_word_21)

    print("\nDecoder test")
    print("Значение равно ", ecc1)
    g = to_16bit(ecc1)
    print(g)
    g = to_16bit(ecc2)
    print(g)
    print("Значение равно ", ecc3)
    g = to_16bit(ecc3)
    print(g)
    g = to_16bit(ecc4)
    print(g)
    habra_word_16b = to_16bit(habra_word_21)
    print("habra_word 16bit ", habra_word_16b)


    print("Проверка перевода")
    print("Сравним хабра слова ", habra_word == habra_word_16b )

test()    


"""
trash
    position1 = (1, 2, 4, 5, 7, 9, 11, 12, 14, 16)
    position2 = (1, 3, 4, 6, 7, 10, 11, 13, 14)
    position4 = (2, 3, 4, 8, 9, 10, 15, 16)
    position8 = (5, 6, 7, 8, 9, 10, 11)
    position16 = (12, 13, 14, 15, 16)
               0123456789ABCDEF
       
                  

    position2 = (1, 3, 4, 6, 7, 10, 11, 13, 14)
    position4 = (2, 3, 4, 8, 9, 10, 15, 16)
    position8 = (5, 6, 7, 8, 9, 10, 11)
    position16 = (12, 13, 14, 15, 16)


def counter(position, variable):
    list_bool = list(str(variable))
    place = list(position)
    y = 0  
    for x in place:
        if int(list_bool[int(x)-1]) == 1:
            y += 1
    if y % 2 == 0:
        return 1
    else:
        return 0 

"""