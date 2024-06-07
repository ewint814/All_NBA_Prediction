#defining a function to get total season stats per player
def get_player_total_season_stats(year):
    #from the api wrapper
    client.players_season_totals(
        season_end_year= year, 
        output_type=OutputType.CSV, 
        output_file_path=f"./total_stats/{year-1}_{year}_player_season_totals.csv"
    )
    #dropping slug column
    df = pd.read_csv(f'./total_stats/{year-1}_{year}_player_season_totals.csv')
    df.drop(columns = 'slug', inplace = True)
    return df.to_csv(f"./total_stats/{year-1}_{year}_player_season_totals.csv", index = False)

#defining a function to combine players who were traded total season stats
def combine_traded_player_total_stats(df):
    player = df['name'].value_counts()
    multi_player = player[player > 1].index
    #create a new dataframe that just has the duplicate payers in it
    multi_df = df[df['name'].isin(multi_player)]
    df = df[df['name'].apply(lambda x: x not in multi_player)]

    #combine the stats from the duplicate players
    combo_stats = multi_df.groupby('name')[['games_played', 'games_started', 'minutes_played', 'made_field_goals', 'attempted_field_goals', 'made_three_point_field_goals', 'attempted_three_point_field_goals', 'made_free_throws', 'attempted_free_throws', 'offensive_rebounds', 'defensive_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'points']].sum().reset_index()
    #combine the teams with a ',' in between
    combo_teams = multi_df.groupby('name')['team'].apply(lambda x: ', '.join(x)).reset_index()
    #merge the dataframes
    combo_df = pd.merge(combo_stats, combo_teams, on='name')
    #only take the first position since it should be the same
    combo_positions = multi_df.groupby('name')['positions'].first().reset_index()
    #combine the dataframes
    combo_df = pd.merge(combo_df, combo_positions, on='name')
    #only take the first age since we dont want to sum them
    age = multi_df.groupby('name')['age'].first().reset_index()
    #combine dataframe
    combo_df = pd.merge(combo_df, age, on='name')
    #concat the dataframe with the combined stats with the old dataframe.
    df = pd.concat([df, combo_df], axis = 0).reset_index(drop = True)
    return df

#defining a function to clean the team and positions column for total season stats
def clean_total_stats(df):
    #make the positions and team columns title case
    df['team'] = df['team'].str.title()
    df['positions'] = df['positions'].str.title()
    return df

#gets player advanced stat totals per season
def get_player_advanced_season_stats(year):
    client.players_advanced_season_totals(
        season_end_year=year,
        output_type=OutputType.CSV,
        output_file_path=f"./advanced_season_stat_total/{year-1}_{year}_advanced_player_season_totals.csv"
)
#dropping duplicate and not needed columns 
    df = pd.read_csv(f'./advanced_season_stat_total/{year-1}_{year}_advanced_player_season_totals.csv')
    df.drop(columns = ['slug', 'positions', 'age', 'team', 'minutes_played', 'is_combined_totals'] , inplace = True)
    return df.to_csv(f"./advanced_season_stat_total/{year-1}_{year}_advanced_player_season_totals.csv", index = False)

#defining a function to combine players who were traded advanced stats
def combine_traded_player_advanced_stats(df):
    player = df['name'].value_counts()
    multi_player = player[player > 1].index
    #create a new dataframe that just has the duplicate payers in it
    multi_df = df[df['name'].isin(multi_player)]
    df = df[df['name'].apply(lambda x: x not in multi_player)]

    #combine the stats from the duplicate players
    combo_stats = multi_df.groupby('name')[['player_efficiency_rating', 'true_shooting_percentage', 'three_point_attempt_rate', 'free_throw_attempt_rate', 'offensive_rebound_percentage', 'defensive_rebound_percentage', 'total_rebound_percentage', 'assist_percentage', 'steal_percentage', 'block_percentage', 'turnover_percentage', 'usage_percentage', 'offensive_win_shares', 'defensive_win_shares', 'win_shares', 'win_shares_per_48_minutes', 'offensive_box_plus_minus', 'defensive_box_plus_minus', 'box_plus_minus', 'value_over_replacement_player']].apply(lambda x: x.multiply(multi_df.loc[x.index, 'games_played'], axis=0)).groupby('name').sum()
    #combine total games for each player
    total_games = multi_df.groupby('name')['games_played'].sum()
    
    #calculate the averages
    combo_stats = combo_stats.divide(total_games, axis=0).reset_index()
    #concat the dataframe with the combined stats with the old dataframe.
    df = pd.concat([df, combo_stats], axis = 0).reset_index(drop = True)
    df.drop(columns = 'games_played', inplace = True)
    return df

#define a function that scrape basketball reference per year stats
def get_per_game_stat(year):
    req = requests.get(f'https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html')
    soup = BeautifulSoup(req.content, 'html.parser')
    per_game_stat = []
    
    #the stats that I want in my dataframe
    stats = {
        'player': 'name',
        'mp_per_g' : 'mpg',
        'fg_per_g' : 'fgm_per_g',
        'fga_per_g' : 'fga_per_g',
        'fg_pct' : 'fg_pct',
        'fg3_per_g' : 'fg3m_per_g',
        'fg3a_per_g' : 'fg3a_per_g',
        'fg3_pct' : 'fg3_pct',
        'fg2_per_g' : 'fg2m_per_g',
        'fg2a_per_g' : 'fg2a_per_g',
        'fg2_pct' : 'fg2_pct',
        'efg_pct' : 'efg_pct',
        'ft_per_g' : 'ftm_per_g',
        'fta_per_g' : 'fta_per_g',
        'ft_pct' : 'ft_pct',
        'orb_per_g': 'orb_per_g',
        'drb_per_g' : 'drb_per_g',
        'trb_per_g' : 'trb_per_g',
        'ast_per_g' : 'ast_per_g',
        'stl_per_g' : 'stl_per_g',
        'blk_per_g' : 'blk_per_g',
        'tov_per_g' : 'tov_per_g',
        'pf_per_g' : 'pf_per_g',
        'pts_per_g' : 'ppg',
        #added team so that I can deal with traded players data
        'team_id': 'team'
    }
        
    #finding each player and their specific stat
    for stat in soup.find('tbody').find_all('tr'):
        per_game_stat_dict = {}
        player = stat.find('td', {'data-stat':'player'})
        #need to add if statement so it only recognizes player names that are filled out
        if player:
            player_found = player.find('a')
            if player_found:
                per_game_stat_dict['name'] = player_found.getText()
        #need to add a for loop to loop through the stats and find each key in the html dictionary
        for key, value in stats.items():
            if key != 'player':
                stat_value = stat.find('td', {'data-stat': key})
                if stat_value:
                    per_game_stat_dict[value] = stat_value.getText()  
        per_game_stat.append(per_game_stat_dict)
    #create a dataframe of our stats and drop any null values
    df = pd.DataFrame(per_game_stat)
    df.dropna(inplace = True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(f'./per_game_stat/per_game_stat_{year-1}_{year}.csv', index = False)
    return df

#define function to deal with traded players
def combine_traded_player_per_game_stats(df):
    player = df['name'].value_counts()
    multi_player = player[player > 1].index
    #create a new dataframe that just has the duplicate payers in it
    multi_df = df[df['name'].isin(multi_player)]
    df = df[df['name'].apply(lambda x: x not in multi_player)]
    grouped = multi_df.groupby('name')
    
    total_list = []
    
    for player, stats in grouped:
        if 'TOT' in stats['team'].values:
            total = stats[stats['team'] == 'TOT']
            total_list.append(total)
            
    total = pd.concat(total_list, axis = 0)
    
    df = pd.concat([total, df], axis = 0).reset_index(drop = True)
    df.drop(columns = 'team', inplace = True)
    return df

#define a function that scrape any award on basketball reference
def get_award(award_list):
    all_awards = pd.DataFrame()
    for award in award_list:
        req = requests.get(f'https://www.basketball-reference.com/awards/{award}.html')
        soup = BeautifulSoup(req.content, 'html.parser')
        awards = []
    
        # Extracting each player and their specific season
        for row in soup.find('tbody').find_all('tr'):
            award_dict = {}
            season = row.find('th', {'data-stat': 'season'})
            if season:
                award_dict['season'] = season.get_text()

            player = row.find('td', {'data-stat': 'player'})
            if player:
                player_found = player.find('a')
                if player_found:
                    award_dict['name'] = player_found.getText()
            #appending back to my list
            awards.append(award_dict)
        #create a dataframe of list
        df = pd.DataFrame(awards)
        df.reset_index(drop=True, inplace=True)
        #adding a binary column to match award
        df[award.upper()] = 1
        all_awards = pd.concat([all_awards, df], ignore_index=True)
        all_awards.fillna(0, inplace = True)
        df[award.upper()].astype(int)
    return all_awards

def scrape_year(year, award_list):
    #scrape and clean total stats
    get_player_total_season_stats(year)
    df_total = pd.read_csv(f"./total_stats/{year-1}_{year}_player_season_totals.csv")
    df_total = combine_traded_player_total_stats(df_total)
    df_total = clean_total_stats(df_total)
    #scrape and clean advanced stats
    get_player_advanced_season_stats(year)
    df_advanced = pd.read_csv(f"./advanced_season_stat_total/{year-1}_{year}_advanced_player_season_totals.csv")
    df_advanced = combine_traded_player_advanced_stats(df_advanced)
    #scrape and clean per year stats
    get_per_game_stat(year)
    df_per = pd.read_csv(f'./per_game_stat/per_game_stat_{year-1}_{year}.csv')
    df_per = combine_traded_player_per_game_stats(df_per)
    
    #combine the total and advanced stats dataframes
    df = pd.merge(df_advanced, df_total, on = 'name')
    #combine the total and per year stats dataframes
    df = pd.merge(df_per, df, on = 'name')
    df = pd.get_dummies(df, columns=['positions'], dtype = int)
    #adding season column for merge purposes with awards
    df['season'] = f'{year-1}-{str(year)[-2:]}'
    
    #scrape awards and merge
    for award in award_list:
        accolade = get_award(award_list)
    all_awards = pd.merge(accolade, df_all_nba, how = 'outer', on = ['season', 'name']).fillna(0)
    #merge award and big df
    df = pd.merge(df, all_awards, how = 'left', on = ['season', 'name'])
    df.fillna(0, inplace = True)
    
    df.to_csv(f'./total/total_{year-1}_{year}.csv', index = False)