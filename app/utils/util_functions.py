import os


def extract_column_names(sql_file: str) -> dict:
    """Extract column names from SQL file"""
    column_names = {}  # {table_name: [column_names]}
    lines = []
    with open(sql_file) as f:
        lines = f.readlines()
        # remove tabs for each line
        lines = [line.replace("\t", "") for line in lines]
        lines = [line.replace("\n", "") for line in lines]
        lines = [line.replace(",", "") for line in lines]
        lines = [line.strip() for line in lines]

        # remove empty lines
        lines = [line for line in lines if line.strip()]

        # remove line starting with conditions
        sql_keywords = [
            "WHERE",
            "GROUP BY",
            "HAVING",
            "ORDER BY",
            "LIMIT",
            "OFFSET",
            "FOREIGN",
            "PRIMARY",
            "DO",
            "ALTER",
            "DROP",
            "ADD",
            "INSERT",
            "UPDATE",
            "DELETE",
            "SELECT",
            "FROM",
            "INNER",
            "LEFT",
            "RIGHT",
            "OUTER",
            "JOIN",
            "ON",
            "AS",
            "AND",
            "OR",
            "NOT",
            "IS",
            "NULL",
            "UNIQUE",
            "INDEX",
            "KEY",
            "REFERENCES",
            "DEFAULT",
            "CHECK",
            "CONSTRAINT",
            "VIEW",
            "DATABASE",
            "IF",
            "EXISTS",
            "CASCADE",
            "RESTRICT",
            "BEGIN",
            "CREATE TYPE",
            "END",
        ]

        conditions = [
            *sql_keywords,
            # ")",
            "(",
            "--",
            "'",
        ]

        lines = [line for line in lines if not line.startswith(tuple(conditions))]

        print(lines)

    table_names = [
        line.replace("CREATE TABLE", "")
        .replace("(", "")
        .replace("IF NOT EXISTS", "")
        .strip()
        for line in lines
        if line.startswith("CREATE TABLE")
    ]

    for table_name in table_names:
        column_names[table_name] = []
        is_table = False
        for line in lines:
            if line.startswith(f"CREATE TABLE {table_name}") or line.startswith(
                f"CREATE TABLE IF NOT EXISTS {table_name}"
            ):
                is_table = True
                continue

            if line.startswith(")"):
                is_table = False
                continue

            if is_table:
                line = line.replace("INT", "")
                line = line.replace("CHAR", "")
                line = line.replace("VARCHAR", "")
                line = line.replace("VAR", "")
                line = line.replace("VARCHAR", "")
                line = line.replace("TEXT", "")
                line = line.replace("FLOAT", "")
                line = line.replace("DOUBLE", "")
                line = line.replace("DATE", "")
                line = line.replace("DATETIME", "")
                line = line.replace("BOOLEAN", "")
                line = line.replace("AUTO_INCREMENT", "")
                line = line.replace("PRIMARY KEY", "")
                line = line.replace("NOT NULL", "")
                line = line.replace("DEFAULT", "")
                line = line.replace("COMMENT", "")
                line = line.replace("REFERENCES", "")
                line = line.replace("ON DELETE CASCADE", "")
                line = line.replace("ON UPDATE CASCADE", "")
                line = line.replace("ON DELETE SET NULL", "")
                line = line.replace("ON UPDATE SET NULL", "")
                line = line.replace("ON DELETE NO ACTION", "")

                # remove numbers
                line = "".join([i for i in line if not i.isdigit()])
                line = line.replace("()", " ")
                line = line.strip()

                column_names[table_name].append(line)

    print("Keys:", column_names.keys())
    print("Values:", list(column_names.values())[2])


if __name__ == "__main__":
    sql_file = os.path.join(os.getcwd(), "app/database/init.sql")
    extract_column_names(sql_file)
