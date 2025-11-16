

from auxiliar import *

# A ideia do projeto será comparar como o número de features (high ou low dimensions) afeta a classificação de dados Windows Executables Programs como vírus ou não. No caso, o SET escolhido tem diversas informaçoes sobre cada programa:
    # Temos: 1) API_Functions => Descreve se uma dada API function é ou não usada ao longo do programa
    #        2) DLLS => Se dado programa importa ou não uma certa DLL (HIGH DIM => 630)
    #        3) PE_Section => Mapeia o conteúdo completo nos detalhes do executável (como se fosse o conteúdo factual do livro) (LOW DIM)
    #        4) PE_HEader => Mapeia o geral de um programa (como se fosse o sumário de um livro) (LOW DIM)
# Para facilitar o projeto, vamos utilizar as DLLs (menos features e boa capacidade descritiva) e Header (menos complexa, mais simples de tratar) e comparar como 2 diferentes classificadores se comportam em um SET com mais/menos features.
DLLs_filename = 'dataset/DLLs_Binary_imported.csv'
PE_header_filename = 'dataset/PE_header_binary_df_imported.csv'

DLL_df = pd.read_csv(DLLs_filename)
PE_header_df = pd.read_csv(PE_header_filename)

# createBinaryCSV(DLL_df, 'Type', './dataset/DLLs_Binary_imported.csv')
# createBinaryCSV(PE_header_df, 'Type', './dataset/PE_header_binary_df_imported.csv')

print(DLL_df.describe())
