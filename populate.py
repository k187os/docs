import sqlite3

# Connect to db sqlite3
conn = sqlite3.connect(database="db.sqlite3")
c = conn.cursor()

# open text file "Medic2"

f = open('FMEDIC.TXT', mode='r')
mylist = {}

for line in f:
    drug_cnas = line[:5]
    drug_nom = line[5:55]
    drug_dci = line[55:105]
    drug_dose = line[105:135]
    drug_forme = line[155:176]
    drug_obs = line[266:]
    if drug_nom != "":
        c.execute('INSERT INTO clinic_drug (drug_nom, drug_dci, drug_forme, drug_dose, drug_cnas , drug_obs  )VALUES '
                  '(?, ? , ? , ? , ? , ?)', (drug_nom.strip(), drug_dci.strip(), drug_forme.strip(), drug_dose.strip(

        ), drug_cnas.strip(), drug_obs.strip()) )

conn.commit()
f.close()
for row in c.execute('SELECT * FROM clinic_drug'):
        print (row)

