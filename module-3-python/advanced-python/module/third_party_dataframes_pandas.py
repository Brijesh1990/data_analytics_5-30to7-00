# import pandas as pd
# pd.show_versions()

import pandas as pd 
# employee={"id":1,"name":"brijesh","age":36,"department":"IT"}
employee={
"first_name": ["Bob", "Jane"],
"last_name": ["Doe", "Swift"]
}
print(pd.DataFrame(employee))

# DataFrame() is an method create a frame in tabular layout 