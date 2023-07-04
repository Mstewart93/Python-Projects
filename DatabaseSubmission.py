import sqlite3

#connect to database
conn = sqlite3.connect('file.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filelist( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    file_name\
        )")
    conn.commit()
conn.close

ListName = ["information.docx", "Hello.txt", "myImage.png", \
         "myMovie.mpg", "World.txt", "data.pdf", "myPhoto.jpg"]

txtList = []
def query_string ():
    for (let i = 0; i <= listName.length; i++) {
    x = txt.find("*.txt")
    txtList.append(x)
    } 


with conn:
    cur = conn.cursor()
    cur.execute(query_string)
    conn.commit
conn.close