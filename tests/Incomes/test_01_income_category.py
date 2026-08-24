import time
from playwright.sync_api import expect


def create_income_category(page):
    """
    Create a new Income Category and return its name.
    """

    page.goto("https://uat.bharatbill.live/business/income-categories")
    page.wait_for_load_state("networkidle")

    category_name = f"Automation_Category_{int(time.time())}"

    page.get_by_role("link", name=" Add new").click()

    page.get_by_role(
        "textbox",
        name="Enter catgeory name"
    ).fill(category_name)

    page.get_by_role(
        "textbox",
        name="Enter Description"
    ).fill(f"Created by Playwright - {category_name}")

    page.get_by_role(
        "button",
        name="Save"
    ).click()

    page.wait_for_load_state("networkidle")

    expect(
        page.get_by_text(category_name).first
    ).to_be_visible()

    print(f"\n✅ Category Created : {category_name}")

    return category_name