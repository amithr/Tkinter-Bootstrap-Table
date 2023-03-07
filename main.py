import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

app = ttk.Window(themename="superhero")
colors = app.style.colors

coldata = [
    {"text": "LicenseNumber", "stretch": False},
    "CompanyName",
    {"text": "UserCount", "stretch": False},
]

rowdata = [
    ('A123', 'IzzyCo', 12),
    ('A136', 'Kimdee Inc.', 45),
    ('A158', 'Farmadding Co.', 36)
]
table = Tableview(
    master=app,
    coldata=coldata,
    rowdata=rowdata,
    paginated=True,
    pagesize=10, # Number of rows to show per page
    autofit=False, # Whether or not to automatically change the size of a column based on the existing data
    searchable=True,
    bootstyle=PRIMARY,
    stripecolor=(colors.light, None), # background, foreground


)

table.pack(fill=BOTH, expand=YES, padx=10, pady=10)

app.mainloop()