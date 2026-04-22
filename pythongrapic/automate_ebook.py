from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    print ("processing....")

    page.goto("https://ostad.app/", wait_until="networkidle")

    # generate pdf 

    page.pdf(path="rostad.pdf", format="A4", print_background=True)


    print ("pdf created completed.....")


