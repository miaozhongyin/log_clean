import pandas as pd
import json,sys
df = pd.read_table(sys.argv[1]+'.log1',sep='\|\#\$',engine='python',names=['serialName','bizCode','jsondata'])
data = df.to_dict(orient='records')
for _ in data:
	_.update(json.loads(_['jsondata'],encoding='utf-8'))
	del _['jsondata']

df1 = pd.DataFrame(data)
#print df1
df1.to_json(sys.argv[1]+".json",orient='records',force_ascii=False)
#print pd.read_json("./bos_qscore1.json")
