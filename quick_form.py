from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("quick_form"),
    autoescape=select_autoescape()
)

class Field:
    def __init__(self, field_name, validation = None) -> None:
        self.field_name = field_name      
        self.validation = validation

class Input(Field):
    def __init__(self, field_name, validation=None) -> None:
         super().__init__(field_name, validation)      

class Column:
    def __init__(self) -> None:
        self.fields = []
    def add_field(self, field: Field) -> Field:
        if not isinstance(field, Field):
            raise TypeError("must be of type Field!")
        self.fields.append(field)
        return self.fields[-1]
    def __str__(self) -> str:
        return "This is your column"

class Row:
    def __init__(self) -> None:
        self.columns = []
    def add_column(self, column: Column = None) -> Column:
        if not column:
            column = Column()
        else:
            if not isinstance(column, Column):
                raise TypeError("must be of type Column!")
        self.columns.append(column)
        return self.columns[-1]
    def __str__(self) -> str:
            column_count = len(self.columns)
            return f"This row is divided into {column_count} columns"

    
class QuickForm:
    def __init__(self) -> None:
        self.rows = []
    def add_row(self, row: Row = None) -> Row:
        if not row:
             row = Row()
        else:
             if not isinstance(row, Row):
                  raise TypeError("must be of type Row!")
        self.rows.append(row)
        return self.rows[-1]
    def render(self) -> None:
        template = env.get_template("index.html")
        print(template.render(form=self))