import time
from playwright.sync_api import expect


def create_payment_type(page):
    print("\nCreating Payment Type...")

    payment_type = f"Automation_Payment_{int(time.time())}"

    # Open Payment Type page
    page.goto("https://uat.bharatbill.live/business/payment-types")

    # Click Add Payment Type
    page.get_by_role("link", name="Add Payemnt Type").click()

    # Enter Payment Type Name
    page.get_by_role("textbox", name="Enter Name").fill(payment_type)

    # Save
    page.get_by_role("button", name="Save").click()

    # Wait briefly for UI to stabilize
    page.wait_for_timeout(1500)

    # Search for created Payment Type
    search_box = page.get_by_placeholder("Search...")
    search_box.fill(payment_type)

    page.wait_for_timeout(1000)

    # Verify Payment Type exists
    expect(page.get_by_text(payment_type).first).to_be_visible()

    print(f"✅ Payment Type Created Successfully: {payment_type}")

    return payment_type


def test_create_payment_type(page):
    create_payment_type(page)