import time
from playwright.sync_api import expect


def create_expense_category(page):
    print("\nCreating Expense Category...")

    category_name = f"Automation_Expense_Category_{int(time.time())}"
    description = "Created by Playwright Automation"

    # Open Expense Category page
    page.goto("https://uat.bharatbill.live/business/expense-categories")

    # Click Add New
    page.get_by_role("link", name="Add new").click()

    # Fill Category Name
    page.get_by_role("textbox", name="Enter catgeory Name").fill(category_name)

    # Fill Description
    page.get_by_role("textbox", name="Enter Description").fill(description)

    # Save
    page.get_by_role("button", name="Save").click()

    # Wait for save
    page.wait_for_timeout(1500)

    # Search Category
    page.get_by_placeholder("Search...").fill(category_name)

    page.wait_for_timeout(1000)

    # Verify
    expect(page.get_by_text(category_name).first).to_be_visible()

    print(f"✅ Expense Category Created Successfully: {category_name}")

    return category_name


def test_create_expense_category(page):
    create_expense_category(page)