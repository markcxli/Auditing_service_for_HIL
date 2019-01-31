import time
import datetime
import sqlite3
import os
import subprocess


last_list_node_info = {}

conn = sqlite3.connect('HIL_updates.db')
c=conn.cursor()
#c.execute('CREATE TABLE IF NOT EXISTS recent_updates(m_time TEXT , node TEXT,  switch, TEXT)')
c.execute('INSERT INTO recent_updates (m_time, node, switch) VALUES (?, ?, ?)', ('1', '2','3' ))
c.execute('SELECT m_time,node,switch FROM recent_updates')
result=c.fetchall()
for row in result:
	output = " ".join(row)
	print output

print(output)
conn.commit()
conn.close()
