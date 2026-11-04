from sqlalchemy import Connection, text

def transfer_funds(
        conn: Connection,
        from_id: int,
        to_id: int,
        amount: int,
        ) -> None:
    '''
    This function assumes that the following table exists

    CREATE TABLE accounts (
        id INT PRIMARY KEY,
        balance INT NOT NULL
    );
    '''
    with conn.begin():
        conn.execute(
            text("UPDATE accounts SET balance = balance - :amount WHERE id = :id"),
            {"amount": amount, "id": from_id}
        )
        conn.execute(
            text("UPDATE accounts SET balance = balance + :amount WHERE id = :id"),
            {"amount": amount, "id": to_id}
        )
