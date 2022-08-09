import pandas as pd


def get_upper_limit_whisker(column_df):
    """
    Calculate the max whisker value.
    """
    # Rango interquartil de los superior
    iqr = column_df.quantile(0.75) - column_df.quantile(0.25)
    # Obtenemos el valor limite del boxplot 
    return column_df.quantile(0.75) + 1.5 * (iqr)


def get_lower_limit_whisker(column_df):
    """
    Calculate the min whisker value.
    """
    # Rango interquartil de los inferior
    iqr = column_df.quantile(0.75) - column_df.quantile(0.25)
    # Obtenemos el valor limite del boxplot 
    return column_df.quantile(0.25) - 1.5 * (iqr)

def calculate_frequency_values(df, column):
    """
    Calculate the frequency of each value in a column.
    """
    # Vemos los valores de type
    ps_frequency_unique = df[column].value_counts(normalize=True).map(lambda x: round(x, 3)*100).sort_values(ascending=False)
    # accum frequency of values of ps_frequency_unique_type
    accumulated_percentage= ps_frequency_unique.cumsum()
    df_frecuency = pd.concat([ps_frequency_unique, accumulated_percentage], axis=1)
    # change column names
    df_frecuency.columns = ['porcentaje', 'porcentaje_acumulado']
    return df_frecuency
