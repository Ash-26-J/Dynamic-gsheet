import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
]
credentials = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(credentials)
sheet_id = "1f5fuKB8qIzpJML16KDwzGs9Q-REvbxhivdakwKBpFkw"
workbook = client.open_by_key(sheet_id)

# Specify the title of the worksheet you want to access
worksheet_title = "Sheet2"  # Replace with the actual worksheet name
sheet = workbook.worksheet(worksheet_title)  # Use the correct variable

sheet.update_cell(2, 1, "ashish")  # Update a cell with a value
sheet.update_cell(2, 2, "01jst") 
sheet.update_cell(2, 3, "100")  
sheet.sort((1, 'asc')) 
value = sheet.cell(2, 1).value

values =[
    ["Name","price","quaty"],
     ["basket","100","1"],
    ["cricket","10","5"],
    ["bat","200","2"],
    ["ball","50","3"],
    ["glove","20","4"],
    ["stump","30","5"],
    ["wicket","40","6"],
    ["helmet","60","7"],
    ["pads","80","8"],
    ["batting gloves","90","9"],
    ["keeping gloves","110","10"]
    ]
worksheet_list = map(lambda x: x.title, workbook.worksheets())  # Get the list of all worksheets in the workbook    
new_worksheet_name = "sheet3"
if new_worksheet_name not in worksheet_list:  # Check if the new worksheet name already exists
    sheet = workbook.add_worksheet(title=new_worksheet_name, rows="100", cols="20")
else:  # Add the missing colon here
    sheet = workbook.worksheet(new_worksheet_name)  # Access the existing worksheet

# Update the worksheet with the values
sheet.update(f"A1:C{len(values)}", values)
sheet.format("A1:C1", {"textFormat": {"bold": True}})  # Make the header bold
sheet.sort((1, 'asc'))
print(value)  # Print the value of the cell
print(sheet.title)  # Print the title of the worksheet
