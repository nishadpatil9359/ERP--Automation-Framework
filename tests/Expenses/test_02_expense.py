import time
from playwright.sync_api import expect

from tests.Payment_Type.test_01_payment_type import create_payment_type
from tests.Expenses.test_01_expense_category import create_expense_category


def create_expense(page, payment_type, category_name):
    expense_for = f"Production_{int(time.time())}"
    reference_number = f"EXP{int(time.time() * 1000)}"
    amount = "500"

   # Open Expense Module
    page.goto("https://uat.bharatbill.live/business/expenses")
    page.wait_for_load_state("networkidle")

    # Click Add New
    page.get_by_role("link", name=" Add new").click()

    # Amount
    page.get_by_placeholder("Enter Amount", exact=True).fill(amount)

    # Expense Category
    page.locator(
        '#expenses-create-modal select[name="expense_category_id"]'
    ).select_option(label=category_name)

    # Expense For
    page.get_by_role(
        "textbox",
        name="Enter Expense For"
    ).fill(expense_for)

    # Payment Type
    page.locator(
        '#expenses-create-modal select[name="payment_type_id"]'
    ).select_option(label=payment_type)

    # Reference Number
    page.get_by_role(
        "textbox",
        name="Enter reference number"
    ).fill(reference_number)

    # Description (optional)
    page.get_by_role(
        "textbox",
        name="Enter note"
    ).fill("Expense created through Playwright Automation")

    # Save
    page.get_by_role("button", name="Save").click()

    # Wait for save
    page.wait_for_timeout(1500)

    # Search Expense
    page.get_by_role(
        "textbox",
        name="Search"
    ).fill(reference_number)

    # Verify
    expect(page.get_by_text(reference_number).first).to_be_visible(timeout=10000)


def test_create_expense(page):
    payment_type = create_payment_type(page)

    category_name = create_expense_category(page)

    create_expense(
        page,
        payment_type,
        category_name
    )