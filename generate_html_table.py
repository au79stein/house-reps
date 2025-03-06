#!/usr/bin/env python3

import sys

# Read input from stdin
data = sys.stdin.read().strip()

# Split into lines
lines = data.split("\n")

# Extract column headers and rows
headers = [h.strip() for h in lines[0].split("  ") if h]
rows = [list(filter(None, line.split("  "))) for line in lines[2:]]

# Generate HTML table with inline CSS for styling
html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;  /* Add font-size to table */
        }
        th, td {
            padding: 8px;
            text-align: left;
            border: 1px solid #ddd;
            font-size: 14px;  /* Add font-size to table cells */
        }
        .blue {
            color: blue;
        }
        .red {
            color: red;
        }
    </style>
</head>
<body>
  <h1>Members of the 119th House of Representatives</h>
    <table>
        <tr>
            """ + "".join(f"<th>{h}</th>" for h in headers) + """
        </tr>
"""

# Add rows to table
for row in rows:
    html += "<tr>"
    for i, cell in enumerate(row):
        if i == 2 and cell.strip() == 'R':  # Check if it's the Party column (index 2) and value is 'R'
            html += f"<td class='red'>{cell.strip()}</td>"
        elif i == 2 and cell.strip() == 'D':  # Check if it's the Party column (index 2) and value is 'R'
            html += f"<td class='blue'>{cell.strip()}</td>"
        else:
            html += f"<td class>{cell.strip()}</td>"
    html += "</tr>\n"

html += """
    </table>
</body>
</html>
"""

# Output the HTML
print(html)

