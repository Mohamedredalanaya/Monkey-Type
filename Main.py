from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service=Service(ChromeDriverManager().install())
drive=webdriver.Chrome(service=service)

drive.get("https://monkeytype.com/")
print("After you choice about the cookies")
input("Hit enter to start!\n")

while True:
    try:
        drive.find_element(By.ID,"wordsInput")
        words=drive.find_element(By.CSS_SELECTOR,"div[class='word active']").text    
        single_word=[]
        for i in words:
            if i!="\n":
                single_word.append(i)
            
        single_word="".join(single_word)
        # print(f"The word is : {single_word}")
        
        drive.find_element(By.ID,"wordsInput").send_keys(single_word)
        drive.find_element(By.ID,"wordsInput").send_keys(" ")
    except:
        break
    

input("hit enter to exit")