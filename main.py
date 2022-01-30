import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from send_email.send_email import send_email



def main():
    #load headless chrome driver and get tickets site
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver.exe')
    logging.basicConfig(filename='example.log', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%I:%M:%S %p %m/%d/%Y', level=logging.INFO)

    #try to get page, log and email if it didn't work
    try:
        driver.get("https://www.worldshottesttour.com/")

        #get status of element <a href="#elsalvador" event_label="San Salvador, El Salvador"><span></span>ON SALE SOON</a>
        sv_link = driver.find_elements_by_css_selector('a[event_label="San Salvador, El Salvador"]')
        link = sv_link[0].get_attribute('href')

        if link == "https://www.worldshottesttour.com/#elsalvador":
            logging.info('Aun no esta listo')
        else:
            logging.info('Link listo: {}'.format(link))
            send_email("ya", link)
            logging.info('link enviado')
   
    except:
        logging.error('ERROR cargando')
        send_email("error","")

    driver.close()

if __name__ == "__main__":
    main()