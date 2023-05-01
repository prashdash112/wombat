from wombat import wombat 
import pandas as pd

#reading df
df = pd.read_csv('variant_v.csv')

if __name__ =="__main__":
    summary = wombat.metric_summary(df,path_to_save='summary.csv')
    datacard = wombat.datacard(df, path_to_save='Datacard_user.txt')
    version = wombat.version(df.head(5),file_name='fraud_bool', folder_path='./local_repo')
    report = wombat.generate_report(df=df.head(10), path_to_save='./Data_Profile_Report.html', pdf=False)
    schema = wombat.schema(df=df,path_to_save='schema.csv',show=1)