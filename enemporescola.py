import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import qgrid
low_memory=False



df = pd.read_csv('microdados_enem_por_escola\\dados\\MICRODADOS_ENEM_ESCOLA.csv',
                 delimiter=';',
                 encoding='iso-8859-1',
                 usecols=["NU_ANO", "CO_UF_ESCOLA", "SG_UF_ESCOLA", "NO_MUNICIPIO_ESCOLA", "NO_ESCOLA_EDUCACENSO", "TP_DEPENDENCIA_ADM_ESCOLA", "TP_LOCALIZACAO_ESCOLA", "NU_MATRICULAS", "NU_PARTICIPANTES_NEC_ESP", "NU_PARTICIPANTES", "NU_TAXA_PARTICIPACAO", "NU_MEDIA_CN", "NU_MEDIA_CH", "NU_MEDIA_LP", "NU_MEDIA_MT", "NU_MEDIA_RED", "NU_MEDIA_OBJ", "NU_MEDIA_TOT", "NU_TAXA_APROVACAO", "NU_TAXA_REPROVACAO", "NU_TAXA_ABANDONO", "PORTE_ESCOLA"])

print(df.describe())

print(df.head(n=10))
print(df.tail())
print(df["SG_UF_ESCOLA"].unique())
print(df["SG_UF_ESCOLA"].value_counts())
print(df["SG_UF_ESCOLA"].value_counts(normalize = True))

#print(df.groupby("NO_MUNICIPIO_ESCOLA").mean())

##grafio ta ficando grande demais
# plt.bar(df["SG_UF_ESCOLA"], df["NU_MEDIA_MT"], color="red")
# plt.show()
#print(df["NU_MATRICULAS"].plot.hist(bins=30, edgecolor='black'))
print(df.sample(10).sort_values(by='NU_MATRICULAS'))
# print(df.sample(3).sort_values(by= "NU_MEDIA_CN"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_CH"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_LP"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_MT"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_RED"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_OBJ"))
# print(df.sample(3).sort_values(by= "NU_MEDIA_TOT"))
# print(df.sample(3).sort_values(by= "NU_TAXA_APROVACAO"))
# print(df.sample(3).sort_values(by= "NU_TAXA_REPROVACAO"))
# print(df.sample(3).sort_values(by= "NU_TAXA_ABANDONO"))
# print(df.sample(3).sort_values(by= "NU_TAXA_PARTICIPACAO"))