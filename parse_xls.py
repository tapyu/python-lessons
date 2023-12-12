import xlrd, xlwt
from .config import *
import os

def fix_excel(file_path):
    new_workbook = xlwt.Workbook()
    try:
        # Open the Excel workbook
        workbook = xlrd.open_workbook(file_path)

        # Select the first worksheet (index 0)
        worksheet = workbook.sheet_by_index(0)

        # create a new worksheet
        new_worksheet = new_workbook.add_sheet(worksheet.name)

        # Read data from each cell in the sheet
        new_row = 0
        for row in range(worksheet.nrows):
            if {cell.ctype for cell in worksheet.row(row)} == {0}:
                continue
            for col, cell in enumerate(worksheet.row(row)):
                new_worksheet.write(new_row, col, cell.value)
            new_row += 1
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
    except xlrd.XLRDError as e:
        logging.error("Error reading Excel file: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
    
    base_name, extension = os.path.splitext(file_path)
    new_workbook.save(f"{base_name}_corrigido{extension}")