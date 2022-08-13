import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
from IPython.display import display, Markdown

def univ_hisplot(df,col_name,ax):
    """ Grafico histograma con linea de densidad asociad """
    plot0=sns.histplot(data = df,x =col_name, ax=ax,color='green', kde=True)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax.set_title(f'Distribution of {col_name}',fontdict={'fontsize':8})
    ax.set_xlabel(col_name,fontdict={'fontsize':7})
    ax.set_ylabel(r'Count/Dist.',fontdict={'fontsize':7})
    plt.tight_layout()



def univ_boxplot(df,col_name,ax):
    """ Diagrama de cajas"""
    plot1=sns.boxplot(data = df[col_name],ax=ax,orient='v')
    ax.set_title('Box plot',fontdict={'fontsize':8})
    ax.set_ylabel(col_name,fontdict={'fontsize':7})
    plt.tight_layout()
    


def univ_violinplot(df,col_name,ax):
    """Grafico de violin"""
    plot2=sns.violinplot(x = df[col_name],ax=ax,palette="Set1")
    ax.set_title('Violin Plot',fontdict={'fontsize':8})
    ax.set_xlabel(col_name,fontdict={'fontsize':7})
    plt.tight_layout()

def plots_univariate_analysis(dataframe,column_name):
    """Grafica histograma, digrama de cajas y grafico de violina para colum_name"""
    fig,axes = plt.subplots(nrows=1,ncols=3,dpi=120,figsize = (10,5))
    fig.suptitle('Graficos para analisis univariados')
    univ_hisplot(dataframe,column_name,axes[0])
    univ_boxplot(dataframe,column_name,axes[1])
    univ_violinplot(dataframe,column_name,axes[2])
    plt.show()

def freq_dist(df, col_name):
    """Arma la tabla de distribucion de frecuencias de col_name"""
    frec_df = df[col_name].value_counts().reset_index().rename(columns={col_name: 'frec_abs',
                                                                        'index': col_name}).sort_values(col_name)
    frec_df['frec_abs_acum'] = frec_df['frec_abs'].cumsum()
    frec_df['frec_rel_%'] = round(100 * frec_df['frec_abs']/len(df[col_name]), 4)
    frec_df['frec_rel_%_acum'] = frec_df['frec_rel_%'].cumsum()
    display(frec_df)


def univariate_analysis(dataframe, column_name, table_dist= False):
    """Muestra el analisis univariado para column_name :
        -Descripcion estadistica de colum_name
        -Histograma, diagrama de cajas, y grafico de violin de column_name
        -Tabla de distribucion de frecuencias"""
    display(Markdown(f'### Descripcion de la columna {column_name} '))
    
    print(dataframe[column_name].describe().round(3))
    plots_univariate_analysis(dataframe,column_name)
    
    if table_dist:
        display(Markdown('### Distribucion de frequencias '))
        freq_dist(dataframe,column_name)
    
def count_plot_percentage(df, col_name, title, color_f =["#7C3030"]):
    """Grafico de barras con porcentaje de frecuencias"""
    plt.figure(figsize=(15, 8))
    ax = sns.countplot(data = df, x=col_name, order = df[col_name].value_counts().index, palette=color_f)
    plt.xticks(size=12)
    plt.title(title)
    plt.xlabel(col_name, size=14)
    plt.ylabel('Count', size=14)

    total = len(df[col_name])
    for p in ax.patches:
        percentage = '{:.2f}%'.format(100 * p.get_height()/total)
        x = p.get_x() + p.get_width() / 2 - 0.16
        y = p.get_y() + p.get_height()
        ax.annotate(percentage, (x, y), size = 14)
    