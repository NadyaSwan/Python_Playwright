class LoginPage:
    INVALID_CREDENTIALS_ERROR_TEXT = 'Epic sadface: Username and password do not match any user in this service'
    LOCKED_USER_ERROR_TEXT = 'Epic sadface: Sorry, this user has been locked out.'

    def __init__(self, page):
        self.page = page

    def goto(self):
        return self.page.goto('https://www.saucedemo.com')

    def username_input(self):
        return self.page.locator('#user-name')

    def password_input(self):
        return self.page.locator('#password')

    def login_button(self):
        return self.page.locator('#login-button')

    def login_error_label(self):
        return self.page.locator('[data-test="error"]')

    def log_in(self, username, password):
        self.goto()
        self.username_input().fill(username)
        self.password_input().fill(password)
        self.login_button().click()

