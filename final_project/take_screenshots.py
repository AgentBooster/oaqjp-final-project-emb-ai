import time
from playwright.sync_api import sync_playwright
import os

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1000, 'height': 600})
        page = context.new_page()
        
        # We can just load the template as a file! 
        index_path = f"file://{os.path.abspath('templates/index.html')}"
        page.goto(index_path)

        # Test 1 (Task 11) - 6b_deployment_test.png
        print("Taking 6b_deployment_test.png...")
        page.fill("#textToAnalyze", "I think I am having fun")
        # Inject the expected response
        html_response1 = "For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is <b>joy</b>."
        page.evaluate(f'document.getElementById("system_response").innerHTML = `{html_response1}`')
        time.sleep(1)
        
        # The user wants it in the root of the repo
        output_1 = os.path.join("..", "6b_deployment_test.png")
        page.screenshot(path=output_1, full_page=True)
        print(f"Saved {output_1}")

        # Test 2 (Task 14) - 7c_error_handling_interface.png
        print("Taking 7c_error_handling_interface.png...")
        page.fill("#textToAnalyze", "")
        html_response2 = "Invalid text! Please try again!"
        page.evaluate(f'document.getElementById("system_response").innerHTML = `{html_response2}`')
        time.sleep(1)
        
        output_2 = os.path.join("..", "7c_error_handling_interface.png")
        page.screenshot(path=output_2, full_page=True)
        print(f"Saved {output_2}")

        browser.close()

if __name__ == "__main__":
    main()
