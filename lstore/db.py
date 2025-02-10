from lstore.table import Table
from lstore.index import Index

class Database():

    def __init__(self):
        self.tables = []
        pass

    # Not required for milestone1
    def open(self, path):
        pass

    def close(self):
        pass

    """
    # Creates a new table
    :param name: string         #Table name
    :param num_columns: int     #Number of Columns: all columns are integer
    :param key: int             #Index of table key in columns
    """
    def create_table(self, name, num_columns, key_index):
        #Check for dupe table
        for table in self.tables:
            if table.name == name:
                raise Exception(f"Table {name} already exists")
    
        table = Table(name, num_columns, key_index)
        self.tables.append(table)

        for i in range (0, num_columns):
            table.index.create_index(i)

        return table

    
    """
    # Deletes the specified table
    """
    def drop_table(self, name):
        for i, table in enumerate(self.tables):
            if table.name == name:
                #Drop all indices for specified table
                for col in range(table.num_columns):
                    table.index.drop_index(col)
                
                #Then remove table
                self.tables.pop(i)
                return
        
        raise Exception(f"Table {name} does not exist")

    
    """
    # Returns table with the passed name
    """
    def get_table(self, name):

        for table in self.tables:
            if table.name == name:
                return table
        
        raise Exception(f"Table {name} does not exist")
