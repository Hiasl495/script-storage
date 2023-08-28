import pandas as pd
import numpy as np
import os
import openpyxl
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage   # Import QWebEngineView from PyQtWebEngineWidgets
from PyQt5.QtCore import QUrl
from fastapi import FastAPI
import uvicorn
import threading
import time

app = FastAPI() # create fast api app instance

class BrowserWindow(QMainWindow):
    def __init__(self, html_path):
        super().__init__()
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # Create a QUrl object from the HTML file path
        html_url = QUrl.fromLocalFile(html_path)
        self.browser.setUrl(html_url)
def run_fastapi():
    app = FastAPI()

    #@app.get("/")
    #async def read_root():
    #    return {"message": "Welcome to the FastAPI Desktop App"}

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

if __name__ == "__main__":
    # Start FastAPI server in a separate thread
    fastapi_thread = threading.Thread(target=run_fastapi) # run function for uvicorn server
    fastapi_thread.start()

    # Wait for a short while for the FastAPI server to start
    time.sleep(2)

    # Construct the file path to predefined-html.html
    script_directory = os.path.dirname(os.path.abspath(__file__))
    predefined_html_path = os.path.join(script_directory, "predefined-html.html")
    print("After html declaration")

    # Initialize the GUI after FastAPI server starts
    app_qt = QApplication(sys.argv)
    window = BrowserWindow(predefined_html_path)
    window.show()
    sys.exit(app_qt.exec_())


def working_app():
    # Define the directory path
    directory_path = "C://Users//user//Documents//inputs//"

    # List all files and subdirectories in the specified directory
    items = os.listdir(directory_path)

    '''
    INPUT READER
    '''
    # Loop through the items in the directory
    for file_it in items:
        file_path = os.path.join(directory_path, file_it)  # Full path of the item

        # Check if the item is a file
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                df = pd.read_excel(file_path, engine="openpyxl")
                print(df)

                # save Excel input naming

    '''
    MAIN FUNCTIONALITY
    '''

    '''
    OUTPUTTER
    '''
    return 0


