import time

from playwright.sync_api import expect

from utils.navigation import open_shift
from test_01_shift import create_shift


def update_shift(page):

    print("\nUpdating Shift...")

    timestamp = int(time.time())

    updated_shift = f"Updated_Shift_{timestamp}"

    # Navigate to Shift
    open_shift(page)

    # Edit latest/first shift
    page.get_by_role(
        "button"
    ).filter(
        has_text="Edit"
    ).first.click()

    # Shift Name
    page.locator(
        "#shift_eidt_name"
    ).fill(updated_shift)

    # Start Time
    page.locator(
        "#shift_start_time"
    ).fill("17:04")

    # End Time
    page.locator(
        "#shift_end_time"
    ).fill("23:04")

    # Start Break
    page.locator(
        "#edit_start_break_time"
    ).fill("19:05")

    # End Break
    page.locator(
        "#edit_end_break_time"
    ).fill("20:05")

    # Update
    page.get_by_role(
        "button",
        name="Update"
    ).click()

    page.wait_for_timeout(1500)

    # Verify
    expect(
        page.get_by_text(
            updated_shift
        ).first
    ).to_be_visible()

    print(
        f"✅ Shift Updated : {updated_shift}"
    )

    return updated_shift


def test_update_shift(page):

    create_shift(page)
    update_shift(page)