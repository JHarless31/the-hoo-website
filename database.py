from sqlalchemy import create_engine, text

db_conn_str = "mysql+pymysql://lilctga62bk09z3ipajt:pscale_pw_R1d9qUNhmLEN0aNvNNdNOgCWmZ4q2m6D0MxsCcJX9Lt@us-west.connect.psdb.cloud/thehoo?charset=utf8mb4"

engine = create_engine(db_conn_str, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})

with engine.connect() as conn:
  result = conn.execute(text("select * from actions"))
  print("type(result): ", type(result))
  result_all = result.all()
  print("type(result.all()): ", type(result_all))
  first_result = result_all[0]
  print("First result: ", first_result)
  print("First result type: ", type(first_result))
  first_result_dict = dict(result_all[0])
  print("first_result_dict type: ", type(first_result_dict))
  print(first_result_dict)