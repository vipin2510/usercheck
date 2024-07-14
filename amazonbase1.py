from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_user_existence(phone_number):
    # Set up the WebDriver (make sure you have the appropriate driver installed)
    driver = webdriver.Chrome()  # Or use Firefox, Edge, etc.

    try:
        # Navigate to the Amazon sign-in page
        driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        # Wait for the phone/email input field to be visible
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_email"))
        )

        # Enter the phone number
        input_field.send_keys(phone_number)

        # Find and click the "Continue" button
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        # Wait for the page to load and check for user existence
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "auth-password-missing-alert"))
        )

        # If we reach this point, the user exists
        return True

    except Exception as e:
        # If an exception occurs, assume the user doesn't exist
        print(f"Error: {e}")
        return False

    finally:
        # Close the browser
        driver.quit()

# Example usage
phone_number = "vipingautamooooo16@gmail.com"  # Replace with the phone number you want to check
user_exists = check_user_existence(phone_number)
print(f"User exists: {user_exists}")