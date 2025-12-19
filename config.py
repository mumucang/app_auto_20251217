import os.path

project_path = os.path.dirname(os.path.abspath(__file__))
datas_path = os.path.join(project_path, 'datas')
logs_path = os.path.join(project_path, 'logs')
pictures_path = os.path.join(project_path, 'pictures')
reports_path = os.path.join(project_path, 'reports')

platformName = "Android" #ios
appium_server_url = "http://localhost:4723/wd/hub"





if __name__ == '__main__':
    print(project_path)
    print(datas_path)