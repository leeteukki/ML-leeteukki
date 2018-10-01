import sqlite3

# sqlite 데이터베이스 연결하기

dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

# 테이블 생성하고 데이터 넣기
cur = conn.cursor()
cur.executescript("""
        /* items 테이블이 있다면 제어*/
        DROP TABLE IF EXISTS item;

        /*테이블 생성하기*/
        CREATE TABLE items(
            item_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            price INTEGER
            );
            
        /* 데이터 넣기*/
        INSERT INTO items(name, price)VALUES('Apple, 800);
        INSERT INTO items(name, price)VALUES('Orange', 780);
        INSERT INTO items(name, price)VALUES('Banana', 430);
        """)

#위의 조작을 데이터베이스에 반영하기
conn.commit()

# 데이터 추출하기
cur = conn.cursor()
cur.execute("SELECT item_id,name,price FROM items")
item_list = cur.detchall()

#출력하기
for it in item_list:
    print(it)
