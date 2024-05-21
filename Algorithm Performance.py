#Link: https://platform.stratascratch.com/coding/10350-algorithm-performance?code_type=1

fb_search_events.head()
fb_search_events['ratings'] = 1
fb_search_events.loc[(fb_search_events['search_results_position'] > 3) & (fb_search_events['clicked'] == 1), 'ratings'] = 2
fb_search_events.loc[(fb_search_events['search_results_position'].between(0, 3)) & (fb_search_events['clicked'] == 1), 'ratings'] = 3 

fb_search_events = fb_search_events[['search_id', 'ratings']]
result = fb_search_events.groupby('search_id')['ratings'].max().reset_index()
result
