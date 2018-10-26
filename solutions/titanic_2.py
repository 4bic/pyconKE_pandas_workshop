(titanic.rename(columns={'Pclass': 'Class'})
        .pivot_table(values='Survived', index='Sex', columns='Class', aggfunc='mean')
        .style.format('{:.2%}'))
