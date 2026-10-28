
import time

from utils.navigation import open_leave_type


def close_open_modals(page):
    """Close the Add Leave modal if it is already open."""

    modal = page.locator("#create-leave-modal")

    if modal.is_visible():
        cancel_button = modal.get_by_role(
            "button",
            name="Cancel"
        )

        if cancel_button.is_visible():
            cancel_button.click()
        else:
            page.keyboard.press("Escape")


def create_leave_type(page):
    print("\nCreating Leave Type...")

    close_open_modals(page)
    open_leave_type(page)

    timestamp = int(time.time())
    leave_type_name = f"Automation_Leave_Type_{timestamp}"

    # Open Add Leave Type modal
    add_button = page.get_by_role(
        "link",
        name="Add Leave Type",
        exact=True
    )

    add_button.click()

    # Wait for the correct modal
    modal = page.locator("#create-leave-type-modal")
    modal.wait_for(state="visible", timeout=10000)

    # Fill Leave Type Name
    modal.locator("input[name='name']").fill(
        leave_type_name
    )

    # Fill Description
    modal.locator("textarea[name='description']").fill(
        "Created by Playwright Automation"
    )

    # Save Leave Type
    modal.get_by_role(
        "button",
        name="Save",
        exact=True
    ).click()

    # Verify the created record in the table
    page.get_by_text(
        leave_type_name,
        exact=True
    ).wait_for(state="visible", timeout=15000)

    print(f"Leave Type Created Successfully: {leave_type_name}")

    return leave_type_name


def test_create_leave_type(page):
    create_leave_type(page)
