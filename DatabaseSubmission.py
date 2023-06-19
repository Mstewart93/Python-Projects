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


with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_filelist(file_name) VALUES(?)", \
                ('information.docx')
                )
    cur.execute("INSERT INTO tbl_filelist(file_name) VALUES(?)", \
                ('Hello.txt')
                )
    cur.execute("INSERT INTO tbl_filelist(file_name) VALUES(?)", \
                ('myImage.png')
                )
    cur.execute("INSERT INTO tbl_filelist(file_name) VALUES(?)", \
                ('myMovie.mpg')
                )
    cur.execute("INSERT INTO tbl_filelist(file_name) VALUES(?)", \
                ('World.txt')
                )
    cur.execute("INSERT INTO tbl_filelist(file_name) VALUES(?)", \
                ('data.pdf')
                )
    cur.execute("INSERT INTO tbl_filelist(file_name) VALUES(?)", \
                ('myPhoto.jpg')
                )
    conn.commit
conn.close

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_filelist WHERE field LIKE %.txt")
    conn.commit
conn.close