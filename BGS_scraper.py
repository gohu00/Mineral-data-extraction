def BGS_scraper (datee, datea, commodity) :
  url = f"https://www2.bgs.ac.uk/mineralsuk/statistics/wms.cfc?method=listResults&dataType=Production&dateFrom={datea}&dateTo={datee}&commodity={commodity}&country=&agreeToTsAndCs=agreed&exportToSpreadsheet=Yes"
  urllib.request.urlretrieve(url, "test.xlsx")
  df = pd.read_excel('test.xlsx', header = 1) 
  df = df[['\n\tCountry',
             'Unnamed: 3',
             'Unnamed: 5',
             'Unnamed: 7',
             'Unnamed: 9',
             'Unnamed: 11',
             'Unnamed: 13',
             'Unnamed: 15',
             'Unnamed: 17',
             'Unnamed: 19',
             'Unnamed: 21',
             'Unnamed: 23',
             ]]
  df = df.rename(columns={
             '\n\tCountry': 'Pays',
             'Unnamed: 3':f'{datea}',
             'Unnamed: 5':f'{datea+1}',
             'Unnamed: 7':f'{datea+2}',
             'Unnamed: 9':f'{datea+3}',
             'Unnamed: 11':f'{datea+4}',
             'Unnamed: 13':f'{datea+5}',
             'Unnamed: 15':f'{datea+6}',
             'Unnamed: 17':f'{datea+7}',
             'Unnamed: 19':f'{datea+8}',
             'Unnamed: 21':f'{datea+9}',
             'Unnamed: 23':f'{datea+10}',
             })
  df = df[df['Pays'].isin(options)]
  df= df.T
  new_header = df.iloc[0] #grab the first row for the header
  df = df[1:] #take the data less the header row
  df.columns = new_header
  return df 
