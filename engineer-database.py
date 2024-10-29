import sqlite3

conn = sqlite3.connect('data.db')

user_login_query = '''CREATE TABLE IF NOT EXISTS user_login(
                user_id INT NOT NULL,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                PRIMARY KEY (user_id),
                FOREIGN KEY (user_id) REFERENCES user_info (user_id)
                )
                '''
conn.execute(user_login_query)

User_info_query = '''CREATE TABLE IF NOT EXISTS user_data
                (user_id INT NOT NULL, 
                first_name VARCHAR(255) NOT NULL, 
                last_name VARCHAR(255) NOT NULL, 
                title VARCHAR(255), 
                age INT,
                PRIMARY KEY (user_id)
                FOREIGN KEY (user_id) REFERENCES user_login (user_id)
                )
                '''
conn.execute(User_info_query)

Trade_requirements_query = '''CREATE TABLE IF NOT EXISTS trade_requirements
                (ticker VARCHAR(255) NOT NULL,
                price_entry INT NOT NULL,
                volume_entry INT NOT NULL,
                volume_exit INT NOT NULL,
                ma_entry_20 INT NOT NULL,
                ma_exit_20 INT NOT NULL,
                ma_entry_50 INT NOT NULL,
                ma_exit_50 INT NOT NULL,
                vwap_entry INT NOT NULL,
                vwap_exit INT NOT NULL,
                rsi_entry INT NOT NULL,
                rsi_exit INT NOT NULL
                )
                '''
conn.execute(Trade_requirements_query)

News_results_query = '''CREATE TABLE IF NOT EXISTS news_results
                (news_id VARCHAR(255) NOT NULL,
                index_id VARCHAR(255) NOT NULL,
                expected_number INT NOT NULL,
                actual_number INT NOT NULL,
                change_1_hour INT NOT NULL,
                change_1_day INT NOT NULL,
                change_1_week INT NOT NULL
                )
                '''
conn.execute(News_results_query)