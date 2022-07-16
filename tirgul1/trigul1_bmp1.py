from tirgul1 import trigul1_bmp2
# using only in tests, so no cheating :)


# gets img path (bmp) and text and returns out path (bmp) with text hidden in the last bit of every pixel
def encode_pixels(img_path, text, out_path):
    # using marker to know where our text ends, we don't know when to stop
    end_marker = "|"
    bit_lst = create_bit_lst(text + end_marker)

    img = open(img_path, "rb")
    output_path = open(out_path, "wb")
    # I decided not to write at the beginning of the bmp but to start at location 4096
    # copy first 4096 bytes
    output_path.write(img.read(4096))
    bitmap = img.read()
    for bit_index in range(len(bit_lst)):
        # removing the last bit from each byte of the bmp and adding our new bit
        output_int = bitmap[bit_index] // 2 * 2 + bit_lst[bit_index]
        output_byte = output_int.to_bytes(1, byteorder='little')
        # write the new byte to the output file
        output_path.write(output_byte)

    # copying the rest of the bytes from the old file
    output_path.write(bitmap[len(bit_lst):])
    output_path.close()
    return output_path


def create_bit_lst(text):
    bit_lst = []
    for b in text.encode():
        # filling the bytes so all of them will be 8 char long
        byte = bin(b)[2:].rjust(8, '0')
        #        print("Binary of letter: ", s)
        for bit in byte:
            bit_lst.append(int(bit))
    #    print(bit_lst)
    return bit_lst


# =============================================================================
# Tests:
def test_bit_lst1():
    lst = [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0,
           1, 1, 1, 1]
    assert create_bit_lst("hello") == lst


def test_bit_lst2():
    lst = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1,
           0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1]
    assert create_bit_lst("שלום") == lst


def test_pixels1():
    orig_img = "img_input\\house2.bmp"
    new_file = "img_output\\house2.bmp"
    text = "this house looks nice!"
    encode_pixels(orig_img, text, new_file)
    expected_str = trigul1_bmp2.decode_pixels(new_file)
    assert expected_str == text


def test_pixels2():
    orig_img = "img_input\\man.bmp"
    new_file = "img_output\\man.bmp"
    text = "the man is very tall"
    encode_pixels(orig_img, text, new_file)
    expected_str = trigul1_bmp2.decode_pixels(new_file)
    assert expected_str == text
