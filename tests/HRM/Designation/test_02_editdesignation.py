import time

from playwright.sync_api import expect

from utils.navigation import open_designation
from test_01_designation import create_designation


def update_designation(page):

    print("\nUpdating Designation...")

    timestamp = int(time.time())

    updated_designation = (
        f"Updated_Designation_{timestamp}"
    )

    # Navigate to Designation
    open_designation(page)

    # Edit latest/first designation
    page.get_by_role(
        "button",
        name="Edit"
    ).first.click()

    # Update Name
    page.locator(
        '#edit-designation-modal input[name="name"]'
    ).fill(updated_designation)

    # Update Description
    page.locator(
        '#edit-designation-modal textarea[name="description"]'
    ).fill(
        "Updated by Playwright Automation"
    )

    # Update
    page.get_by_role(
        "button",
        name="Update"
    ).click()

    page.wait_for_timeout(1500)

    # Verify
    expect(
        page.get_by_text(
            updated_designation
        ).first
    ).to_be_visible()

    print(
        f"✅ Designation Updated : {updated_designation}"
    )

    return updated_designation


def test_update_designation(page):

    create_designation(page)
    update_designation(page)