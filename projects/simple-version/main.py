import pandas as pd
import numpy as np
import os
import openpyxl
import sys

import uvicorn
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow
from fastapi import FastAPI

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import threading
import time

 # GLOBAL VARIABLES
# Loop through the items in the directory
df_list = []

fastapi_app = FastAPI()

def run_fastapi():
    uvicorn.run(fastapi_app, host="127.0.0.1", port=8000, log_level="info")

@fastapi_app.get("/")
async def read_root():
    with open("static/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


# Mount the "static" folder to serve static files
fastapi_app.mount("/static", StaticFiles(directory="static"), name="index")

@fastapi_app.get("/process")
async def process():
    # Define the directory path
    directory_path = "C://Users//user//Documents//inputs//"

    # List all files and subdirectories in the specified directory
    items = os.listdir(directory_path)

    '''
    INPUT READER
    '''
    for file_it in items:
        file_path = os.path.join(directory_path, file_it)  # Full path of the item

        # Check if the item is a file
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                df = pd.read_excel(file_path, engine="openpyxl")
                df_list.append(df) # add the newly read-in df to the list

    # save Excel input naming
    # Add your data processing logic here
    processed_data = "Input data has been loaded. You can now decide what to do."
    return {"message": processed_data}


@fastapi_app.get("/execute_option")
async def execute_option(selected_option: str):
    # Define a switch-like dictionary to map options to functions
    options_dict = {
        "option1": function1,
        "option2": function2,
        "option3": function3
    }

    # Execute the corresponding function based on the selected option
    if selected_option in options_dict:
        selected_function = options_dict[selected_option]
        result = selected_function()
        return {"message": result}
    else:
        return {"message": "Option not found"}


def function1():
    return "Executing Function 1"


def function2():
    return "Executing Function 2"


def function3():
    return "Executing Function 3"

def main():
    # Start FastAPI server in a separate thread
    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.start()

    # Wait for a short while for the FastAPI server to start
    time.sleep(2)

    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(100, 200, 300, 300)
    window.setWindowTitle("MainWindow")

    # Create a QWebEngineView to embed the FastAPI HTML content
    web_view = QWebEngineView(window)
    web_view.setGeometry(0, 0, 800, 600)
    window.setCentralWidget(web_view)

    # Load the FastAPI URL in the web view
    web_view.setUrl(QUrl("http://127.0.0.1:8000"))

    window.show() # display window
    sys.exit(app.exec_()) # close the exe program when the window is closed

if __name__ == "__main__":
    main()




