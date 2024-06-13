|Feature|Type|Description|
|---|---|---|
|mpg|float|Minutes per game|
|fgm_per_g|float|Field goals made per game|
|fga_per_g|float|Field goals attempted per game|
|fg_pct|float|Field goal percentage|
|fg3m_per_g|float|3 point field goals made per game|
|fg3a_per_g|float|3 point field goals attempted per game|
|fg3_pct|float|3 point field goals percentage|
|fg2m_per_g|float|2 point field goals made per game|
|fg2a_per_g|float|2 point field goals attempted per game|
|fg2_pct|float|2 point field goals percentage|
|efg_pct|float|Effective field goal percentage: Adjusts field goal percentage to account for the fact that three-point field goals count for three points, while all other field goals only count for two points|
|ftm_per_g|float|Free throws made per game|
|fta_per_g|float|Free throws attempted per game|
|ft_pct|float|Free throw percentage|
|orb_per_g|float|Offensive rebounds per game|
|drb_per_g|float|Defensive rebounds per game|
|trb_per_g|float|Total rebounds per game|
|ast_per_g|float|Assists per game|
|stl_per_g|float|Steals per game|
|blk_per_g|float|Blocks per game|
|tov_per_g|float|Turnovers per game|
|pf_per_g|float|Personal fouls per game|
|ppg|float|Points per game|
|player_effeciency_rating|float|Player effeciency rating: Advanced analytic that rates a player's per-minute productivity|
|true_shooting_percentage|float|True shooting percentage: Advanced analytic that measures a player's efficiency at shooting the ball|
|three_point_attempt_rate|float|Three point attempt rate: Advanced analytic that measures the percentage of total field goal attempts that are 3-pt shots|
|free_throw_attempt_rate|float|Free throw attempt rate: Advanced analytic that measures the ratio of Free Throw Attempts to Field Goal Attempts|
|offensive_rebound_percentage|float|Offensive rebound percentage: Advanced analytic that measures the ratio between the player's offensive rebounds and the sum of the team's offensive rebounds plus the opponent's defensive rebounds, all multiplied by the player's percentage of minutes on the court|
|defensive_rebound_percentage|float|Defensive rebound percentage: Advanced analytic that measures the ratio between the player's defensive rebounds and the sum of the team's defensive rebounds plus the opponent's offensive rebounds, all multiplied by the player's percentage of minutes on the court|
|total_rebound_percentage|float|Total rebound percentage: Advanced analytic that measures the ratio by dividing the number of rebounds collected by a player by the total number of missed shots|
|assist_percentage|float|Assist percentage: Advanced analytic that measures an estimate of the percentage of teammate field goals a player assisted while he was on the floor|
|steal_percentage|float|Steal percentage: Advanced analytic that measures an estimate of the percentage of opponent possessions that end with a steal by the player while he was on the floor|
|block_percentage|float|Block percentage: Advanced analytic that measures an estimate of the percentage of opponent possessions that end with a block by the player while he was on the floor|
|turnover_percentage|float|Turnover percentage: Advanced analytic that measures an estimate of turnovers per 100 plays|
|usage_percentage|float|Usage percentage: Advanced analytic that measures an estimate of the percentage of team plays used by a player while he was on the floor|
|offensive_win_shares|float|Offensive win shares: Advanced analytic that is measured by (marginal offense) / (marginal points per win)|
|defensive_win_shares|float|Defensive win shares: Advanced analytic that is measured by (marginal defense) / (marginal points per win)|
|win_shares|float|Win shares: Advanced analytic that attempts to divvy up credit for team success to the individuals on the team|
|win_shares_per_48_minutes|float|Win shares per 48 minutes: Advanced analytic that attempts to divvy up credit for team success to the individuals on the team per 48 minutes|
|offensive_box_plus_minus|float|Offensive box plus minus: Advanced analytic that estimates the impact a player has on his team's offensive performance per 100 possessions, compared to the league average|
|defensive_box_plus_minus|float|Defensive box plus minus: Advanced analytic that estimates the impact a player has on his team's defensive performance per 100 possessions, compared to the league average| 
|box_plus_minus|float|Box plus minus: Advanced analytic that estimates the points per 100 possessions that a player contributed above a league-average player|
|value_over_replacement_player|float|Value over replacement player: Advanced analytic that measures a box score estimate of the points per 100 team possessions that a player contributed above a replacement-level player, translated to an average team and prorated to an 82-game season|
|age|integer|Age of the player|
|games_played|integer|Games played in a season|
|games_started|integer|Games started in a season|
|minutes_played|integer|Minutes played in a season|
|made_field_goals|integer|Total made field goals in a season|
|attempted_field_goals|integer|Total attempted field goals in a season|
|made_three_point_field_goals|integer|Total made three point field goals in a season|
|attempted_three_point_field_goals|integer|Total attempted three point field goals in a season|
|made_free_throws|integer|Total made free throws in a season|
|attempted_free_throws|integer|Total attempted free throws in a season|
|offensive_rebounds|integer|Total offensive rebounds in a season|
|defensive_rebounds|integer|Total defensive rebounds in a season|
|assists|integer|Total assists in a season|
|steals|integer|Total steals in a season|
|blocks|integer|Total blocks in a season|
|turnovers|integer|Total turnovers in a season|
|personal_fouls|integer|Total personal fouls in a season|
|points|integer|Total points in a season|
|target_encoded|integer|The encoded target variable: 0: no award, 1: All-NBA 1st Team, 2: All-NBA 2nd Team, 3: All-NBA 3rd Team|