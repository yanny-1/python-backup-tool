from pathlib import Path
from datetime import datetime
import json 
import shutil 

with open("tasks.json", encoding="utf-8") as f: 
    plik = json.load(f)["tasks"]

for task in plik: 
    counter = 0
    source = Path(task["source"])
    backup = Path(task["backup"])
    
    if not backup.exists(): 
        backup.mkdir(parents=True)
    else: 
        print(f'{backup} already exists.')
    
    with open("log.txt", "a", encoding="utf-8") as f: 
        if not source.exists():
            print(f'{source} does not exist!')
            x = input("Do you want to create it? yes/no ")
            match x: 
                case "yes":
                    source.mkdir(parents=True)
                case "no": 
                    continue
                case "": 
                    print("You must enter 'yes' or 'no'")
        else: 
            for file in source.rglob("*"): 
                file_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if file.is_file() and file.suffix in task["extensions"]:
                    relative = file.relative_to(source)
                    target = backup / relative 
                    target.parent.mkdir(parents=True, exist_ok=True)
                    if not target.exists() or file.stat().st_mtime > target.stat().st_mtime:
                        shutil.copy(file, target)
                        counter += 1 
                        print(f"Successfully copied {file.name}")
                    else: 
                        print(f'{file.name} was not copied.')
                f.write(f'Date: {file_date} \n Copied {file.name}\n')
            f.write(f'[SUMMARY] - {counter} files were copied. \n\n')
