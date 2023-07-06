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

for x in ListName:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_filelist VALUES (?)", (x,))
            print(x)
conn.close()