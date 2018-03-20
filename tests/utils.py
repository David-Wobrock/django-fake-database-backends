import copy
import itertools
import re

def order_insert_statements(sql_statements):
    """Orders alphabetically the fields/columns of the insert statement
    Does not work for 'INSERT INTO * ...' 
    """
    sql_statements = list(sql_statements)
    ordered_insert_statements = copy.deepcopy(sql_statements)

    for idx, statement in enumerate(sql_statements):
        if is_sql_insert_statement(statement):
            ordered_insert_statements[idx] = order_insert_statement(
                statement)

    return ordered_insert_statements


def is_sql_insert_statement(sql_statement):
    return sql_statement.startswith('INSERT INTO')


def order_insert_statement(insert_statement):
    """Orders the field of an sql insert into statement 
    in alphabetical order
    """
    columns_values_dict = parse_insert_statement(insert_statement)

    ordered_columns = sorted(columns_values_dict.keys())
    return _replace_insert_order(
        insert_statement,
        ordered_columns,
        columns_values_dict)


def parse_insert_statement(insert_statement):
    """Return a dict with the columns of the insert statement as keys
    and the values of the statement as values
    """
    # Get columns
    match = re.search(r'^INSERT INTO ".*" \(([^)]+)\)', insert_statement)
    columns = [x.strip() for x in match.group(1).split(',')]

    # Get values
    if is_insert_values(insert_statement):
        match = re.match(r'^INSERT INTO .* VALUES \((.*)\)', insert_statement)
    else:  # insert select
        match = re.match(r'^INSERT INTO .* SELECT (.*) FROM', insert_statement)
    values = [x.strip() for x in match.group(1).split(',')]

    return dict(zip(columns, values))


def is_insert_values(insert_statement):
    return re.match('INSERT INTO .* VALUES', insert_statement) is not None


def _replace_insert_order(initial_statement, new_order, values_dict):
    replacement_columns = ', '.join(new_order)
    replacement_values = ', '.join([values_dict[col] for col in new_order])

    columns_replaced_statement = re.sub(
        r'(INSERT INTO ".*") \(.*\) ([VALUES|SELECT].*)',
        r'\g<1> ({0}) \g<2>'.format(replacement_columns),
        initial_statement)

    if is_insert_values(initial_statement):
        replaced_statement = re.sub(
            r'(INSERT INTO .* VALUES) .*',
            r'\g<1> ({0});'.format(replacement_values),
            columns_replaced_statement)
    else:  # insert select
        replaced_statement = re.sub(
            r'(INSERT INTO .* SELECT) .* (FROM .*)',
            r'\g<1> {0} \g<2>'.format(replacement_values),
            columns_replaced_statement)
    return replaced_statement
