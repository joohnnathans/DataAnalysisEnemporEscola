import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import qgrid
low_memory=False



df = pd.read_csv('microdados_enem_por_escola\\dados\\MICRODADOS_ENEM_ESCOLA.csv',
                 delimiter=';',
                 encoding='iso-8859-1',
                 usecols=["NU_ANO", "CO_UF_ESCOLA", "SG_UF_ESCOLA", "NO_MUNICIPIO_ESCOLA", "NO_ESCOLA_EDUCACENSO", "TP_DEPENDENCIA_ADM_ESCOLA", "TP_LOCALIZACAO_ESCOLA", "NU_MATRICULAS", "NU_PARTICIPANTES_NEC_ESP", "NU_PARTICIPANTES", "NU_TAXA_PARTICIPACAO", "NU_MEDIA_CN", "NU_MEDIA_CH", "NU_MEDIA_LP", "NU_MEDIA_MT", "NU_MEDIA_RED", "NU_MEDIA_OBJ", "NU_MEDIA_TOT", "NU_TAXA_APROVACAO", "NU_TAXA_REPROVACAO", "NU_TAXA_ABANDONO", "PORTE_ESCOLA"])

# print(df.describe())

# print(df.head(n=10))
# print(df.tail())
# print(df["SG_UF_ESCOLA"].unique())
# print(df["SG_UF_ESCOLA"].value_counts())
# print(df["SG_UF_ESCOLA"].value_counts(normalize = True))

#print(df.groupby("NO_MUNICIPIO_ESCOLA").mean())

##grafio ta ficando grande demais
# plt.bar(df["SG_UF_ESCOLA"], df["NU_MEDIA_MT"], color="red")
# plt.show()
#print(df["NU_MATRICULAS"].plot.hist(bins=30, edgecolor='black'))
# print(df.sample(10).sort_values(by='NU_MATRICULAS'))
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



# file_enem_por_escola =  open(r'microdados_enem_por_escola\\dados\\MICRODADOS_ENEM_ESCOLA.csv')

# campos_file = file_enem_por_escola.readline()
# campos_file = campos_file.split(";")
# pd.DataFrame(campos_file)



# base_enem_escola = {"NU_ANO":[],"CO_UF_ESCOLA":[],"SG_UF_ESCOLA":[],"NO_MUNICIPIO_ESCOLA":[],"NO_ESCOLA_EDUCACENSO":[],"TP_DEPENDENCIA_ADM_ESCOLA":[],"TP_LOCALIZACAO_ESCOLA":[],
#                    "NU_MATRICULAS":[],"NU_PARTICIPANTES_NEC_ESP":[],"NU_PARTICIPANTES":[],"NU_TAXA_PARTICIPACAO":[],"NU_MEDIA_CN":[],"NU_MEDIA_CH":[],"NU_MEDIA_LP":[],"NU_MEDIA_MT":[],
#                    "NU_MEDIA_RED":[],"NU_MEDIA_OBJ":[],"NU_MEDIA_TOT":[],"NU_TAXA_APROVACAO":[],"NU_TAXA_REPROVACAO":[],"NU_TAXA_ABANDONO":[],"PORTE_ESCOLA":[]}

# for i in file_enem_por_escola:
#     i = i.split(";")
#     base_enem_escola["NU_ANO"].append(i[campos_file.index('NU_ANO')])
#     base_enem_escola["CO_UF_ESCOLA"].append(i[campos_file.index('CO_UF_ESCOLA')])
#     base_enem_escola["SG_UF_ESCOLA"].append(i[campos_file.index('SG_UF_ESCOLA')])
#     base_enem_escola["NO_MUNICIPIO_ESCOLA"].append(i[campos_file.index('NO_MUNICIPIO_ESCOLA')])
#     base_enem_escola["NO_ESCOLA_EDUCACENSO"].append(i[campos_file.index('NO_ESCOLA_EDUCACENSO')])
#     base_enem_escola["TP_DEPENDENCIA_ADM_ESCOLA"].append(i[campos_file.index('TP_DEPENDENCIA_ADM_ESCOLA')])
#     base_enem_escola["TP_LOCALIZACAO_ESCOLA"].append(i[campos_file.index('TP_LOCALIZACAO_ESCOLA')])
#     base_enem_escola["NU_MATRICULAS"].append(i[campos_file.index('NU_MATRICULAS')])
#     base_enem_escola["NU_PARTICIPANTES_NEC_ESP"].append(i[campos_file.index('NU_PARTICIPANTES_NEC_ESP')])
#     base_enem_escola["NU_PARTICIPANTES"].append(i[campos_file.index('NU_PARTICIPANTES')])
#     base_enem_escola["NU_TAXA_PARTICIPACAO"].append(i[campos_file.index('NU_TAXA_PARTICIPACAO')])
#     base_enem_escola["NU_MEDIA_CN"].append(i[campos_file.index('NU_MEDIA_CN')])
#     base_enem_escola["NU_MEDIA_CH"].append(i[campos_file.index('NU_MEDIA_CH')])
#     base_enem_escola["NU_MEDIA_LP"].append(i[campos_file.index('NU_MEDIA_LP')])
#     base_enem_escola["NU_MEDIA_MT"].append(i[campos_file.index('NU_MEDIA_MT')])
#     base_enem_escola["NU_MEDIA_RED"].append(i[campos_file.index('NU_MEDIA_RED')])
#     base_enem_escola["NU_MEDIA_OBJ"].append(i[campos_file.index('NU_MEDIA_OBJ')])
#     base_enem_escola["NU_MEDIA_TOT"].append(i[campos_file.index('NU_MEDIA_TOT')])
#     base_enem_escola["NU_TAXA_APROVACAO"].append(i[campos_file.index('NU_TAXA_APROVACAO')])
#     base_enem_escola["NU_TAXA_REPROVACAO"].append(i[campos_file.index('NU_TAXA_REPROVACAO')])
#     base_enem_escola["NU_TAXA_ABANDONO"].append(i[campos_file.index('NU_TAXA_ABANDONO')])
#     base_enem_escola["PORTE_ESCOLA"].append(i[campos_file.index('PORTE_ESCOLA\n')])

#     pd.DataFrame(base_enem_escola)