import os
import csv



class CSVFileManager:   
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_FOLDER = os.path.join(BASE_DIR, "data")

    @staticmethod
    def read_csv(filename):

        path = os.path.join(CSVFileManager.DATA_FOLDER,filename)

        if not os.path.exists(path):
            return []
        
        with open(path,"r",newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            return list(reader)  


    @staticmethod
    def append_csv(filename,row):

        os.makedirs(CSVFileManager.DATA_FOLDER, exist_ok=True)

        path = os.path.join(CSVFileManager.DATA_FOLDER, filename)
        with open(path, "a", newline="",encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)

    @staticmethod
    def write_csv(filename, rows):
        
        os.makedirs(CSVFileManager.DATA_FOLDER, exist_ok=True)
        path = os.path.join(CSVFileManager.DATA_FOLDER,filename)
        with open(path,"w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
