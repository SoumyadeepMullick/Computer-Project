import webbrowser

country="Italy"
html_content= f"<html> <head> {country} </head>   <body> <img src='D:\\Computer project(class-12)\handbag.jpg'> </body> </html>"
with open("index.html","w") as html_file:
    html_file.write(html_content)
    print("Done!")

webbrowser.open_new_tab("index.html")