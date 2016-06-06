## Learning about PostgreSQL

'createdb'
'dropdb'
'psql'

## psql

\dt - list tables

CREATE TABLE example:


'''
CREATE TABLE my_first_table (
       id SERIAL,
       vchar_example VARCHAR(255),
       text_example TEXT,
       bool_example BOOLEAN,
       int_example INTEGER,
       num_example NUMERIC(12,4),
       CONSTRAINT uniq_vchar UNIQUE (vchar_example, bool_example)
       );
'''


ALTER TABLE EXAMPLE 1:

ALTER TABLE my_first_table ALTER COLUMN bool_example SET NOT NULL;

testdb=# INSERT INTO my_first_table (vchar_example, bool_example, int_example) VALUES ('TEST', false, 5);

testdb=# SELECT * FROM my_first_table WHERE bool_example = false AND int_example > 5;


testdb=# CREATE UNIQUE INDEX mft_id_idx ON my_first_table (id);
CREATE INDEX
testdb=# ALTER TABLE my_first_table ADD CONSTRAINT pk_mft_id PRIMARY KEY USING INDEX mft_id_idx;
NOTICE:  ALTER TABLE / ADD CONSTRAINT USING INDEX will rename index "mft_id_idx" to "pk_mft_id"
ALTER TABLE


testdb=# ALTER TABLE fk_example ALTER COLUMN mft_id SET NOT NULL;

testdb=# INSERT INTO fk_example (num_ex, mft_id) VALUES (100, 3);
INSERT 0 1
testdb=# INSERT INTO fk_example (num_ex, mft_id) VALUES (50, 4);
INSERT 0 1


```
SELECT (mft.id,
        mft.vchar_example,
        mft.bool_example,
        mft.int_example,  
        fe.num_ex)
   FROM my_first_table mft, fk_example fe
  WHERE fe.mft_id = mft.id;
```
