import webbrowser
import os
from jinja2 import Environment, PackageLoader, select_autoescape
from typing import List

env = Environment(
    loader=PackageLoader("quick_form"),
    autoescape=select_autoescape()
)

class Field:
    def __init__(self, field_name: str, label: str = None, hidden: bool = False) -> None:
        self.field_name = field_name
        if label is None:
            label = field_name
        self.label = label      
        self.hidden = hidden
        self.hide_when = {}
        self.show_when = {}
        self.changeHandle = "handle" + self.field_name



class Input(Field):
    def __init__(self, field_name: str, label: str = None, hidden: bool = False) -> None:
         super().__init__(field_name, label, hidden)


class Row:
    def __init__(self) -> None:
        self._fields = []
    @property
    def fields(self) -> List[Field]:
        return self._fields

    
class QuickForm:
    def __init__(self, header: str = "My Form", action: str = "#", method: str = "post", button_label: str = "Submit") -> None:
        self.header = header
        self.action = action
        self.method = method
        self.button_label = button_label
        self._rows = []
        self._fields = []
    
    @property
    def rows(self) -> List[Row]:
        return self._rows
    
    @property
    def fields(self) -> List[Row]:
        return self._fields

    def add_row(self, row: Row = None) -> Row:
        if not row:
             row = Row()
        else:
             if not isinstance(row, Row):
                  raise TypeError("must be of type Row!")
        self._rows.append(row)
        return self.rows[-1]
    
    def add_field(self, row: Row, field: Field) -> Field:
        if isinstance(row, int):
            row = self.rows[row]
        elif not isinstance(row, Row):
           raise TypeError('row argument must be of type Row or Int')
        
        if isinstance(field, Field): 
            row._fields.append(field)
            self._fields.append(field)
            return self.fields[-1]
        else:
            raise TypeError("field argument must be of type Field")
    
    def render(self, file_path: str) -> None:
        template = env.get_template("index.html")
        output = template.render(form=self)
        with open(file_path, 'w') as HTML_form:
            HTML_form.write(output)
        webbrowser.open('file://' + os.path.realpath(file_path))
    
    def hide_if(self, target_field: Field, event_field: Field, value: str) -> None:
        if value in event_field.hide_when:
            event_field.hide_when[value].append(target_field)
        else:
            event_field.hide_when[value] = [target_field]
    def show_if(self, target_field: Field, event_field: Field, value: str) -> None:
        if value in event_field.show_when:
            event_field.show_when[value].append(target_field)
        else:
            event_field.show_when[value] = [target_field]

        