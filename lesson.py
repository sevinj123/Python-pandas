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


# #indi ise benzin ve dizel olmaqla qruplara ayiraciq ve benzinle olanlari topladi ededi ortasini bir cixardi dizellerinkini bir
# import pandas as pd
# df=pd.read_excel('Python-pandas/cars.xlsx')
# typeanalys=df.groupby('Type')['Price'].agg(['count' , 'sum' , 'min'])           #.mean() evezine .sum() .count() .max() .min ve s cixara bilersen
# print(typeanalys)
# #.agg() ise hamisini gormeye komek edir. mes ['Price].agg(['count' , 'sum' , 'min'])

# import pandas as pd
# df=pd.read_excel('Python-pandas/cars.xlsx')
# newcar=df[(df['Price']<=20000) & (df['Mark']==('Toyota'))]
# print(newcar)





#həm "BMW" olan, həm də ili 2015-dən böyük
# import pandas as pd
# df=pd.read_excel('Python-pandas/cars.xlsx')
# bmw=df[(df['Mark']=='BMW') & (df['Year']>=2015)]
# bmw_value=bmw.sort_values('KM')  #burda bmw yazdim cwnki yuxaridaki setrin filter olunaninin bir daha filter olmasini isteyirem
# #ve hetta bunu iki setr yox da bir setrde yazmaq olar
# #bmw olan kodun ] isaresinden sonra en sonuna .sort_values('KM') yazmaq olar
# # print(bmw_value)




# import pandas as pd
# df=pd.read_excel('Python-pandas/cars.xlsx')
# toyotas=df[df['Mark'] == ('Toyota')]
# pricedif=toyotas['Price'].max() - toyotas['Price'].min()
# print(pricedif)


# #Mənə elə maşınları göstər ki, həm Yanacaq növü (Type) 'Benzin' olsun, həm də Yürüşü (KM) 50.000-dən az olsun.
# import pandas as pd
# df=pd.read_excel('Python-pandas/cars.xlsx')
# kmtype=df[(df['Type'] == 'Benzin') & (df['KM'] <= 50000)].sort_values('Type')
# #type_value = kmtype.sort_values('Type')
# print(kmtype)


# #Bütün Mercedes-lərin orta (mean) qiymətini tapsın.Bütün BMW-lərin orta (mean) qiymətini tapsın.Terminalda bu iki orta qiymət arasındakı fərqi göstərsin.
# import pandas as pd
# df=pd.read_excel('Python-pandas/cars.xlsx')
# mercedes=df[df['Mark'] == 'Mercedes']['Price'].mean()
# bmw=df[df['Mark'] == 'BMW']['Price'].mean()
# terminal= mercedes-bmw
# print(terminal)

#ele bir kod yaz ki cedvele yeni section elave edilsin ve 10% bahalasma ile qiymet qeyd edilsin
import pandas as pd
df=pd.read_excel('Python-pandas/cars.xlsx')
currentable=df['Price_increase'] = df['Price'] * 1.1    #bu ise artimi
currentable=df['Price_decrease'] = df['Price'] * 0.9  #bu 19% azalmani gosterir
print(df)   #burda df yazdim cenki butun cedveli gormek isteyirem