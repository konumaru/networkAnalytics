CREATE TABLE IF NOT EXISTS for_research.user_info (
                    slave_screen_name TEXT,
                    user_id BIGINT,
                    screen_name TEXT,
                    friends_count INT,
                    followers_count INT,
                    self_discription TEXT,
                    protected INT,
                    PRIMARY KEY(user_id)
                )