import pandas as pd
import re

with open('bcipep.dat','r') as f:
	columns = ['Entry',
			 			'Sequence',
			 	  	  	'Model_studied',
			 	  	  	'Method',
			 	  		'Source',
			 			'Antibody',
			 			'DbReference',
						'Citation',
						'Immunogenicity',
						'Neutralization',
						'AntigenStru',
						'Pathogen',
						'Comment']
	bc_df= pd.DataFrame(columns = columns)
	row = 0
	bc_df.loc[row] = [None for n in range(len(columns))]
	for line in f:
		line = re.split(r'\s+', line)
		if line[0] not in columns:
			continue
		if not bc_df.loc[row, line[0]] == None:
			row +=1
			bc_df.loc[row] = [None for n in range(len(columns))]
		bc_df.loc[row, line[0]] = line[1]

print(bc_df.head)
