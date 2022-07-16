def is_hiding_info_at_pixel(img_path):
    file = open(img_path, "rb")
    byte_lst = file.read()

    # checking if the file format is bmp
    if byte_lst[:2] != b'BM':
        return "Invalid file type, expected BMP"

    bit_lst = []
    for bite in byte_lst:
        bit_lst.append(bite % 2)

    output = []
    for bitoffset in range(8):
        for i in range(len(bit_lst) // 8):
            byte = bit_lst[8 * i + bitoffset:8 * i + 8 + bitoffset]
            bin_letter = 0
            for bit in byte:
                bin_letter = bin_letter * 2 + bit
            ch = chr(bin_letter)
            if ch.isalnum():
                output.append(ch)
            else:
                output.append(" ")
    all_string = ''.join(output)
    strings = all_string.split()

    dict = open("words_alpha.txt", "r")
    dict_lst = dict.readlines()
    dict_set = set()
    for word in dict_lst:
        dict_set.add(word[:-1])

    valid_words = []
    for str in strings:
        if str in dict_set and len(str) > 2:
            valid_words.append(str)

    print("FOUNDS ", len(valid_words), " words: ", valid_words)
    return len(valid_words) > 2


def test_file_format():
    assert is_hiding_info_at_pixel('img_input\\capybara.jpg') == "Invalid file type, expected BMP"


def test_file_format2():
    assert is_hiding_info_at_pixel('img_input\\bmp_wiki_tests.txt') == "Invalid file type, expected BMP"


def test_bmp1():
    assert is_hiding_info_at_pixel('img_output\\house.bmp') == True


def test_bmp2():
    assert is_hiding_info_at_pixel('img_output\\house2.bmp') == True


def test_bmp3():
    assert is_hiding_info_at_pixel('img_output\\man.bmp') == True
