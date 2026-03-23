import re

with open(r"c:\Users\Pranjal Guleria\PORTFOLIO\index.html", "r", encoding="utf-8") as f:
    text = f.read()

# project 1 2 3
p1_start = text.find("<!-- Project 1 -->")
p4_start = text.find("<!-- Project 4 -->")
end_projects = text.find('            </div>', p4_start)

if p1_start != -1 and p4_start != -1 and end_projects != -1:
    p1_3 = text[p1_start:p4_start]
    p4_6 = text[p4_start:end_projects]

    old_projects_content = p1_3 + p4_6

    # adjust projects 4, 5, 6 UI for link wrapping (inside p4_6)
    p4_6 = p4_6.replace(
        '<div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">',
        '<div style="display: flex; gap: 0.5rem;">'
    )

    # We want these buttons to take up 50% width each and have center alignment
    # To do this safely, we will replace the 'class="btn btn-outline"' inside p4_6
    
    # We update the 'btn-outline' class to add inline styling for equal flex.
    p4_6 = p4_6.replace(
        'class="btn btn-outline"',
        'class="btn btn-outline" style="flex: 1; padding-left: 0; padding-right: 0; text-align: center; justify-content: center; font-size: 0.85rem;"'
    )

    new_projects_content = p4_6 + p1_3
    new_text = text.replace(old_projects_content, new_projects_content)

    with open(r"c:\Users\Pranjal Guleria\PORTFOLIO\index.html", "w", encoding="utf-8") as f:
        f.write(new_text)
    
    print("Successfully updated index.html")
else:
    print("Could not find blocks.")
