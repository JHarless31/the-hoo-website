from sqlalchemy import create_engine, text

#save the database connection string as a variable
db_conn_str = "mysql+pymysql://lilctga62bk09z3ipajt:pscale_pw_R1d9qUNhmLEN0aNvNNdNOgCWmZ4q2m6D0MxsCcJX9Lt@us-west.connect.psdb.cloud/thehoo?charset=utf8mb4"

#creating an database engine using db_conn_str inside of a variable
engine = create_engine(db_conn_str,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def load_actions_from_db():
  #use the database engine to open a connection inside the variable "conn" to the database and query the database; save the results in the variable "result"
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM actions"))
  #create a list of dictionaries; each dictionary is a row in the "actions" table
    actions = []
    for row in result.all():
      actions.append(row._asdict())
    return actions