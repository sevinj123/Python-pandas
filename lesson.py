# import pandas as pd
# df=pd.read_excel('Python-pandas/cars.xlsx')
# print(df)

# import pandas as pd
# df=pd.read_excel('Python-pandas/cars.xlsx')
# #summarize=df['Price']>20000   #bu deyir ki her setre sual verir senin qiymetin 20.000 den boyukdur mu ya yox netice olaraq cavab true false olur
# #summarize=df[df['Price']>20000]  #burda sadece deyir ki qiymeti boywk olsun
# summarize=df[(df['Price']>20000) &( df['KM']>20000)]
# print(summarize)   

# import pandas as pd
# df=pd.read_excel('Python-pandas/cars.xlsx')
# average=df.groupby('Mark')['Price'].mean()
# print(average)           
# #bu kodda cedvelde ne qeder masin varsa onlarin ededi ortasini cixardi
# #her masindan 1 dene var deye ededi orta eyni qaldi ama ferqli sayda olsaydi qiymet deyisecekdi


#indi ise benzin ve dizel olmaqla qruplara ayiraciq ve benzinle olanlari topladi ededi ortasini bir cixardi dizellerinkini bir
import pandas as pd
df=pd.read_excel('Python-pandas/cars.xlsx')
typeanalys=df.groupby('Type')['Price'].agg(['count' , 'sum' , 'min'])           #.mean() evezine .sum() .count() .max() .min ve s cixara bilersen
print(typeanalys)
#.agg() ise hamisini gormeye komek edir. mes ['Price].agg(['count' , 'sum' , 'min'])