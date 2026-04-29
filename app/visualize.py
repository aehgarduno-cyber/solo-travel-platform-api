import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

con=psycopg2.connect(
    dbname='travel_blog',
    user='postgres',
    host='pg',        # connec to the DOCKER Pg_container
    port='5432'
)
def sql_to_df(query):
    return pd.read_sql(query, con)

# Post base on the destincation being takenr
query1="""
SELECT d.city, COUNT(*) AS post_count
FROM post_destinations pd
JOIN destinations d ON d.id = pd.destination_id
GROUP BY d.city;
"""

df1=sql_to_df(query1)
df1.plot(kind='bar', x='city', y='post_count', title='Posts by Destination', figsize=(10,5))
plt.show()

# AVG Cost $
query2="""
SELECT d.country, AVG(t.total_cost) AS avg_cost
FROM trips t
JOIN destinations d ON d.id = t.destination_id
GROUP BY d.country;
"""

df2=sql_to_df(query2)
df2.plot(kind='bar', x='country', y='avg_cost', title='Average Trip Cost', figsize=(10,5))
plt.show()