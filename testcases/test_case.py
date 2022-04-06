from datetime import datetime
from time import sleep, time
import pytest
import os

@pytest.mark.usefixtures("setup")
class TestFillAndSaveSign():
    def test_fill_name(self):
        driver = self.driver
        ts = time()
        timestamp = datetime.fromtimestamp(ts).strftime('%d%m%Y%H%M%S')
        # Scroll down the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Fill in the name and click "Next"
        import pdb; pdb.set_trace()
        input_name = driver.find_element_by_id("name")
        input_name.send_keys("First Name " + str(timestamp) )
        next_button = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[4]/div/a[1]")
        next_button.click()
        
        
        # Scroll down the page and take a screenshot in the screenshot folder with a timestamp
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        
        path = os.path.join(os.getcwd(), 'screenshots')
        extention = ".png"
        new_window = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[4]")
        new_window.screenshot(os.path.join(path, timestamp+extention))

        # import pdb; pdb.set_trace()
        sign_button = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[4]/div[1]/a[1]/div")
        sign_button.click()

        sleep(5)
        assert "Document signed!" in driver.page_source