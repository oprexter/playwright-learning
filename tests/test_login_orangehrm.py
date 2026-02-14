import re
from playwright.sync_api import Page, expect

from pages.orangehrm_login_page import loginpage
from pages.orangehrm_home_page import Homepage  


def test_case_1(logged_in_page: Page) -> None:
    
    
    
    
   
    home_obj = Homepage(logged_in_page)
    
    # 
    
    # login_obj.enter_username("Admin")
    # login_obj.enter_password("admin123")
    
    # login_obj.click_login()
    
    home_obj.upgrade_button_visible()
    home_obj.click_performance_link()
    home_obj.click_dashboard_link()
    
    #print("Test case 1 executed successfully")
    
    
    
def test_case_2(logged_in_page: Page):
    
    
   
    
    home_obj = Homepage(logged_in_page)
    
    
    
    
    
    home_obj.click_dashboard_link()
    home_obj.upgrade_button_visible()
    home_obj.click_performance_link()
    
    #print("Test case 2 executed successfully")

    
    
    

def test_case_3(logged_in_page: Page):
    
    
    home_obj = Homepage(logged_in_page)
    
    home_obj.click_performance_link()
    home_obj.perf_visible()
  
    #print("Test case 3 executed successfully")
    
    
