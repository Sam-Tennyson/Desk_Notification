import time
import pandas as pd
from plyer import notification

if __name__ == "__main__":
    pth = r"E:\Saurabh_Shukla_Project\DesktopNotification\vocab.xlsx"
    file_name = pd.read_excel(pth)

    print("Program is running")
    print("Press Ctrl+C to stop the code :)")
    while True:
        for e in range(len(file_name)):
            notification.notify(
                title= "Vocabulary",
                message = f"{file_name.iloc[e]}",
                app_icon= "E:\Saurabh_Shukla_Project\DesktopNotification\diction.ico",
                timeout = 2
            )
            time.sleep(60*60)
