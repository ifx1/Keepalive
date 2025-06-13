from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import schedule

# 替换为你的 Streamlit 应用 URL
APP_URL = "https://your-streamlit-app-url.streamlit.app"

def keep_alive():
    try:
        # 配置无头浏览器选项
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # 无头模式
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")  # 禁用 GPU 加速（某些环境下需要）

        # 初始化 WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        # 访问应用 URL
        driver.get(APP_URL)
        print(f"Visited {APP_URL} at {time.ctime()}")
        
        # 等待页面加载（可选，根据需要调整）
        time.sleep(5)
        
        # 关闭浏览器
        driver.quit()
    except Exception as e:
        print(f"Error: {e}")

# 定时任务，每 10 分钟访问一次
schedule.every(10).minutes.do(keep_alive)

# 主循环
while True:
    schedule.run_pending()
    time.sleep(1)
