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
            font-size: 14px;  /* Table font size */
        }
        th, td {
            padding: 8px;
            text-align: left;
            border: 1px solid #ddd;
        }
        .red-row {
            background-color: #f8d7da;  /* Light red background for 'R' Party */
        }
        .blue-row {
            background-color: #cce5ff;  /* Light blue background for 'D' Party */
        }
        .red {
            color: red;  /* Red text color for 'R' in Party column */
        }
        .blue {
            color: blue;  /* Blue text color for 'D' in Party column */
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
    if row[2].strip() == 'R':  # Check if it's the Party column (index 2) and value is 'R'
        html += "<tr class='red-row'>"  # Apply 'red-row' class to the entire row
    elif row[2].strip() == 'D':  # Check if it's the Party column and value is 'D'
        html += "<tr class='blue-row'>"  # Apply 'blue-row' class to the entire row
    else:
        html += "<tr>"

    for i, cell in enumerate(row):
        if i == 2 and cell.strip() == 'R':  # Check if it's the Party column and value is 'R'
            html += f"<td class='red'>{cell.strip()}</td>"  # Color 'R' red
        elif i == 2 and cell.strip() == 'D':  # Check if it's the Party column and value is 'D'
            html += f"<td class='blue'>{cell.strip()}</td>"  # Color 'D' blue
        else:
            html += f"<td>{cell.strip()}</td>"

    html += "</tr>\n"

html += """
    </table>
</body>
</html>
"""
# Output the HTML
print(html)

