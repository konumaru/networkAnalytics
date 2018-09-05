CREATE TABLE IF NOT EXISTS for_research.status_info (
                    user_id BIGINT,
                    screen_name TEXT,
                    status_id BIGINT,
                    status_text TEXT,
                    PRIMARY KEY(status_id)
                )