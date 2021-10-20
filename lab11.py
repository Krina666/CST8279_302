import sqlite3
import base64
import webbrowser

n = input("Please enter the number between 1 and 24 or enter q to exit： ")
#print(type(n))
yes = True
while yes:
    if n.isnumeric(): #if number
        n = int(n)
        if 0 < n < 25:#if input is 1-24
            yes = False

            #print(n)
        else: #else ask input again
            n = input("Please enter the number between 1 and 24 or enter q to exit： ")

    else:
        if n == "q":
            exit()
        else:
            n = input("Please enter the number between 1 and 24 or enter q to exit： ")

conn = sqlite3.connect('week11.db')
c = conn.cursor()
c.execute('select Link from Lab10 where id=%d' % n)
link = str(c.fetchone()[0])
print(link)

base64_message = link
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

webbrowser.open_new(message)

city_name = input("Please enter the name of the city：")
country_name = input("Please enter the name of the country：")
'''listToPass = [city_name, country_name]
c.executemany('update Lab10 set City=? and Country=? where id=4', listToPass)
c.executemany('update Lab10 set City=? and Country=? where id=?', ((city_name,), (country_name,), (n,)))'''
c.execute('Update Lab10 set City=%s and Country=%s where id=?', (city_name, country_name, n))
conn.commit()
c.close()
conn.close()
