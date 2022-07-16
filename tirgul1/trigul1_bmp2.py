from tirgul1 import trigul1_bmp1
# using only in tests, so no cheating :)


def decode_pixels(img_path):
    file = open(img_path, "rb")
    # copy first 4096 bytes
    file.seek(4096)
    byte_lst = file.read()
    bit_lst = []
    # adding the last bit of each byte to bit_lst
    for byte in byte_lst:
        bit_lst.append(byte % 2)

    output = []
    # connecting the lst bits to bytes
    for i in range(len(bit_lst)//8):
        byte = bit_lst[8*i:8*i+8] # each time skip to next byte
        bin_letter = 0
        # converting the list of 8 bits to int by shifting left
        for bit in byte:
            bin_letter = bin_letter*2 + bit
        # stopping at the end marker
        if chr(bin_letter) == '|':
            break
        output.append(chr(bin_letter))
    # joining list of chars to the str
    final_str = ''.join(output)
    return final_str

# Tests:
def test_pixels1():
    orig_img = "img_input\\house2.bmp"
    new_file = "img_output\\house2.bmp"
    text = "this house looks nice!"
    trigul1_bmp1.encode_pixels(orig_img, text, new_file)
    expected_str = decode_pixels(new_file)
    assert expected_str == text

def test_pixels2():
    orig_img = "img_input\\man.bmp"
    new_file = "img_output\\man.bmp"
    text = "the man is very tall"
    trigul1_bmp1.encode_pixels(orig_img, text, new_file)
    expected_str = decode_pixels(new_file)
    assert expected_str == text
