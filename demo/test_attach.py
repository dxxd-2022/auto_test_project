import allure


def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)
def test_attach_html():
    allure.attach("这是一段htmlbody块","html测试块",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file(r"C:\Users\HTD\picture\photo.jpg",name="这是一张图片",attachment_type=allure.attachment_type.JPG)
def test_attach_video():
    allure.attach.file(name="这是一段视频",attachment_type=allure.attachment_type.MP4)