Detailed Test Cases

Project: SauceDemo (Swag Labs)
Tester: Nazar Bazhan
Date: 2026-02-02

---

ID: TC-01
Summary: Verify successful product purchase
Preconditions: User is on the Login page.
Steps:
1. Enter valid username and password.
2. Click the "Login" button.
3. On the Inventory page, click "Add to cart" for the first item.
4. Click on the "Cart" icon in the top right corner.
5. Click the "Checkout" button.
6. Fill in the form fields: First Name, Last Name, Zip Code.
7. Click "Continue".
8. Click "Finish" on the Overview page.
Postconditions: User is logged out or cart is cleared for next session.
Expected Results: User sees the "CHECKOUT: COMPLETE!" page with the message "Thank you for your order!".
Actual Results: User saw the "Thank you for your order!" message.
Status: Pass.

---

ID: TC-02
Summary: Verify Login with Locked Out User
Preconditions: User is on the Login page.
Steps:**
1. Enter username: "locked_out_user".
2. Enter password: "secret_sauce".
3. Click the "Login" button.
Postconditions: None.
Expected Results: Login is denied. An error message appears: "Sorry, this user has been locked out."
Actual Results: Error message displayed as expected.
Status: Pass.

---

ID: TC-03
Summary: Verify 'Name (Z to A)' Sorting Functionality (Negative Scenario)
Preconditions:
1. User is logged in as "problem_user" (to reproduce the known bug).
2. User is on the Inventory page.
Steps:
1. Click on the Sort Dropdown menu.
2. Select the "Name (Z to A)" option.
3. Observe the order of the product list.
Postconditions: None.
Expected Results: The product list should be reordered alphabetically from Z to A.
Actual Results: The product list did not change.
Status:Fail (See Bug Report **FUNC-002**)