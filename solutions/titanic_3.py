full_names.str.split('.').str[0].value_counts()

titanic.loc[full_names.str.startswith('Capt.'), ('Name', 'Age', 'Pclass')]
