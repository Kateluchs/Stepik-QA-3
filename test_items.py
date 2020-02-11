from selenium.common.exceptions import NoSuchElementException
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_bascket_button_is_here(browser):
    browser.get(link)
    try:
        browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    except NoSuchElementException:
        assert False, "button is not found"
    #pytest -s -v --browser_name=firefox --language=es test_items.py
    #pytest -s -v --language=es test_items.py