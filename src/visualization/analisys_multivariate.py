import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def scatter_one_to_some(df, col_name, target_col_name):
    """Grafico de dispersión de una columna con varias columnas"""
    fig, axes = plt.subplots(ncols=5,nrows=3,sharey=True)
    fig.set_figheight(20)
    fig.set_figwidth(30)
    for ax, numerical_feature in zip(axes.flat, df.drop([col_name,target_col_name], axis = 1)):
        g = sns.scatterplot(x=numerical_feature, y=col_name, data=df, ax=ax, hue=target_col_name)
        g.set_xlabel(numerical_feature,fontsize=20)
        g.set_ylabel(col_name,fontsize=20)
    fig.suptitle(f'Pairplot de {col_name} con el resto de las variables en relacion con la calidad de vino', fontsize=30)
    fig.tight_layout()
    plt.show()
