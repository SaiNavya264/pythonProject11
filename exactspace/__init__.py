from browsermobproxy import server
from selenium import webdriver


server = server("path/to/browsermob-proxy")
server.start()
proxy = server.create_proxy()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy.proxy}')
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://exactspace.co/")
proxy.new_har("exactspace")


driver.quit()


har_data = proxy.har
entries = har_data['log']['entries']


status_codes = [entry['response']['status'] for entry in entries]


total_status_code_count = len(status_codes)


status_2xx_count = sum(200 <= code < 300 for code in status_codes)

status_4xx_count = sum(400 <= code < 500 for code in status_codes)


status_5xx_count = sum(500 <= code < 600 for code in status_codes)


print(f"Total status code count: {total_status_code_count}")
print(f"Total count for 2XX status codes: {status_2xx_count}")
print(f"Total count for 4XX status codes: {status_4xx_count}")
print(f"Total count for 5XX status codes: {status_5xx_count}")


server.stop()
