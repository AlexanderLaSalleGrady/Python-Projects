import logging

from src.utils.dbconfig import get_connection

logging.basicConfig(filename='bank_member_dao.log', level=logging.INFO)


def create_new_member(member):
    logging.info('New member information passed' + str(member))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("insert into bank_member values(default, ?,?,?,?,?,?,?,?,?,?,?,?)", (member['first_name'],
                                                                                               member['last_name'],
                                                                                               member['dob'],
                                                                                               member['sex'],
                                                                                               member['ssn'],
                                                                                               member['address'],
                                                                                               member['city'],
                                                                                               member['state'],
                                                                                               member['zip'],
                                                                                               member['phone'],
                                                                                               member['email'],
                                                                                               member['bank_member_password']))
        db_connection.commit()
    finally:
        db_connection.close()


def get_all_members():
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from bank_member")
        query_rows = db_cursor.fetchall()
    finally:
        if db_connection:
            db_connection.close()

    return query_rows


def get_member_by_id(bank_member_id):
    logging.info('bank_member_id passed: ' + str(bank_member_id))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from bank_member where bank_member_id = ?", bank_member_id)
        query_rows = db_cursor.fetchall()
    finally:
        if db_connection:
            db_connection.close()

    return query_rows


def get_account_by_id(account_id):
    logging.info('account_id passed: ' + str(account_id))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from bank_account where account_id = ?", account_id)
        query_rows = db_cursor.fetchall()
    finally:
        if db_connection:
            db_connection.close()

    return query_rows


def update_client_information(bank_member_id, first_name):
    logging.info('bank_member_id passed: ' + str(bank_member_id) + ', New first_name passed: ' + str(first_name))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("update bank_member set first_name = ? where bank_member_id = ?", first_name, bank_member_id)
        db_cursor.commit()
    finally:
        if db_connection:
            db_connection.close()

    return bank_member_id


def delete_client_by_id(bank_member_id):
    logging.info('bank_member_id passed: ' + str(bank_member_id))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("delete from bank_member where bank_member_id = ?", bank_member_id)
        db_cursor.commit()
    finally:
        if db_connection:
            db_connection.close()

    return bank_member_id


def create_new_account(bank_member_id, account_t, account_b):
    logging.info('bank_member_id passed: ' + str(bank_member_id) + ', account type passed: ' + str(account_t) + ', account balance passed: ' + str(account_b))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("insert into bank_account values(default, ?,?,?)", (bank_member_id, account_t, account_b))

        db_connection.commit()
    finally:
        db_connection.close()


def get_accounts_by_client_id(bank_member_id):
    logging.info('bank_member_id passed: ' + str(bank_member_id))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select bank_member_id, bank_account.account_id, bank_account.account_type, "
                          "bank_account.account_balance from bank_account where bank_member_id = ?", bank_member_id)
        query_rows = db_cursor.fetchall()
    finally:
        if db_connection:
            db_connection.close()

    return query_rows


def get_single_account_by_client_id(bank_member_id, account_id):
    logging.info('bank_member_id passed: ' + str(bank_member_id) + ', account_id passed: ' + str(account_id))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select bank_member_id, bank_account.account_id, bank_account.account_type, "
                          "bank_account.account_balance from bank_account where bank_member_id = ? and account_id = "
                          "?", bank_member_id, account_id)
        query_rows = db_cursor.fetchone()
    finally:
        if db_connection:
            db_connection.close()

    return query_rows


def update_account_type_by_client_id(bank_member_id, account_id, account_type):
    logging.info('bank_member_id passed: ' + str(bank_member_id) + ', account_id passed: ' + str(account_id) + ', new account type passed: ' + str(account_type))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("update bank_account set account_type = ? where bank_member_id = ? and account_id = ?", account_type, bank_member_id, account_id)
        db_cursor.commit()
    finally:
        if db_connection:
            db_connection.close()

    return bank_member_id, account_id


def delete_account_by_client_id(bank_member_id, account_id):
    logging.info('bank_member_id passed: ' + str(bank_member_id) + ', account_id passed: ' + str(account_id))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("delete from bank_account where account_id = ? and bank_member_id = ?", account_id, bank_member_id)
        db_cursor.commit()
    finally:
        if db_connection:
            db_connection.close()

    return bank_member_id, account_id


def get_balance_from_account_by_account_id(account_id):
    logging.info('account_id passed: ' + str(account_id))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select account_balance from bank_account where account_id = ?", account_id)
        query_rows = db_cursor.fetchone()
    finally:
        if db_connection:
            db_connection.close()

    return query_rows


def update_account_balance_by_account_id(account_id, new_balance):
    logging.info('account_id passed: ' + str(account_id) + ', new account balance passed: ' + str(new_balance))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("update bank_account set account_balance = ? where account_id = ?", new_balance, account_id)
        db_cursor.commit()
    finally:
        if db_connection:
            db_connection.close()

    return new_balance


def get_account_between_values(bank_member_id, greaterThan, lessThan):
    logging.info('bank_member_id passed: ' + str(bank_member_id) + ', greaterThan value passed: ' + str(
        greaterThan) + ', lessThan value passed: ' + str(lessThan))
    db_connection = ''
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select bank_member_id, bank_account.account_id, bank_account.account_type, "
                          "bank_account.account_balance from bank_account where bank_member_id = ? and "
                          "account_balance <= ? and account_balance >= ?",bank_member_id, greaterThan, lessThan)
        query_rows = db_cursor.fetchall()
    finally:
        if db_connection:
            db_connection.close()

    return query_rows
