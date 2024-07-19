# from http.server import HTTPServer
#
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
#
# class LoginPageTests(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.server = HTTPServer(('localhost', 0), Application())
#         port = cls.server.socket.getsockname()[1]
#         url = f"http://localhost:{port}"
#         cls.selenium = webdriver.Firefox()
#         cls.selenium.implicitly_wait(5)
#         cls.browser = cls.selenium.current_window_handle
#         cls.url = url
#         cls.admin_user = UserFactory.create(role='ADMIN')
#         cls.client_user = UserFactory.create()
#         cls.non_existent_user = 'invaliduser'
#         cls.password = 'password'
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         cls.server.shutdown()
#         super().tearDownClass()
#
#     def test_homepage_not_logged_in(self):
#         self.selenium.get(self.url + '/')
#         title = self.selenium.find_element_by_tag_name('title').text
#         self.assertIn('Home - Weather App', title)
#         self.assertEqual(len(self.selenium.windows), 1)
#
#     def test_login_successful(self):
#         self.selenium.get(self.url + '/login')
#         username = self.selenium.find_element_by_id('id_username')
#         password = self.selenium.find_element_by_id('id_password')
#         submit = self.selenium.find_element_by_xpath('/html/body/div[1]/form/button')
#
#         username.send_keys(self.admin_user.username)
#         password.send_keys(Keys.RETURN)
#
#         # Wait until we see the Home Page again
#         while True:
#             current_handles = self.selenium.window_handles
#             if len(current_handles) > 1:
#                 self.selenium.switch_to.window(current_handles[-1])
#                 self.selenium.close()
#                 self.selenium.switch_to.window(current_handles[0])
#             elif len(current_handles) == 1:
#                 break
#
#         assert self.selenium.current_url == self.url + '/'
#         assert self.selenium.find_elements_by_link_text('Log out') != []
#
#     def test_login_with_wrong_credentials(self):
#         self.selenium.get(self.url + '/login')
#         username = self.selenium.find_element_by_id('id_username')
#         password = self.selenium.find_element_by_id('id_password')
#         submit = self.selenium.find_element_by_xpath('/html/body/div[1]/form/button')
#
#         username.send_keys(self.non_existent_user)
#         password.send_keys(Keys.RETURN)
#
#         # Wait until we see the Login Page again
#         while True:
#             current_handles = self.selenium.window_handles
#             if len(current_handles) > 1:
#                 self.selenium.switch_to.window(current_handles[-1])
#                 self.selenium.close()
#                 self.selenium.switch_to.window(current_handles[0])
#             elif len(current_handles) == 1:
#                 break
#
#         error_message = self.selenium.find_element_by_css_selector('.errorlist li').text
#         self.assertIn('Please enter a correct email address or username.', error_message)
#
#     def test_login_as_different_users(self):
#         self.selenium.get(self.url + '/login')
#         username = self.selenium.find_element_by_id('id_username')
#         password = self.selenium.find_element_by_id('id_password')
#         submit = self.selenium.find_element_by_xpath('/html/body/div[1]/form/button')
#
#         # Logging in as admin user first
#         username.clear()
#         username.send_keys(self.admin_user.username)
#         password.clear()
#         password.send_keys(self.password)
#         submit.click()
#
#         # Now logout
#         self.selenium.find_element_by_link_text('Log out').click()
#
#         # Logging in as client user now
#         self.selenium.refresh()
#         username.clear()
#         username.send_keys(self.client_user.username)
#         password.clear()
#         password.send_keys(self.password)
#         submit.click()
#
#         # Checking whether we are redirected to profile page of client user
#         assert self.selenium.current_url == f"{self.url}/profile/{self.client_user.pk}/"
