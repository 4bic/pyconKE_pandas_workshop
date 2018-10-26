titanic['Embarked'].unique()

titanic = titanic.assign(Embarked=titanic['Embarked'].replace({'S': 'Southampton, England',
                                                               'C': 'Cherbourg, France',
                                                               'Q': 'Queenstown (Cobh), Ireland'}))

titanic['Embarked'].value_counts()

titanic['Embarked'].value_counts(normalize=True)

titanic['Embarked'].value_counts(normalize=True).sort_values().plot(kind='barh');
