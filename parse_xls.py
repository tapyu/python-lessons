import xlrd

def read_excel(file_path):
    try:
        # Open the Excel workbook
        workbook = xlrd.open_workbook(file_path)

        # Select the first sheet (index 0)
        sheet = workbook.sheet_by_index(0)

        # Get the number of rows and columns in the sheet
        num_rows = sheet.nrows
        num_cols = sheet.ncols

        # Read data from each cell in the sheet
        for row_index in range(num_rows):
            row_data = []
            for col_index in range(num_cols):
                cell_value = sheet.cell_value(row_index, col_index)
                row_data.append(cell_value)
            print(row_data)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except xlrd.XLRDError as e:
        print(f"Error reading Excel file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")