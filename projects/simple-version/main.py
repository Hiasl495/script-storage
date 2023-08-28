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




