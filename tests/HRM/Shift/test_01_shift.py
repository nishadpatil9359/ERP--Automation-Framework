import time

from utils.navigation import open_shift


def create_shift(page):

    print("\nCreating Shift...")

    timestamp = int(time.time())

    shift_name = f"Automation_Shift_{timestamp}"

    # Navigate to Shift
    open_shift(page)

    # Add Shift
    page.locator("a").filter(
        has_text="Add Shift"
    ).click()

    # Shift Name
    page.locator(
        "#shift_create_name"
    ).fill(shift_name)

    # Start Time
    page.locator(
        "#shift_create_start_time"
    ).fill("17:00")

    # End Time
    page.locator(
        "#shift_create_end_time"
    ).fill("23:00")

    # Break = Yes
    page.locator(
        "#shift_create_break_status"
    ).select_option("1")

    # Start Break
    page.locator(
        "#shift_create_start_break_time"
    ).fill("19:00")

    # End Break
    page.locator(
        "#shift_create_end_break_time"
    ).fill("20:00")

    # Save
    page.get_by_role(
        "button",
        name="Save"
    ).click()

    page.wait_for_timeout(1500)

    print(
        f"✅ Shift Created : {shift_name}"
    )

    return shift_name


def test_create_shift(page):

    create_shift(page)