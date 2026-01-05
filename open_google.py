from playwright.sync_api import sync_playwright
import time


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        title = page.title()
        print(title)
        
        input("Press Enter to close the browser...")
        browser.close()


if __name__ == "__main__":
    main()
    
    
    
 ## code explanation 
#  sync_playwright is a tool useed to control browser in synchronous way.
 
#  browser = p.chromium.launch(headless=False) 
#  the above line launches a chromium crowsere in non headless mode (visible mode)
 
#  page = browser.new_page() 
#  the above line creates a new page in the browser
 
#  page.goto("https://www.google.com")
#  the above line navigates to google home page
 
#  title = page.title()     
#  the above line gets the title of the current page
 
#  then prints the title and closes the browser.