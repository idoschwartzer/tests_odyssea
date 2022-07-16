import os


def decode_jpg(jpg_path): #gets img path(jpg) and returns hidden text
    img = open(jpg_path, "rb") # opening in binary the path fie
    str_img = img.read()
    start = str_img.find(b'\xff\xd9') + 2
    img.close()
    return str_img[start::].decode('utf-8')


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

