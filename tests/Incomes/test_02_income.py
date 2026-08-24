import time
from datetime import datetime
from playwright.sync_api import expect

from tests.Payment_Type.test_01_payment_type import create_payment_type
from tests.Incomes.test_01_income_category import create_income_category


def test_create_income(page):

    # Step 1: Create Payment Type
    payment_type = create_payment_type(page)

    # Step 2: Create Income Category
    category_name = create_income_category(page)

    # Step 3: Open Income Module
    page.goto("https://uat.bharatbill.live/business/incomes")
    page.wait_for_load_state("networkidle")

    timestamp = int(time.time())

    amount = "30000"
    income_for = f"Automation Income {timestamp}"
    reference_number = f"REF{timestamp}"
    note = f"Created by Playwright {timestamp}"
    income_date = datetime.now().strftime("%Y-%m-%d")

    # Add New Income
    page.get_by_role("link", name=" Add new").click()

    # Amount
    page.get_by_role("spinbutton").fill(amount)

    # Income Category
    page.locator(
        '#incomes-create-modal select[name="income_category_id"]'
    ).select_option(label=category_name)

    # Income For
    page.get_by_role(
        "textbox",
        name="Enter income for"
    ).fill(income_for)

    # Wait for Payment Type dropdown
    payment_dropdown = page.locator(
        '#incomes-create-modal select[name="payment_type_id"]'
    )

    expect(payment_dropdown).to_be_visible()

    page.wait_for_timeout(1000)

    # Select the newly created Payment Type
    payment_dropdown.select_option(label=payment_type)

    # Reference Number
    page.get_by_role(
        "textbox",
        name="Enter reference number"
    ).fill(reference_number)

    # Date
    page.locator(
        '#incomes-create-modal input[name="incomeDate"]'
    ).fill(income_date)

    # Note
    page.get_by_role(
        "textbox",
        name="Enter note"
    ).fill(note)

    # Save
    page.get_by_role(
        "button",
        name="Save"
    ).click()

    page.wait_for_timeout(1500)

    # Search
    page.get_by_placeholder("Search...").fill(reference_number)

    # Verify
    expect(page.get_by_text(income_for).first).to_be_visible(timeout=10000)

    print(f"\n✅ Income Created : {income_for}")