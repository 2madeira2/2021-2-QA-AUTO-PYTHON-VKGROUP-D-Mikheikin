from selenium.webdriver.common.by import By

BUTTON_LOG = (By.XPATH, r'//div[contains(@class, "responseHead-module-button")]')
EMAIL_LOC = (By.NAME, 'email')
PASSWORD_LOC = (By.NAME, 'password')
BUTTON_AUTH_LOC = (By.XPATH, r'//div[contains(@class, "authForm-module-button")]')

CLICK_LIST_LOGOUT = (By.XPATH, r'//div[contains(@class, "right-module-rightButton")]')
CLICK_BUTTON_LOGOUT = (By.XPATH, r'//a[@href="/logout"]')
SPINNER_LOC = (By.XPATH, '//div[contains(@class, "spinner")]')

PROFILE_LOC = (By.XPATH, r"//a[@href='/profile']")
NAME_LOC = (By.XPATH, '//div[@data-name = "fio"]/div/input')
PHONE_LOC = (By.XPATH, '//div[@data-name = "phone"]/div/input')
SAVE_LOC = (By.XPATH, '//div[@class = "profile-contact-info"]/div/button[@class = "button button_submit"]')

BALANCE_TAB_LOC = (By.XPATH, r'//a[contains(@class, "center-module-billing")]')
PAYER_INSCRIPTION = (By.XPATH, r'//div[@class = "deposit__payment-form__title"]')

TOOLS_TAB_LOC = (By.XPATH, r'//a[contains(@class, "center-module-tools")]')
TOOLS_ADD_FEED_BUTTON = (By.XPATH, r'//div[contains(@class, "feeds-module-addButton")]')

