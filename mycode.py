#!C:\Users\Personal\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
searchterm =  form.getvalue('searchbox')
print("The searched value is",searchterm)