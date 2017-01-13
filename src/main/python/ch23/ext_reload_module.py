import module1

module1.printer('taosm')

from imp import reload
reload(module1)

module1.printer('lihui')