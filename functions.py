import json

FILEPATH = "todos.txt"
SETTINGSPATH = "settings.json"

def get_todos(filepath=FILEPATH):
    try:
        with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
        return todos_local
    except FileNotFoundError:
        with open("todos.txt", "w") as new_file:
            print("Error, todos.txt not found. New file created")
        with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def get_settings(settingspath=SETTINGSPATH):
    try:
        with open(settingspath, "r") as file_local:
            settings_local = json.load(file_local)
        return settings_local
    except FileNotFoundError:
        with open("settings.json","w") as new_file:
            default_settings = {"setting_top_bottom": 1,}
            new_file.write(json.dumps(default_settings, indent=4))
            print("Error, settings.json not found. New file created")
        with open(settingspath, "r") as file_local:
            settings_local = json.load(file_local)
        return settings_local

def write_settings(settings_arg, settingspath=SETTINGSPATH):
    settings_json = json.dumps(settings_arg, indent=4)
    with open(settingspath, "w") as settings:
        settings.write(settings_json)

if __name__ == "__main__":
    get_settings()
