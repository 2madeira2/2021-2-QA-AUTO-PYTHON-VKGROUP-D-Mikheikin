from selenium.webdriver.common.by import By

BUTTON_LOG_LOCATOR = (By.XPATH, r'//div[contains(@class, "responseHead-module-button")]')
EMAIL_LOCATOR = (By.NAME, 'email')
PASSWORD_LOCATOR = (By.NAME, 'password')
BUTTON_AUTH_LOCATOR = (By.XPATH, r'//div[contains(@class, "authForm-module-button")]')

CLICK_LIST_LOGOUT_LOCATOR = (By.XPATH, r'//div[contains(@class, "right-module-rightButton")]')
CLICK_BUTTON_LOGOUT_LOCATOR = (By.XPATH, r'//a[@href="/logout"]')
SPINNER_LOCATOR = (By.XPATH, '//div[contains(@class, "spinner")]')

PROFILE_LOCATOR = (By.XPATH, r"//a[@href='/profile']")
NAME_LOCATOR = (By.XPATH, '//div[@data-name = "fio"]/div/input')
PHONE_LOCATOR = (By.XPATH, '//div[@data-name = "phone"]/div/input')
SAVE_PROFILE_LOCATOR = (By.XPATH, '//div[@class = "profile-contact-info"]/div/button[@class = "button button_submit"]')

BALANCE_TAB_LOCATOR = (By.XPATH, r'//a[contains(@class, "center-module-billing")]')
PAYER_INSCRIPTION_LOCATOR = (By.XPATH, r'//div[@class = "deposit__payment-form__title"]')

TOOLS_TAB_LOCATOR = (By.XPATH, r'//a[contains(@class, "center-module-tools")]')
TOOLS_ADD_FEED_BUTTON_LOCATOR = (By.XPATH, r'//div[contains(@class, "feeds-module-addButton")]')

