from selenium import webdriver
import time



class gmailaccount():
    def gmailAcc(self):
        firstname = input('Please enter First Name:\n')
        lastname = input('Please enter Last Name:\n')
        username = input('Please enter username Name:\n')
        password = input('Please enter Password:\n')
        ConfirmPassword = input('Please enter ConfirmPassword:\n')
        baseurl= "http://www.gmail.com/"
        driver= webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(3)



        print("Gmail is opened successfully")
        driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/content/span').click()

        print("Create Account is clicked")

        driver.find_element_by_id("firstName").send_keys(firstname)
        print("Enter  first name")

        driver.find_element_by_id('lastName').send_keys(lastname)
        print("Enter last name")

        driver.find_element_by_id('username').send_keys(username)
        print("Enter user name")

        driver.find_element_by_xpath("//div[@id='passwd']//input[contains(@class, 'whsOnd zHQkBf')]").send_keys(password)
        print("password entered")
        print("Start : %s" % time.ctime())

        print("End : %s" % time.ctime())

        driver.find_element_by_xpath("//div[@id='confirm-passwd']//input[contains(@class, 'whsOnd zHQkBf')]").send_keys(ConfirmPassword)
        print("confirmed password")

        driver.find_element_by_xpath("//*[@id='accountDetailsNext']/content/span").click()
        print("signup checking")

        time.sleep(10)
        try:
            passwordnotmatch = driver.find_element_by_xpath("//div[@class='GQ8Pzc']")
            if passwordnotmatch.is_displayed():
                print("Sign up unsuccessful")
            #else:
             #   print("sign up successful")
        except:
            print("Sign up successful")


ga=gmailaccount()
ga.gmailAcc()


