import os #using only in tests, so no cheating :)


def encode_jpg(jpg_path, text, output_path): #gets img path(jpeg) and returns other img path(jpeg) with given text
    img = open(jpg_path, "rb") # opening in binary the path fie
    output_path = open(output_path, "wb")
    output_path.write(img.read())
    output_path.write(text.encode()) # converting the text to binary and adding it to the output path
    output_path.close() # closing the file, can also write "with _______ as _______" which also closes the file
    return output_path




# Tests:
def test_sheela_1():
    orig_file = "img_input\\cat.jpg"
    new_file = "img_output\\new_cat.jpg"
    text = "hello"
    if os.path.exists(new_file):
        os.remove(new_file)
    encode_jpg(orig_file, text, new_file)

    file_size = os.path.getsize(new_file)
    final_img = open(new_file, "rb")
    text_len = len(text.encode())
    final_img.seek(file_size-text_len)
    bin_text = final_img.read()
    found_text =  bin_text.decode('utf-8')
    assert found_text == text


def test_sheela_2():
    orig_file = "img_input\\dog.jpg"
    new_file = "img_output\\new_dog.jpg"
    text = "this is a cute dog!😮😁"
    if os.path.exists(new_file):
        os.remove(new_file)
    encode_jpg(orig_file, text, new_file)
    file_size = os.path.getsize(new_file)
    final_img = open(new_file, "rb")
    text_len = len(text.encode())
    pos = file_size - text_len
    final_img.seek(pos)
    bin_text = final_img.read()
    found_text = bin_text.decode('utf-8')
    assert found_text == text

def test_sheela_3():
    orig_file = "img_input\\capybara.jpg"
    new_file = "img_output\\new_capybra.jpg"
    text = "I love capybaras"
    if os.path.exists(new_file):
        os.remove(new_file)
    encode_jpg(orig_file, text, new_file)

    file_size = os.path.getsize(new_file)
    final_img = open(new_file, "rb")
    text_len = len(text.encode())
    pos = file_size - text_len
    final_img.seek(pos)
    bin_text = final_img.read()
    found_text = bin_text.decode('utf-8')
    assert found_text == text

