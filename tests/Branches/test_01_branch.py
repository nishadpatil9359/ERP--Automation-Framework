import time
from playwright.sync_api import expect


def create_branch(page):
    print("\nCreating Branch...")

    timestamp = int(time.time())

    branch_name = f"Automation_Branch_{timestamp}"
    phone = f"98{str(timestamp)[-8:]}"
    email = f"branch{timestamp}@gmail.com"
    address = "Ghansoli, Navi Mumbai"
    description = "Created by Playwright Automation"

    # Open Branches page
    page.goto("https://uat.bharatbill.live/business/branches")
    page.wait_for_load_state("networkidle")

    # Click Add Branch
    page.get_by_role("link", name="Add Branch").click()

    # Branch Name
    page.get_by_role(
        "textbox",
        name="Enter branch name"
    ).fill(branch_name)

    # Phone
    page.get_by_role(
        "textbox",
        name="Enter Phone"
    ).fill(phone)

    # Email
    page.get_by_role(
        "textbox",
        name="Enter Email"
    ).fill(email)

    # Address
    page.get_by_role(
        "textbox",
        name="Enter Address"
    ).fill(address)

    # Description
    page.get_by_role(
        "textbox",
        name="Enter Description"
    ).fill(description)

    # Save
    page.get_by_role(
        "button",
        name="Save"
    ).click()

    page.wait_for_timeout(1500)

    # Search Branch
    page.get_by_placeholder("Search...").fill(branch_name)

    # Verify
    expect(page.get_by_text(branch_name).first).to_be_visible(timeout=10000)

    print(f"✅ Branch Created Successfully: {branch_name}")

    return branch_name


def test_create_branch(page):
    create_branch(page)