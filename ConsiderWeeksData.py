#Give the List of columns consisting of an ID and the summarized features
#Summarization of features would in Weeks
#This selects 13 weeks of data ignoring the last 13 weeks from the last used date
def considerRows(Dataframe, ListofColumns):
    new_df = pandas.DataFrame()
    usages_df = Dataframe[ListofColumns]
    usages_df = usages_df.fillna(0)
    usages_df_grouped = usages_df.groupby('ID')
    for each in new_df_grouped:
        df =  each[1]
        distinct_weeks = sorted(frozenset(df['Week_Value']))
        total_weeks = len(distinct_weeks)
        if len(distinct_weeks) < 26:
            usages_df = usages_df[usages_df['ID'] == each[0]]
        else:
            consider_weeks = distinct_weeks[total_weeks-26:total_weeks-13]
            df = df[df['Week_Value'].isin(consider_weeks)]
            new_df = pandas.concat([new_df,df])
    return new_df
