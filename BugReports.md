Project: SauceDemo
Tester: Nazar Bazhan
Date: 31.01.2026

### Summary

| ID | Summary (Title) | Severity | Priority | Status |
|-----------------------------------------------------|
| FUNC-001 | Dog image shown instead of product for "problem_user" | Medium | Medium | Open |
| FUNC-002 | Sorting "Z to A" fails for "problem_user" | Medium | Low | Open |

### Detailed Descriptions

---
[FUNC-001] Dog image shown instead of product
Severity: Medium (Content Error)
Environment: Chrome / Windows 11
Description: When logged in as "problem_user", product images are replaced with a placeholder dog image.
Steps to Reproduce:
    1. Log in as "problem_user".
    2. Go to Products page.
    3. Observe product images (e.g., "Sauce Labs Backpack").
Actual Result: The product image is replaced with a generic placeholder image (dog).
Expected Result: Correct product image should be displayed.
---
[FUNC-002] Sorting "Z to A" fails for "problem_user"
Severity: Medium (Functional Error)
Environment: Chrome / Windows 11
Description: The sorting feature fails to reorder the inventory list when 'Name (Z to A)' is selected; items remain in the default "A to Z" order.
Steps to Reproduce:
    1. Log in to https://www.saucedemo.com/ as "problem_user".
    2. Click on the sort dropdown menu (top right corner).
    3. Select the option "Name (Z to A)".
Actual Result: The product list does not change; items remain in the original order (A to Z).
Expected Result: The product list should be resorted alphabetically in descending order (from Z to A).
---