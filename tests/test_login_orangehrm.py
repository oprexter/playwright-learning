import re
from playwright.sync_api import Page, expect

from pages.orangehrm_login_page import loginpage
from pages.orangehrm_home_page import Homepage  


def test_case_1(page: Page) -> None:
    
    login_obj = loginpage(page)
    home_obj = Homepage(page)
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_obj.enter_username("Admin")
    login_obj.enter_password("admin123")
    
    login_obj.click_login()
    
    home_obj.upgrade_button_visible()
    home_obj.click_performance_link()
    home_obj.click_dashboard_link()
    
    
    
def test_case_2(page: Page):
    
    
   
    login_obj = loginpage(page)
    home_obj = Homepage(page)
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_obj.enter_username("Admin")
    login_obj.enter_password("admin123")
    
    login_obj.click_login()
    
    home_obj.click_dashboard_link()
    home_obj.upgrade_button_visible()
    home_obj.click_performance_link()
    
    

    
    
    
    # without pom write below code
    
    # page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # page.get_by_role("textbox", name="Username").fill("Admin")
    
    # page.get_by_role("textbox", name="Password").fill("admin123")
    # page.get_by_role("button", name="Login").click()
    # expect(page.get_by_role("button", name="Upgrade")).to_be_visible()
    # page.get_by_role("link", name="Performance").click()
    # page.get_by_role("link", name="Dashboard").click()
    
    
