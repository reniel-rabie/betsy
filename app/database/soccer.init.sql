CREATE TABLE IF NOT EXISTS soccer_fixtures (

    -- connect fixtures and soccer_fixtures
    uuid UUID NOT NULL
    FOREIGN KEY (uuid) REFERENCES fixtures (uuid)

    -- days since last match
    home_days_since_last_match_1 INT,
    home_days_since_last_match_2 INT,
    home_days_since_last_match_3 INT,
    home_days_since_last_match_4 INT,
    home_days_since_last_match_5 INT,
    home_days_since_last_match_6 INT,
    home_days_since_last_match_7 INT,
    home_days_since_last_match_8 INT,
    home_days_since_last_match_9 INT,
    home_days_since_last_match_10 INT,

    away_days_since_last_match_1 INT,
    away_days_since_last_match_2 INT,
    away_days_since_last_match_3 INT,
    away_days_since_last_match_4 INT,
    away_days_since_last_match_5 INT,
    away_days_since_last_match_6 INT,
    away_days_since_last_match_7 INT,
    away_days_since_last_match_8 INT,
    away_days_since_last_match_9 INT,
    away_days_since_last_match_10 INT,

    -- goals for
    home_team_goals INT,
    away_team_goals INT,
    home_half_goals INT,
    away_half_goals INT,

    home_goals_last_1 INT,
    home_goals_last_2 INT,
    home_goals_last_3 INT,
    home_goals_last_4 INT,
    home_goals_last_5 INT,
    home_goals_last_6 INT,
    home_goals_last_7 INT,
    home_goals_last_8 INT,
    home_goals_last_9 INT,
    home_goals_last_10 INT,

    away_goals_last_1 INT,
    away_goals_last_2 INT,
    away_goals_last_3 INT,
    away_goals_last_4 INT,
    away_goals_last_5 INT,
    away_goals_last_6 INT,
    away_goals_last_7 INT,
    away_goals_last_8 INT,
    away_goals_last_9 INT,
    away_goals_last_10 INT,


    -- average goals for
    home_avg_goals_last_1 INT,
    home_avg_goals_last_2 INT,
    home_avg_goals_last_3 INT,
    home_avg_goals_last_4 INT,
    home_avg_goals_last_5 INT,
    home_avg_goals_last_6 INT,
    home_avg_goals_last_7 INT,
    home_avg_goals_last_8 INT,
    home_avg_goals_last_9 INT,
    home_avg_goals_last_10 INT,

    away_avg_goals_last_1 INT,
    away_avg_goals_last_2 INT,
    away_avg_goals_last_3 INT,
    away_avg_goals_last_4 INT,
    away_avg_goals_last_5 INT,
    away_avg_goals_last_6 INT,
    away_avg_goals_last_7 INT,
    away_avg_goals_last_8 INT,
    away_avg_goals_last_9 INT,
    away_avg_goals_last_10 INT,

    -- goals against
    home_goals_against_last_1 INT,
    home_goals_against_last_2 INT,
    home_goals_against_last_3 INT,
    home_goals_against_last_4 INT,
    home_goals_against_last_5 INT,
    home_goals_against_last_6 INT,
    home_goals_against_last_7 INT,
    home_goals_against_last_8 INT,
    home_goals_against_last_9 INT,
    home_goals_against_last_10 INT,

    away_goals_against_last_1 INT,
    away_goals_against_last_2 INT,
    away_goals_against_last_3 INT,
    away_goals_against_last_4 INT,
    away_goals_against_last_5 INT,
    away_goals_against_last_6 INT,
    away_goals_against_last_7 INT,
    away_goals_against_last_8 INT,
    away_goals_against_last_9 INT,
    away_goals_against_last_10 INT,

    -- average goals against
    home_avg_goals_against_last_1 INT,
    home_avg_goals_against_last_2 INT,
    home_avg_goals_against_last_3 INT,
    home_avg_goals_against_last_4 INT,
    home_avg_goals_against_last_5 INT,
    home_avg_goals_against_last_6 INT,
    home_avg_goals_against_last_7 INT,
    home_avg_goals_against_last_8 INT,
    home_avg_goals_against_last_9 INT,
    home_avg_goals_against_last_10 INT,

    away_avg_goals_against_last_1 INT,
    away_avg_goals_against_last_2 INT,
    away_avg_goals_against_last_3 INT,
    away_avg_goals_against_last_4 INT,
    away_avg_goals_against_last_5 INT,
    away_avg_goals_against_last_6 INT,
    away_avg_goals_against_last_7 INT,
    away_avg_goals_against_last_8 INT,
    away_avg_goals_against_last_9 INT,
    away_avg_goals_against_last_10 INT,

    -- net goals
    home_net_goals_last_1 INT,
    home_net_goals_last_2 INT,
    home_net_goals_last_3 INT,
    home_net_goals_last_4 INT,
    home_net_goals_last_5 INT,
    home_net_goals_last_6 INT,
    home_net_goals_last_7 INT,
    home_net_goals_last_8 INT,
    home_net_goals_last_9 INT,
    home_net_goals_last_10 INT,

    away_net_goals_last_1 INT,
    away_net_goals_last_2 INT,
    away_net_goals_last_3 INT,
    away_net_goals_last_4 INT,
    away_net_goals_last_5 INT,
    away_net_goals_last_6 INT,
    away_net_goals_last_7 INT,
    away_net_goals_last_8 INT,
    away_net_goals_last_9 INT,
    away_net_goals_last_10 INT,

    -- shots
    home_shots INT,
    away_shots INT,

    home_shots_last_1 INT,
    home_shots_last_2 INT,
    home_shots_last_3 INT,
    home_shots_last_4 INT,
    home_shots_last_5 INT,
    home_shots_last_6 INT,
    home_shots_last_7 INT,
    home_shots_last_8 INT,
    home_shots_last_9 INT,
    home_shots_last_10 INT,

    away_shots_last_1 INT,
    away_shots_last_2 INT,
    away_shots_last_3 INT,
    away_shots_last_4 INT,
    away_shots_last_5 INT,
    away_shots_last_6 INT,
    away_shots_last_7 INT,
    away_shots_last_8 INT,
    away_shots_last_9 INT,
    away_shots_last_10 INT,

    -- shots on target
    home_shots_on_target INT,
    away_shots_on_target INT,

    home_shots_on_target_last_1 INT,
    home_shots_on_target_last_2 INT,
    home_shots_on_target_last_3 INT,
    home_shots_on_target_last_4 INT,
    home_shots_on_target_last_5 INT,
    home_shots_on_target_last_6 INT,
    home_shots_on_target_last_7 INT,
    home_shots_on_target_last_8 INT,
    home_shots_on_target_last_9 INT,
    home_shots_on_target_last_10 INT,

    away_shots_on_target_last_1 INT,
    away_shots_on_target_last_2 INT,
    away_shots_on_target_last_3 INT,
    away_shots_on_target_last_4 INT,
    away_shots_on_target_last_5 INT,
    away_shots_on_target_last_6 INT,
    away_shots_on_target_last_7 INT,
    away_shots_on_target_last_8 INT,
    away_shots_on_target_last_9 INT,
    away_shots_on_target_last_10 INT,

    -- corners
    home_corners INT,
    away_corners INT,

    home_corners_last_1 INT,
    home_corners_last_2 INT,
    home_corners_last_3 INT,
    home_corners_last_4 INT,
    home_corners_last_5 INT,
    home_corners_last_6 INT,
    home_corners_last_7 INT,
    home_corners_last_8 INT,
    home_corners_last_9 INT,
    home_corners_last_10 INT,

    away_corners_last_1 INT,
    away_corners_last_2 INT,
    away_corners_last_3 INT,
    away_corners_last_4 INT,
    away_corners_last_5 INT,
    away_corners_last_6 INT,
    away_corners_last_7 INT,
    away_corners_last_8 INT,
    away_corners_last_9 INT,
    away_corners_last_10 INT,

    -- fouls
    home_fouls INT,
    away_fouls INT,

    home_fouls_last_1 INT,
    home_fouls_last_2 INT,
    home_fouls_last_3 INT,
    home_fouls_last_4 INT,
    home_fouls_last_5 INT,
    home_fouls_last_6 INT,
    home_fouls_last_7 INT,
    home_fouls_last_8 INT,
    home_fouls_last_9 INT,
    home_fouls_last_10 INT,

    away_fouls_last_1 INT,
    away_fouls_last_2 INT,
    away_fouls_last_3 INT,
    away_fouls_last_4 INT,
    away_fouls_last_5 INT,
    away_fouls_last_6 INT,
    away_fouls_last_7 INT,
    away_fouls_last_8 INT,
    away_fouls_last_9 INT,
    away_fouls_last_10 INT,

    -- cards
    home_yellow_cards INT,
    away_yellow_cards INT,
    home_red_cards INT,
    away_red_cards INT,

    home_yellow_cards_last_1 INT,
    home_yellow_cards_last_2 INT,
    home_yellow_cards_last_3 INT,
    home_yellow_cards_last_4 INT,
    home_yellow_cards_last_5 INT,
    home_yellow_cards_last_6 INT,
    home_yellow_cards_last_7 INT,
    home_yellow_cards_last_8 INT,
    home_yellow_cards_last_9 INT,
    home_yellow_cards_last_10 INT,

    away_yellow_cards_last_1 INT,
    away_yellow_cards_last_2 INT,
    away_yellow_cards_last_3 INT,
    away_yellow_cards_last_4 INT,
    away_yellow_cards_last_5 INT,
    away_yellow_cards_last_6 INT,
    away_yellow_cards_last_7 INT,
    away_yellow_cards_last_8 INT,
    away_yellow_cards_last_9 INT,
    away_yellow_cards_last_10 INT,

    home_red_cards_last_1 INT,
    home_red_cards_last_2 INT,
    home_red_cards_last_3 INT,
    home_red_cards_last_4 INT,
    home_red_cards_last_5 INT,
    home_red_cards_last_6 INT,
    home_red_cards_last_7 INT,
    home_red_cards_last_8 INT,
    home_red_cards_last_9 INT,
    home_red_cards_last_10 INT,

    away_red_cards_last_1 INT,
    away_red_cards_last_2 INT,
    away_red_cards_last_3 INT,
    away_red_cards_last_4 INT,
    away_red_cards_last_5 INT,
    away_red_cards_last_6 INT,
    away_red_cards_last_7 INT,
    away_red_cards_last_8 INT,
    away_red_cards_last_9 INT,
    away_red_cards_last_10 INT,

    -- offsides
    home_offsides INT,
    away_offsides INT,

    home_offsides_last_1 INT,
    home_offsides_last_2 INT,
    home_offsides_last_3 INT,
    home_offsides_last_4 INT,
    home_offsides_last_5 INT,
    home_offsides_last_6 INT,
    home_offsides_last_7 INT,
    home_offsides_last_8 INT,
    home_offsides_last_9 INT,
    home_offsides_last_10 INT,

    away_offsides_last_1 INT,
    away_offsides_last_2 INT,
    away_offsides_last_3 INT,
    away_offsides_last_4 INT,
    away_offsides_last_5 INT,
    away_offsides_last_6 INT,
    away_offsides_last_7 INT,
    away_offsides_last_8 INT,
    away_offsides_last_9 INT,
    away_offsides_last_10 INT,

    -- possession
    home_possession INT,
    away_possession INT,

    home_avg_possession_last_1 INT,
    home_avg_possession_last_2 INT,
    home_avg_possession_last_3 INT,
    home_avg_possession_last_4 INT,
    home_avg_possession_last_5 INT,
    home_avg_possession_last_6 INT,
    home_avg_possession_last_7 INT,
    home_avg_possession_last_8 INT,
    home_avg_possession_last_9 INT,
    home_avg_possession_last_10 INT,

    away_avg_possession_last_1 INT,
    away_avg_possession_last_2 INT,
    away_avg_possession_last_3 INT,
    away_avg_possession_last_4 INT,
    away_avg_possession_last_5 INT,
    away_avg_possession_last_6 INT,
    away_avg_possession_last_7 INT,
    away_avg_possession_last_8 INT,
    away_avg_possession_last_9 INT,
    away_avg_possession_last_10 INT,

    -- passes
    home_passes INT,
    away_passes INT,

    home_passes_last_1 INT,
    home_passes_last_2 INT,
    home_passes_last_3 INT,
    home_passes_last_4 INT,
    home_passes_last_5 INT,
    home_passes_last_6 INT,
    home_passes_last_7 INT,
    home_passes_last_8 INT,
    home_passes_last_9 INT,
    home_passes_last_10 INT,

    away_passes_last_1 INT,
    away_passes_last_2 INT,
    away_passes_last_3 INT,
    away_passes_last_4 INT,
    away_passes_last_5 INT,
    away_passes_last_6 INT,
    away_passes_last_7 INT,
    away_passes_last_8 INT,
    away_passes_last_9 INT,
    away_passes_last_10 INT,

    -- tackles
    home_tackles INT,
    away_tackles INT,

    home_tackles_last_1 INT,
    home_tackles_last_2 INT,
    home_tackles_last_3 INT,
    home_tackles_last_4 INT,
    home_tackles_last_5 INT,
    home_tackles_last_6 INT,
    home_tackles_last_7 INT,
    home_tackles_last_8 INT,
    home_tackles_last_9 INT,
    home_tackles_last_10 INT,

    away_tackles_last_1 INT,
    away_tackles_last_2 INT,
    away_tackles_last_3 INT,
    away_tackles_last_4 INT,
    away_tackles_last_5 INT,
    away_tackles_last_6 INT,
    away_tackles_last_7 INT,
    away_tackles_last_8 INT,
    away_tackles_last_9 INT,
    away_tackles_last_10 INT,

    -- saves
    home_saves INT,
    away_saves INT,

    home_saves_last_1 INT,
    home_saves_last_2 INT,
    home_saves_last_3 INT,
    home_saves_last_4 INT,
    home_saves_last_5 INT,
    home_saves_last_6 INT,
    home_saves_last_7 INT,
    home_saves_last_8 INT,
    home_saves_last_9 INT,
    home_saves_last_10 INT,

    away_saves_last_1 INT,
    away_saves_last_2 INT,
    away_saves_last_3 INT,
    away_saves_last_4 INT,
    away_saves_last_5 INT,
    away_saves_last_6 INT,
    away_saves_last_7 INT,
    away_saves_last_8 INT,
    away_saves_last_9 INT,
    away_saves_last_10 INT,

    -- previous results

    -- wins
    home_wins_last_1 INT,
    home_wins_last_2 INT,
    home_wins_last_3 INT,
    home_wins_last_4 INT,
    home_wins_last_5 INT,
    home_wins_last_6 INT,
    home_wins_last_7 INT,
    home_wins_last_8 INT,
    home_wins_last_9 INT,
    home_wins_last_10 INT,
    away_wins_last_1 INT,
    away_wins_last_2 INT,
    away_wins_last_3 INT,
    away_wins_last_4 INT,
    away_wins_last_5 INT,
    away_wins_last_6 INT,
    away_wins_last_7 INT,
    away_wins_last_8 INT,
    away_wins_last_9 INT,
    away_wins_last_10 INT,

    -- draws
    home_draws_last_1 INT,
    home_draws_last_2 INT,
    home_draws_last_3 INT,
    home_draws_last_4 INT,
    home_draws_last_5 INT,
    home_draws_last_6 INT,
    home_draws_last_7 INT,
    home_draws_last_8 INT,
    home_draws_last_9 INT,
    home_draws_last_10 INT,
    away_draws_last_1 INT,
    away_draws_last_2 INT,
    away_draws_last_3 INT,
    away_draws_last_4 INT,
    away_draws_last_5 INT,
    away_draws_last_6 INT,
    away_draws_last_7 INT,
    away_draws_last_8 INT,
    away_draws_last_9 INT,
    away_draws_last_10 INT,

    -- losses
    home_losses_last_1 INT,
    home_losses_last_2 INT,
    home_losses_last_3 INT,
    home_losses_last_4 INT,
    home_losses_last_5 INT,
    home_losses_last_6 INT,
    home_losses_last_7 INT,
    home_losses_last_8 INT,
    home_losses_last_9 INT,
    home_losses_last_10 INT,
    away_losses_last_1 INT,
    away_losses_last_2 INT,
    away_losses_last_3 INT,
    away_losses_last_4 INT,
    away_losses_last_5 INT,
    away_losses_last_6 INT,
    away_losses_last_7 INT,
    away_losses_last_8 INT,
    away_losses_last_9 INT,
    away_losses_last_10 INT,

    FOREIGN KEY (home_team_id) REFERENCES teams (uuid),
    FOREIGN KEY (away_team_id) REFERENCES teams (uuid),
    FOREIGN KEY (venue_id) REFERENCES venues (uuid)
);