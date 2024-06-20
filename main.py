import openpyxl
import datetime

# Create and save the workbook if it doesn't exist
wb_path = "C:\\Programming\\Attendance\\Attendance.xlsx"
try:
    wb_attendance = openpyxl.load_workbook(wb_path)
except FileNotFoundError:
    wb_attendance = openpyxl.Workbook()
    wb_attendance.save(wb_path)
    wb_attendance.close()

# Load source and destination workbooks
wb_source = openpyxl.load_workbook('C:\\Programming\\Attendance\\Datasheet.xlsx')
wb_attendance = openpyxl.load_workbook(wb_path)

# Generate new sheet for every new day
today = datetime.datetime.now().strftime("%d-%m-%y")
new_sheet = wb_attendance.create_sheet(today)

# Capture total names and details (assuming data starts from row 1)
source_sheet = wb_source['Data']
total_names = source_sheet.max_column
total_details = source_sheet.max_row

# Copy names to new sheet (first column)
for row in range(1, total_details + 1):
    source_cell = source_sheet.cell(row=row, column=1)
    dest_cell = new_sheet.cell(row=row, column=1)
    dest_cell.value = source_cell.value

# Ensure the 'Data' sheet exists in the attendance workbook
if 'Data' not in wb_attendance.sheetnames:
    wb_attendance.create_sheet(index=0, title='Data')

# Copy entire source sheet to the 'Data' sheet in the attendance workbook
for row in range(1, total_details + 1):
    for col in range(1, total_names + 1):
        source_cell = source_sheet.cell(row=row, column=col)
        dest_cell = wb_attendance['Data'].cell(row=row, column=col)
        dest_cell.value = source_cell.value

# Save the attendance workbook
wb_attendance.save(wb_path)
