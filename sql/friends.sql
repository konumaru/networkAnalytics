CREATE TABLE IF NOT EXISTS for_research.friends (
                    user_id BIGINT,
                    screen_name TEXT,
                    friend_ids TEXT,
                    PRIMARY KEY(user_id)
                )