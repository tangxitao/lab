import pandas as pd 
df1 =pd.read_csv("CPU使用率1.csv")
del df1["Time"]
df2=pd.read_csv("CPU使用率3.csv")
del df2["Time"]
df3 =pd.read_csv("CPU使用率5.csv")
del df3["Time"]
df=pd.concat([df1,df2,df3],axis=1)

df1 =pd.read_csv("每秒磁盘读写容量1.csv")
del df1["Time"]
df2=pd.read_csv("每秒磁盘读写容量3.csv")
del df2["Time"]
df3 =pd.read_csv("每秒磁盘读写容量5.csv")
del df3["Time"]
df=pd.concat([df,df1,df2,df3],axis=1)

df1 =pd.read_csv("GPU Power Usage.csv")
del df1["Time"]
df1 = df1.rename(columns={'GPU 0': '181_GPU0_Power'})
df1 = df1.rename(columns={'GPU 1': '181_GPU1_Power'})
df1 = df1.rename(columns={'GPU 2': '181_GPU2_Power'})
df1 = df1.rename(columns={'GPU 3': '181_GPU3_Power'})
df1 = df1.rename(columns={'GPU 0.1': '185_GPU0_Power'})
df1 = df1.rename(columns={'GPU 1.1': '185_GPU1_Power'})
df1 = df1.rename(columns={'GPU 2.1': '185_GPU2_Power'})
df1 = df1.rename(columns={'GPU 3.1': '185_GPU3_Power'})
df1 = df1.rename(columns={'GPU 0.2': '183_GPU0_Power'})
df1 = df1.rename(columns={'GPU 1.2': '183_GPU1_Power'})
df1 = df1.rename(columns={'GPU 2.2': '183_GPU2_Power'})
df1 = df1.rename(columns={'GPU 3.2': '183_GPU3_Power'})
df2=pd.read_csv("GPU Temperature.csv")
del df2["Time"]
df2 = df2.rename(columns={'GPU 0': '181_GPU0_temp'})
df2 = df2.rename(columns={'GPU 1': '181_GPU1_temp'})
df2 = df2.rename(columns={'GPU 2': '181_GPU2_temp'})
df2 = df2.rename(columns={'GPU 3': '181_GPU3_temp'})
df2 = df2.rename(columns={'GPU 0.1': '185_GPU0_temp'})
df2 = df2.rename(columns={'GPU 1.1': '185_GPU1_temp'})
df2 = df2.rename(columns={'GPU 2.1': '185_GPU2_temp'})
df2 = df2.rename(columns={'GPU 3.1': '185_GPU3_temp'})
df2 = df2.rename(columns={'GPU 0.2': '183_GPU0_temp'})
df2 = df2.rename(columns={'GPU 1.2': '183_GPU1_temp'})
df2 = df2.rename(columns={'GPU 2.2': '183_GPU2_temp'})
df2 = df2.rename(columns={'GPU 3.2': '183_GPU3_temp'})
df3 =pd.read_csv("GPU Utilization.csv")
del df3["Time"]
df3 = df3.rename(columns={'GPU 0': '181_GPU0_usage'})
df3 = df3.rename(columns={'GPU 1': '181_GPU1_usage'})
df3 = df3.rename(columns={'GPU 2': '181_GPU2_usage'})
df3 = df3.rename(columns={'GPU 3': '181_GPU3_usage'})
df3 = df3.rename(columns={'GPU 0.1': '185_GPU0_usage'})
df3 = df3.rename(columns={'GPU 1.1': '185_GPU1_usage'})
df3 = df3.rename(columns={'GPU 2.1': '185_GPU2_usage'})
df3 = df3.rename(columns={'GPU 3.1': '185_GPU3_usage'})
df3 = df3.rename(columns={'GPU 0.2': '183_GPU0_usage'})
df3 = df3.rename(columns={'GPU 1.2': '183_GPU1_usage'})
df3 = df3.rename(columns={'GPU 2.2': '183_GPU2_usage'})
df3 = df3.rename(columns={'GPU 3.2': '183_GPU3_usage'})

df4=pd.read_csv("GPU Framebuffer.csv")
del df4["Time"]
df4 = df4.rename(columns={'GPU 0': '181_GPU0_mem'})
df4 = df4.rename(columns={'GPU 1': '181_GPU1_mem'})
df4 = df4.rename(columns={'GPU 2': '181_GPU2_mem'})
df4 = df4.rename(columns={'GPU 3': '181_GPU3_mem'})
df4 = df4.rename(columns={'GPU 0.1': '185_GPU0_mem'})
df4 = df4.rename(columns={'GPU 1.1': '185_GPU1_mem'})
df4 = df4.rename(columns={'GPU 2.1': '185_GPU2_mem'})
df4 = df4.rename(columns={'GPU 3.1': '185_GPU3_mem'})
df4 = df4.rename(columns={'GPU 0.2': '183_GPU0_mem'})
df4 = df4.rename(columns={'GPU 1.2': '183_GPU1_mem'})
df4 = df4.rename(columns={'GPU 2.2': '183_GPU2_mem'})
df4 = df4.rename(columns={'GPU 3.2': '183_GPU3_mem'})

df=pd.concat([df,df1,df2,df3,df4],axis=1)

df.to_csv("1.csv",index=False)
print(df)






