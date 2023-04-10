from wombat_dev import wombat #.wombat import metric_summary
import pandas as pd
from wombat_dev.wombat import versioning


df = pd.read_csv('variant_v.csv')
summary = wombat.metric_summary(df,path_to_save='summary.csv')
