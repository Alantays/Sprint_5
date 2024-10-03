from locators import Locators


class TestConstructor:
    def test_navigate_to_sauces_section(self, driver, authorization):
        sauces = driver.find_element(*Locators.SAUCES_SECTION)
        sauces.click()
        sauces_div = driver.find_element(*Locators.SAUCES_DIV)
        assert "tab_tab_type_current__2BEPc" in sauces_div.get_attribute("class")

    def test_navigate_to_buns_section(self, driver, authorization):
        sauces = driver.find_element(*Locators.SAUCES_SECTION)
        sauces.click()
        buns = driver.find_element(*Locators.BUNS_SECTION)
        buns.click()
        buns_div = driver.find_element(*Locators.BUNS_DIV)
        assert "tab_tab_type_current__2BEPc" in buns_div.get_attribute("class")

    def test_navigate_to_toppings_section(self, driver, authorization):
        toppings = driver.find_element(*Locators.TOPPINGS_SECTION)
        toppings.click()
        toppings_div = driver.find_element(*Locators.TOPPINGS_DIV)
        assert "tab_tab_type_current__2BEPc" in toppings_div.get_attribute("class")