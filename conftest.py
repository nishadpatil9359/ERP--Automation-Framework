import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def page():
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=300
    )

    context = browser.new_context()

    page = context.new_page()

    # Login
    page.goto("https://uat.bharatbill.live/login")
 
    page.get_by_role(
        "textbox",
        name="Enter your Email"
    ).fill("info.aimautomation@gmail.com")

    page.get_by_role(
        "textbox",
        name="Password"
    ).fill("123456")

    page.get_by_role(
        "button",
        name="Log In"
    ).click()

    page.wait_for_load_state("networkidle")

    print("\n Login Successful\n")

    yield page

    print("\n Closing Browser\n")

    context.close()
    browser.close()
    playwright.stop()