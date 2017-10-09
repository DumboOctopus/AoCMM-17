import data_cruncher, sqlite3
from aocmm_functions import insert_probabilities
conn = sqlite3.connect("data.db")
c = conn.cursor()

# Destroy all probabilities including congloms
c.execute("DELETE FROM probabilities")
#remove all congloms:
c.execute("DELETE FROM persons_data where is_conglom=1")

c.execute("SELECT person, text_id, typing_data from persons_data")
persons_data = c.fetchall()

for person, text_id, typing_data in persons_data:
    occurrences, totals, probabilities = data_cruncher.calculate(typing_data, None, None)
    probabilities_id = insert_probabilities(probabilities, c)
    c.execute("UPDATE persons_date SET probabilities_id={} where person = '{}' and text_id={}".format(probabilities_id, person, text_id))
