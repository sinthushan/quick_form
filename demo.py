from quick_form import QuickForm, Row, Input

my_form = QuickForm()
new_row = Row()
new_row.add_column()
new_row.add_column()
my_form.add_row()
my_form.add_row()
row = my_form.add_row()
my_form.add_row(new_row)
row.add_column()

input = Input("Name")
new_row.columns[1].add_field(input)
for row in my_form.rows:
    print(row)
print(my_form.rows[3].columns[1].fields[0].field_name)