from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    current_date = datetime.now().strftime('%d/%m/%Y')
    msg_body = template.safe_substitute(name="Pedro", date=current_date)
    #safe_substitute will not return error if is missing some placeholder, like substitute did.
print(msg_body)
