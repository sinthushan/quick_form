from quick_form import QuickForm, Row, Input

my_form = QuickForm()
new_row = Row()
my_form.add_row(new_row)
my_form.add_row()
input_one = Input("Name")
input_two = Input("Account")
input_three = Input("Address")
my_form.add_field(new_row,input_one)
my_form.add_field(0,input_two)
my_form.add_field(1,input_three)

my_form.render("output.html")