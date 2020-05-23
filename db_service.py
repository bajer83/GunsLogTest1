import sqlite3
from sqlite3 import Error
from record import Record


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection successful")
    except Error as e:
        print(f"the error '{e}' occured")

    return connection


def execute_query(connection, query, data):  # Used for insert statements
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query executed OK")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query, param=None):  # used for Select statements
    cursor = connection.cursor()
    print(f'Passed parameter : {param}')
    try:
        if param is None:
            cursor.execute(query)
        else:
            cursor.execute(query, param)  # used if additional parameters are used
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def temp():
    add_guns = """
        INSERT INTO
        guns (id, type)
        VALUES
        (1, 'Mini G Gun'),
        (2, 'Mini G Gun'),
        (3, 'Mini G Gun'),
        (4,'Mini G Gun'),
        (5, 'Mini G Gun'),
        (6, 'Mini G Gun'),
        (7, 'Sleeve Gun');
        """

    add_records = """
        INSERT INTO records (gunid, project, gun_total_shots)
        VALUES
        (1, 'Project 1', 0),
        (1, 'Project 2', 100),
        (1, 'Project 3', 200),
        (2, 'Project 1', 0);
        """

    # execute_query(connection, create_guns_table)
    # execute_query(connection, create_records_table)
    # execute_query(connection, add_records)
    # execute_query(connection, add_guns)


def return_records(connection):
    """
    Returns all guns statistics
    :param connection:
    :return: Cursor
    """
    query = """
    select gunid, date_time, gun_total_shots, id from records ORDER BY date_time
        """
    gun_records = execute_read_query(connection, query)

    return gun_records


def return_latest_total_shots_for_gun(connection, gunid):
    """
    Queries database and returns the total_amount of shots for the latest (based on the latest date of entry) for the
    given gund id.
    :param gunid: Gun number
    :return: Integer for total number of shots or 0 if no data found
    """

    cursor = connection.cursor()
    try:
        cursor.execute("select gun_total_shots from records where gunid=:gun_id ORDER BY date_time DESC",
                       {"gun_id": gunid})
        result = cursor.fetchall()
        if not result:  # if no data found
            return 0
        return result[0][0]

    except Error as e:
        print(f"The error '{e}' occurred")


def return_latest_total_shots_for_airlines(connection, gunid):
    cursor = connection.cursor()
    try:
        cursor.execute("select airline_total_shots from records where gunid=:gun_id ORDER BY date_time DESC",
                       {"gun_id": gunid})
        result = cursor.fetchall()
        if not result:
            return 0  # if no data found
        return result[0][0]

    except Error as e:
        print(f"The error '{e}' occurred")


def return_latest_total_shots_for_tbs(connection, gunid):
    cursor = connection.cursor()
    try:
        cursor.execute("select tb_total_shots from records where gunid=:gun_id ORDER BY date_time DESC",
                       {"gun_id": gunid})
        result = cursor.fetchall()
        if not result:
            return 0 # if no data found
        return result[0][0]

    except Error as e:
        print(f"The error '{e}' occurred")


def return_latest_total_shots_for_solenoids(connection, gunid):
    cursor = connection.cursor()
    try:
        cursor.execute("select solenoid_total_shots from records where gunid=:gun_id ORDER BY date_time DESC",
                       {"gun_id": gunid})
        result = cursor.fetchall()
        if not result:
            return 0 # if no data found
        return result[0][0]

    except Error as e:
        print(f"The error '{e}' occurred")


def return_record(connection, record_id: int) -> list:
    """
    Returns all data required for updating information panel
    :param connection:
    :param record_id:
    :return: a record with data
    """
    cursor = connection.cursor()
    try:
        cursor.execute("select id, gunid, date_time, gun_total_shots, airline_total_shots, airline_type,"
                       " tb_total_shots, solenoid_total_shots, project, comments"
                       " from records where id=:record_id",
                       {"record_id": record_id})
        result = cursor.fetchall()
        return result

    except Error as e:
        print(f"The error '{e}' occurred")


def return_previous_id_record_for_this_gun(connection,
                                           this_gun: int):
    cursor = connection.cursor()
    try:
        cursor.execute("select id from records where gunid=:gun_number ORDER BY date_time ASC limit 1",
                       {"gun_number": this_gun})
        result = cursor.fetchall()
        return result

    except Error as e:
        print(f"The error '{e}' occurred")

    return result[0]


def add_new_stats_for_gun(connection, new_data):  # TODO Finish the method for all guns

    for each_gun_new_data in new_data:

        gun_id = each_gun_new_data['gunid']
        print(f'New data for one gun {each_gun_new_data}')
        id_of_previous_record = return_previous_id_record_for_this_gun(connection, gun_id)

        if id_of_previous_record:  # if not empty
            packed_id_tuple = id_of_previous_record[0]  # list of tuples, we only want a single value so have to
            # unpack the tuple
            (unpacked_id,) = packed_id_tuple
            each_gun_new_data['previous_record'] = unpacked_id

        insert_query = """insert into records(gunid, project, gun_total_shots, previous_record, airline_type, date_time,
                            airline_total_shots, tb_total_shots, solenoid_total_shots, comments)
                            VALUES(?,?,?,?,?,?,?,?,?,?)"""

        new_data_list = []  # execute function requires a tuple or a list as dictionary used to be unordered
        for values in each_gun_new_data.values():  # TODO change to a better data structure and remove conversion
            new_data_list.append(values)
        print('List before entry: ', new_data_list)
        execute_query(connection, insert_query, new_data_list)


def return_airline_types(connection):
    """
    Returns a list of airline types
    :param connection: db connection
    :return: a list
    """
    query = "select type from airline_type"
    result = execute_read_query(connection, query)
    return_result = []
    for row in result:
        return_result.append(row[0])  # unpacks values from the tuples
    return return_result
