import jinja2
# create Jinja2 Environment
env = jinja2.Environment(loader = jinja2.FileSystemLoader('./'))

# load template
template = env.get_template('template.j2')

# rendering
data = {
   'bgp_filters':{
       'flb': {
           'in': ('permit', '66.66.66.66/32'),
       }
   }
}
result = template.render(data)

print(result)
