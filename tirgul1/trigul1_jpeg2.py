import os
# using only in tests, so no cheating :)


# gets img path(jpg) and returns hidden text
def decode_jpg(jpg_path):
    # opening in binary the path fie
    img = open(jpg_path, "rb")
    str_img = img.read()
    # jpeg file starts with FFD9, start stands for the index after bit  \xD9
    start = str_img.find(b'\xFF\xD9') + 2
    img.close()
    # returning the hidden text and decoding him, meaning we are converting him from bin to ascii
    return str_img[start::].decode('utf-8')


# ======================================================================================================================
# Tests:

def test_sheela_0():
    file = "img_input\\dog.jpg"
    assert decode_jpg(file) == ""

def test_sheela_1():
    file = "img_input\\dog_tirgul1.jpg"
    assert decode_jpg(file) == "this is the cutest dog!😮😁"

def test_sheela_2():
    file = "img_input\\capybara.jpg"
    assert decode_jpg(file) == "capybara is the best animal!!"

