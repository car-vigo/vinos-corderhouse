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
