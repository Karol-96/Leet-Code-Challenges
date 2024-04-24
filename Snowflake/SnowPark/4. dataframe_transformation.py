from snowflake.snowpark import Session
from snowflake.snowpark.function import col

conncetion_parameters = {
    "account": "<your snowflake account>",
    "user": "<your snowflake user>",
    "password": "<your snowflake password>",
    "role": "<your snowflake role>",  # optional
    "warehouse": "<your snowflake warehouse>",  # optional
    "database": "<your snowflake database>",  # optional
    "schema": "<your snowflake schema>",  # optional
}

session  = Session.builder.configs(conncetion_parameters).create()

df = session.table("sample_sql_table").filter(col("id") == 1)
df.show()

df = session.table("sample_sql_table").select(col("id"),col("name"),col("age"))
df.show()

#Joining dataframes
df_left = session.create_dataframe([["a",1],["b",2],["c",3]],schema=["Key","Value1"])
df_right = session.create_dataframe([["a",4],["b",5],["c",6]],schema=["Key","Value2"])

df_left.join(df_right, df_left.col("Key") == df_right.col("Key")).select(df_left["key"].as_("key"), "value1", "value2").show()
df_left.join(df_right,["Key"]).show()

#Joining exprerssions
df_left.join(df_right,(df_left.col["Key"]== df_right.col["Key"] & df_right["Value"] >= df_left["Value"])).select(df_left["key"].as_("key"), "value1", "value2")

#Self joins
from copy import copy
# Create two DataFrames to join
df_lhs = session.create_dataframe([["a", 1], ["b", 2]], schema=["key", "value1"])
df_rhs = session.create_dataframe([["a", 3], ["b", 4]], schema=["key", "value2"])
df_lhs_copied = copy(df_lhs)
df_self_joined = df_lhs.join(df_lhs_copied, (df_lhs.col("key") == df_lhs_copied.col("key")) & (df_lhs.col("value1") == df_lhs_copied.col("value1")))

#renaming columns while performing Joins
df_lhs.join(df_rhs, df_lhs.col("key") == df_rhs.col("key")).select(df_lhs["key"].alias("key1"), df_rhs["key"].alias("key2"), "value1", "value2").show()



#################################################
#Using Exceptions to catch flaws while operating
from snowflake.snowpark.exceptions import SnowparkJoinException
try:
    df_joined = df.join(df, col("id") == col("parent_id")) # fails
except SnowparkJoinException as e:
    print(e.message)
#You cannot join a DataFrame with itself because the column references cannot be resolved correctly. Instead, create a copy of the DataFrame with copy.copy(), and join the DataFrame with this copy.
# This fails because columns named "id" and "parent_id"
# are in the left and right DataFrames in the join.
try:
    df_joined = df.join(df, df["id"] == df["parent_id"])   # fails
except SnowparkJoinException as e:
    print(e.message)
#So we must perform copy operation while joining


################################################### Collect & Create DataFrame
session.sql("""insert into "10tablename" (id123, "3rdID", "id with space") values ('a', 'b', 'c')""").collect()
# Add return to the statement to return the collect() results in a Python worksheet

