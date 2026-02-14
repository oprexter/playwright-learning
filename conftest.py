import pytest
import os
from datetime import datetime
from pages.orangehrm_login_page import loginpage
# from playwright.sync_api import sync_playwright


# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()


@pytest.fixture(scope="session")
def logged_in_page(browser):
   
   
   
   
   page = browser.new_page()

   page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

   login_page = loginpage(page)
   login_page.enter_username("Admin")
   login_page.enter_password("admin123")
   login_page.click_login()

    # Wait for dashboard
    #page.wait_for_url("**/dashboard")

   yield page   # All tests will use this same page

    # 🔥 Logout after ALL tests finish
   page.locator(".oxd-userdropdown").click()  # Open user dropdown
   page.click("text=Logout")

   page.close()
   


# ---------------- PYTEST HOOK ----------------
def pytest_runtest_logreport(report):
    if report.when == "call" and report.outcome == "passed":
        file_name, *_, test_name = report.nodeid.split("::")
        print(f"\n✅ {test_name.replace('_', ' ').title()} Successful")
        
        
# =====================================================
# HOOK → Take Screenshot On Test Failure (PRODUCTION READY)
# =====================================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    # Let pytest run test first
    outcome = yield
    report = outcome.get_result()

    # Only when actual test fails
    if report.when == "call" and report.failed:

        # Get playwright page from fixture
        page = item.funcargs.get("logged_in_page", None)

        if page:
            # Create folder if not exists
            os.makedirs("reports/screenshots", exist_ok=True)

            # Create unique screenshot name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"reports/screenshots/{item.name}_{timestamp}.png"
            # Capture screenshot
            page.screenshot(path=file_name)

            print(f"\n📸 Screenshot saved: {file_name}")