import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_bascket_button_is_here(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
    time.sleep(10)

    #pytest -s -v --browser_name=firefox --language=es test_items.py