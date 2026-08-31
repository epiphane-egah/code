import logging

logger = logging.logging.getLogger()
logger.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s:%(message)s',
                             '%m-%d-%Y %H:%M:%S')


file_handler = logging.FileHandler('logs/eleve.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)




groupby_m = df_filtre.groupby([pd.Grouper(key = 'publishedAt', freq = 'm'),
                              df_filtre['categoryId']])\
                    .agg({'likes':'mean'}).unstack().fillna(0)
groupby_m.plot(figsize = (20, 4.5), style = 'o-');

